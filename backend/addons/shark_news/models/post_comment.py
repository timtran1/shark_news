# coding: utf-8
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class PostComment(models.Model):
    _name = 'post.comment'
    _parent_name = 'parent_id'
    # _parent_store = True
    _order = "create_date desc, likes desc"

    name = fields.Text()
    post_id = fields.Many2one('post')
    post_reference_id = fields.Many2one('post')
    user_id = fields.Many2one('res.users', ondelete='cascade')
    active = fields.Boolean(related='user_id.active')

    parent_id = fields.Many2one('post.comment')
    child_ids = fields.One2many('post.comment', 'parent_id')

    likes = fields.Integer(default=1)

    def like(self):
        user = self.env.user
        user_field = user.user_fields_id

        for comment in self:
            if comment not in user_field.liked_comment_ids:
                user_field.liked_comment_ids += comment
                comment.likes += 1
            else:
                user_field.liked_comment_ids -= comment
                comment.likes -= 1

    @api.model
    def create(self, vals):
        if vals.get('post_id'):
            vals.update({'post_reference_id': vals.get('post_id')})
        elif vals.get('parent_id'):
            vals.update({'post_reference_id': self.browse(vals.get('parent_id')).post_reference_id.id})

        return super(PostComment, self).create(vals)
