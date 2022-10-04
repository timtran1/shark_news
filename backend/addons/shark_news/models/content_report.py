# coding: utf-8
import logging
from odoo import api, fields, models, _
from bs4 import BeautifulSoup
import urllib.request
import json

_logger = logging.getLogger(__name__)


class ContentReport(models.Model):
    _name = 'content.report'

    user_id = fields.Many2one('res.users', ondelete='cascade')
    active = fields.Boolean(related='user_id.active')
    post_id = fields.Many2one('post')
    comment_id = fields.Many2one('post.comment')
    reason = fields.Text()
    state = fields.Selection(selection=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed')
    ], default='pending')