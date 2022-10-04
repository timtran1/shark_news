# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request, Response
from odoo.addons.web.controllers.main import ensure_db
from odoo.exceptions import AccessDenied
import jwt
import json
import datetime

_logger = logging.getLogger(__name__)


class AuthTokenController(http.Controller):
    @http.route('/token_login', type='http', auth='none', cors='*', methods=['POST'], csrf=False)
    def token_login(self, **args):
        ensure_db()
        request.env['res.users'].sudo()
        db_name = request.session.db
        req = request

        try:
            user_id = request.session.authenticate(db_name, args.get('login'), args.get('password'))
            request.session.uid = user_id
            request.session.login = args.get('login')
            request.session.get_context()
            exp = args.get('exp', None) #must be unix timestamp (int)

            user = request.env['res.users'].sudo().browse(user_id)
            user._update_last_login()
            secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')

            data = {
                'uid': user_id,
                'iat': datetime.datetime.utcnow(),
            }
            if exp is not None:
                data.update({'exp': int(exp)})

            token = jwt.encode(data, secret, algorithm="HS256")
            return Response(json.dumps({
                'success': True,
                'access_token': token.decode(),#byte string to regular string
                'db_name': db_name,
                'uid': user_id,
            }), content_type='application/json', status=200)

        except AccessDenied:
            return Response(json.dumps({
                'success': False, 'message': 'Invalid login information'
            }), content_type='application/json', status=403)
