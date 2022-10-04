# -*- coding: utf-8 -*-

import logging
import json
from odoo import http, fields
from odoo.http import request, Response
import string
from .mixpanel import track

_logger = logging.getLogger(__name__)


class Controller(http.Controller):

    @http.route(['/post/rate/<int:post_id>/<int:rating>'], type='http', auth='user', website=True, cors='*')
    def post_rate(self, post_id, rating, **kw):
        res = request.env['post.rating'].sudo().create({
            'post_id': int(post_id),
            'rating': int(rating)/1000,
            'user_fields_id': request.env.user.user_fields_id.id
        })
        track(request.env.user, 'Post rate', {'post_id': post_id})

        return Response(str(res.id), content_type='application/json', status=200)

    @http.route(['/post/click/<int:post_id>'], type='http', auth='user', website=True, cors='*')
    def post_click(self, post_id, **kw):
        track(request.env.user, 'Post click', {'post_id': post_id})
        return Response('ok', content_type='application/json', status=200)

    @http.route(['/session/end'], type='http', auth='user', website=True, cors='*')
    def session_end(self, **kw):
        track(request.env.user, 'Session ended')
        return Response('ok', content_type='application/json', status=200)

    @http.route(['/session/start'], type='http', auth='user', website=True, cors='*')
    def session_start(self, **kw):
        track(request.env.user, 'Session started')
        return Response('ok', content_type='application/json', status=200)