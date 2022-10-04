# -*- coding: utf-8 -*-

import logging
import json
from odoo import http, fields
from odoo.http import request, Response
import string
from datetime import datetime, timedelta
from .mixpanel import track

alphabet = string.ascii_lowercase + string.digits
_logger = logging.getLogger(__name__)


class Controller(http.Controller):

    @http.route(['/feed'], type='http', auth='user', website=True, cors='*')
    def feed(self, **kw):
        user = request.env['res.users'].sudo().browse(request.uid)
        user_fields = user.user_fields_id
        offset = int(kw.get('offset', 0))

        block_filter_user_fields = user_fields.blocked_by_user_field_ids + user_fields.blocked_user_field_ids

        posts = request.env['post'].sudo().search([
            # ('create_date', '>', fields.Datetime.to_string(datetime.now() - timedelta(days=1))),
            # ('id', 'not in', user_fields.read_post_ids.ids)
            ('published', '=', True),
            ('shadow_hide', '=', False),
            ('user_id', 'not in', block_filter_user_fields.mapped('user_id').ids)
        ], limit=5, offset=offset)
        _logger.info(posts)
        user_fields.read_post_ids += posts

        res = {
            'posts': [{
                'id': post.id,
                'title': post.name,
                'url': post.url,
                'image': post.img_url,
                'subtext': post.subtext or '',
                'can_load_iframe': post.can_load_iframe,
                'likes': post.likes,
                'comment_count': post.comment_count,
                'liked': request.env.user.user_fields_id in post.liked_user_field_ids,
                'user': {
                    'id': post.user_id.id,
                    'name': post.user_id.name,
                    'image': '/user_image/%s' % post.user_id.id
                } if post.user_id else None,
            } for post in posts]
        }

        track(user, 'Feed request')

        return Response(json.dumps(res), content_type='application/json', status=200)