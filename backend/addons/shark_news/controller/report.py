# -*- coding: utf-8 -*-

import logging
import json
from odoo import http, fields
from odoo.http import request, Response
import string

alphabet = string.ascii_lowercase + string.digits

_logger = logging.getLogger(__name__)


class Controller(http.Controller):

    @http.route(['/report/new'], type='http', auth='user', website=True, cors='*')
    def report_new(self, reason, post_id=None, comment_id=None, **kw):
        report = request.env['content.report'].sudo().create({
            'reason': reason,
            'post_id': post_id,
            'comment_id': comment_id,
            'user_id': request.env.user.id
        })

        return Response(json.dumps({
            'report': {'id': report.id}
        }), content_type='application/json', status=200)

    @http.route(['/block'], type='http', auth='user', website=True, cors='*')
    def block(self, user_id, **kw):
        user = request.env.user
        user_field = user.user_fields_id

        blocked_user = request.env['res.users'].sudo().browse(int(user_id))
        blocked_user_field = blocked_user.user_fields_id

        if user == blocked_user:
            return Response('cannot block self', status=400)

        user_field.blocked_user_field_ids += blocked_user_field

        return Response(json.dumps({
            'success': True
        }), content_type='application/json', status=200)
