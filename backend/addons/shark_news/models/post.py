# coding: utf-8
import logging
from odoo import api, fields, models, _
from bs4 import BeautifulSoup
import urllib.request
import json
from datetime import timedelta
from random import randrange
from .post_bots import run_fark_bot, run_slashdot_bot, run_reddit_bot, headers, get_img_url, can_load_from_iframe
import requests as r

_logger = logging.getLogger(__name__)


class Post(models.Model):
    _name = 'post'
    _order = "scheduled_date desc, create_date desc"

    name = fields.Char()
    img_url = fields.Char()
    subtext = fields.Text()
    url = fields.Char()
    comment_ids = fields.One2many('post.comment', 'post_id')
    user_id = fields.Many2one('res.users', ondelete='cascade')
    active = fields.Boolean(related='user_id.active')
    can_load_iframe = fields.Boolean(default=True)

    likes = fields.Integer(compute='_compute_likes')
    likes_booster = fields.Integer(default=0)
    comment_count = fields.Integer(compute='_compute_comment_count')
    liked_user_field_ids = fields.Many2many('res.users.fields', 'liked_post_user_rel', 'post_id', 'user_field_id')

    scheduled_date = fields.Datetime(default=fields.Datetime.now)
    published = fields.Boolean(default=True)
    shadow_hide = fields.Boolean(default=False)

    fark_id = fields.Char()
    slashdot_id = fields.Char()
    reddit_id = fields.Char()

    def bot_post(self):
        now = fields.Datetime.now()
        i = 1
        
        # if now.hour in [11, 12]: #gmt
        if True:
            slashdot_posts = run_slashdot_bot()
            for post in slashdot_posts:
                if not self.search([('slashdot_id', '=', post['slashdot_id'])]):
                    post.update({
                        'user_id': self.env.ref('shark_news.bot8').id,
                        'scheduled_date': now + timedelta(seconds=i)
                    })
                    self.create(post)
                    i += 1

            fark_posts = run_fark_bot()
            for post in fark_posts:
                if not self.search([('fark_id', '=', post['fark_id'])]):
                    post.update({
                        'user_id': self.env.ref('shark_news.bot' + str(randrange(1, 14))).id,
                        'scheduled_date': now + timedelta(seconds=i)
                    })
                    self.create(post)
                    i += 1

            reddit_posts = run_reddit_bot()
            for post in reddit_posts:
                if not self.search([('reddit_id', '=', post['reddit_id'])]):
                    post.update({
                        'user_id': self.env.ref('shark_news.bot' + str(randrange(1, 14))).id,
                        'scheduled_date': now + timedelta(seconds=i)
                    })
                    self.create(post)
                    i += 1

    def check_scheduling(self):
        _logger.info('CHECK POST SCHEDULING')
        scheduled_posts = self.search([
            ('scheduled_date', '!=', False),
            ('published', '=', False)
        ])
        now = fields.Datetime.now()
        for post in scheduled_posts:
            if now > post.scheduled_date:
                post.write({'published': True})

    def maintenance_function(self):
        # farks = self.search([('fark_id', '!=', False)])
        # farks.unlink()
        pass

    def like(self):
        user = self.env.user
        user_field = user.user_fields_id

        for post in self:
            if user_field not in post.liked_user_field_ids:
                post.liked_user_field_ids += user_field
            else:
                post.liked_user_field_ids -= user_field

    def _compute_likes(self):
        for post in self:
            post.likes = len(post.liked_user_field_ids) + post.likes_booster

    def _compute_comment_count(self):
        for post in self:
            comments = self.env['post.comment'].search([('post_reference_id', '=', post.id)])
            post.comment_count = len(comments)

    def get_soup(self, url):
        try:
            response = urllib.request.urlopen(url)
            soup = BeautifulSoup(response,
                                 'html.parser',
                                 from_encoding=response.info().get_param('charset'))
            return soup
        except:
            _logger.exception('Error extracting soup from %s' % url)

        return None

    def process_urls(self, vals):
        try:
            response = r.get(vals.get('url'), headers=headers, timeout=5)

            if not vals.get('img_url'):
                soup = BeautifulSoup(response.text, 'html.parser')
                vals['img_url'] = get_img_url(soup)

            vals['can_load_iframe'] = can_load_from_iframe(response.headers)

        except:
            _logger.exception('Error processing url')
            vals['can_load_iframe'] = False

        return vals

    @api.model
    def create(self, vals):
        if vals.get('url'):
            vals = self.process_urls(vals)

        return super(Post, self).create(vals)

    def write(self, vals):
        if vals.get('url'):
            vals = self.process_urls(vals)

        return super(Post, self).write(vals)
