# coding: utf-8
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class PostRating(models.Model):
    _name = 'post.rating'
    _order = "create_date desc"

    post_id = fields.Many2one('post')
    user_fields_id = fields.Many2one('res.users.fields')
    rating = fields.Float()