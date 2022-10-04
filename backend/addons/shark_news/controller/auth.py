# -*- coding: utf-8 -*-

import logging
import json
from odoo import http, fields, SUPERUSER_ID
from odoo.http import request, Response
from datetime import datetime
import string
import random
import jwt
import base64
from .mixpanel import track

alphabet = string.ascii_lowercase + string.digits

_logger = logging.getLogger(__name__)


class Controller(http.Controller):

    @http.route(['/new_user'], type='http', auth="public", website=True, cors='*')
    def new_user(self, **kw):
        password = ''.join(random.choices(alphabet, k=12))
        username = 'user_' + ''.join(random.choices(alphabet, k=12))

        db, login, password = request.env['res.users'].sudo().signup({
            'name': username,
            'login': username,
            'password': password,
            'image_1920': request.env['res.users'].sudo()._get_default_image()
        }, None)
        request.env.cr.commit()

        user_id = request.session.authenticate(db, login, password)
        request.session.uid = user_id
        request.session.login = login
        request.session.get_context()
        exp = kw.get('exp', None)  # must be unix timestamp (int)

        user = request.env['res.users'].sudo().browse(user_id)
        user._update_last_login()
        user.user_fields_id.write({
            'created_ip': request.httprequest.environ.get('HTTP_CF_CONNECTING_IP', False),
            'created_device_info': kw.get('device_info', False)
        })
        secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')

        data = {
            'uid': user_id,
            'iat': datetime.utcnow(),
        }

        if exp is not None:
            data.update({'exp': int(exp)})

        token = jwt.encode(data, secret, algorithm='HS256')

        track(user, 'New user')
        track(user, 'Session started')

        return Response(json.dumps({
            'token': token,
            'v_uid': user_id
        }), content_type='application/json', status=200)

    @http.route(['/delete_user'], type='http', auth="user", website=True, cors='*')
    def delete_user(self, **kw):
        uid = request.uid
        request.uid = SUPERUSER_ID
        user = request.env['res.users'].sudo().browse(uid)

        anon_username = 'user_' + ''.join(random.choices(alphabet, k=12))
        user.sudo().write({
            'login': anon_username,
            'active': False
        })

        track(user, 'Delete user')

        return Response('ok', status=200)

    @http.route(['/signup'], type='http', auth='user', website=True, cors='*')
    def signup(self, name, email, password, **kw):
        uid = request.uid
        user = request.env['res.users'].sudo().browse(uid)
        existing_user = request.env['res.users'].sudo().search([('login', '=', email)])

        if existing_user:
            return Response(json.dumps({'err': 'This email has been taken.'}), status=200)

        if user:
            user.write({
                'name': name,
                'login': email,
                'password': password
            })
            user.user_fields_id.write({
                'signedup': True
            })

            track(user, 'Signup')

            return Response(json.dumps({'uid': user.id}), status=200)

        return Response('user invalid', status=400)

    @http.route(['/login'], type='http', auth='public', website=True, cors='*')
    def login(self, email, password, **kw):
        try:
            uid = request.session.authenticate('localhost', email, password)
            secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
            token = jwt.encode({
                'uid': uid,
                'iat': datetime.utcnow(),
            }, secret, algorithm='HS256')

            track(request.env['res.users'].sudo().browse(uid), 'Login')

            return Response(json.dumps({
                'uid': uid,
                'token': token
            }), content_type='application/json', status=200)
        except:
            return Response(json.dumps({
                'err': 'Email or password incorrect!',
            }), content_type='application/json', status=200)

    @http.route(['/user_image/<int:user_id>'], type='http', auth='public', website=True, cors='*')
    def user_image(self, user_id, **kw):
        user = request.env['res.users'].sudo().browse(user_id)
        return Response(base64.b64decode(user.image_128), content_type='image/png')

    @http.route(['/profile/<int:user_id>'], type='http', auth='public', website=True, cors='*')
    def profile(self, user_id, **kw):
        user = request.env['res.users'].sudo().browse(user_id)
        user_fields = user.user_fields_id
        posts = request.env['post'].sudo().search([
            ('user_id', '=', user.id),
            ('published', '=', True)
        ])

        data = {
            'user': {
                'id': user.id,
                'name': user.name,
                'image': '/user_image/%s' % user.id,
                'posts': [{
                    'id': post.id,
                    'title': post.name,
                    'image': post.img_url,
                    'subtext': post.subtext or '',
                    'likes': post.likes,
                    'liked': user_fields in post.liked_user_field_ids,
                    'comment_count': post.comment_count,
                } for post in posts],
                'liked_posts': [{
                    'id': post.id,
                    'title': post.name,
                    'image': post.img_url,
                    'subtext': post.subtext or '',
                    'likes': post.likes,
                    'liked': True,
                    'comment_count': post.comment_count,
                } for post in user_fields.liked_post_ids]
            }
        }

        return Response(json.dumps(data), content_type='application/json', status=200)
