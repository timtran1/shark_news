# coding: utf-8
import logging
from odoo import api, fields, models, _
from odoo.modules.module import get_module_resource
from odoo.tools import image_process
import base64
from random import randrange

_logger = logging.getLogger(__name__)


class Users(models.Model):
    _inherit = 'res.users'

    user_fields_id = fields.Many2one('res.users.fields', compute='_compute_user_fields_id')
    bot = fields.Boolean(default=False)

    def _compute_user_fields_id(self):
        Fields = self.env['res.users.fields']
        for user in self:
            user.user_fields_id = Fields.search([('user_id', '=', user.id)], limit=1) or \
                                  Fields.create({'user_id': user.id})

    @api.model
    def create(self, vals):
        user = super(Users, self).create(vals)
        self.env['res.users.fields'].create({'user_id': user.id})
        return user

    @api.model
    def _get_default_image(self):
        image_path = get_module_resource('shark_news', 'static/img', '%s.png' % str(randrange(7)))
        image = base64.b64encode(open(image_path, 'rb').read())
        return image_process(image, colorize=False)

    def signup_bots(self):
        bots = self.search([('bot', '=', True)])
        bots.user_fields_id.write({'signedup': True})


class UserFields(models.Model):
    _name = 'res.users.fields'
    _order = 'create_date desc'

    user_id = fields.Many2one('res.users')
    name = fields.Char(related='user_id.name')
    liked_post_ids = fields.Many2many('post', 'liked_post_user_rel', 'user_field_id', 'post_id')
    read_post_ids = fields.Many2many('post')
    liked_comment_ids = fields.Many2many('post.comment')
    signedup = fields.Boolean(default=False)
    blocked_user_field_ids = fields.Many2many('res.users.fields', 'blocked_user_field_rel', 'blocker_user_field_id', 'blockee_user_field_id')
    blocked_by_user_field_ids = fields.Many2many('res.users.fields', 'blocked_user_field_rel', 'blockee_user_field_id', 'blocker_user_field_id')
    rating_ids = fields.One2many('post.rating', 'user_fields_id')

    created_ip = fields.Char()
    created_device_info = fields.Char()
    last_ip = fields.Char()
    country = fields.Char()
    city = fields.Char()
    lat = fields.Char()
    long = fields.Char()
    loc = fields.Char()
    org = fields.Char()
    last_agent = fields.Char()

    _sql_constraints = [
        ('user_id_unique', 'UNIQUE(user_id)', 'A user cannot have the same fields record twice.')
    ]
