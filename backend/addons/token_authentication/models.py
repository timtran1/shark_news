# -*- coding: utf-8 -*-

from odoo import models, fields, api, http
# from odoo.exceptions import AccessDenied
from odoo.http import request
import jwt
import logging

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_user(cls):
        token = request.httprequest.headers.get('Authorization') or request.params.get('token_login')
        if token:
            token = token.replace('Bearer ', '')
            secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
            payload = jwt.decode(token, secret, algorithms=['HS256'])
            request.uid = payload.get('uid')
            # request.session.uid = payload.get('uid')
        else:
            super(IrHttp, cls)._auth_method_user()
