# -*- coding: utf-8 -*-

import logging
import json
from odoo import http, fields
from odoo.http import request, Response
import string
from .mixpanel import track

alphabet = string.ascii_lowercase + string.digits

_logger = logging.getLogger(__name__)


class Controller(http.Controller):

    @http.route(['/post/summary/<int:post_id>'], type='http', auth="public", website=True, cors='*')
    def post_summary(self, post_id, **kw):
        post = request.env['post'].sudo().browse(post_id)

        res = {
            'post': {
                'id': post.id,
                'title': post.name,
                'likes': post.likes,
                'url': post.url,
                'can_load_iframe': post.can_load_iframe,
                'comment_count': post.comment_count,
                'liked': request.env.user.user_fields_id in post.liked_user_field_ids
            }
        }

        return Response(json.dumps(res), content_type='application/json', status=200)

    @http.route(['/post/like/<int:post_id>'], type='http', auth="user", website=True, cors='*')
    def post_like(self, post_id, **kw):
        user = request.env.user
        if not user.user_fields_id.signedup:
            return Response('signup required', content_type='application/json', status=400)

        post = request.env['post'].sudo().browse(post_id)
        post.like()

        track(user, 'Post like')

        return Response('ok', content_type='application/json', status=200)

    @http.route(['/post/new'], type='http', auth="user", website=True, cors='*')
    def post_new(self, title, **kw):
        user = request.env.user
        if not user.user_fields_id.signedup:
            return Response('signup required', content_type='application/json', status=400)

        post = request.env['post'].sudo().create({
            'name': title,
            'url': kw.get('url', None),
            'subtext': kw.get('subtext', None),
            'user_id': user.id
        })

        track(user, 'Post new')

        return Response(json.dumps({
            'post': {
                'id': post.id,
                'title': post.name,
                'image': post.img_url,
                'subtext': post.subtext or '',
                'likes': 0,
                'comment_count': 0,
                'liked': False,
                'user': {
                    'id': post.user_id.id,
                    'name': post.user_id.name,
                    'image': '/user_image/%s' % post.user_id.id
                } if post.user_id else None,
            }
        }), content_type='application/json', status=200)

    @http.route(['/post/comment'], type='http', auth="user", website=True, cors='*')
    def post_comment(self, comment, post_id, parent_comment_id=None, **kw):
        user = request.env.user
        user_field = user.user_fields_id
        if not user_field.signedup:
            return Response('blocked', status=400)

        post = request.env['post'].sudo().browse(int(post_id))
        if user_field in post.user_id.user_fields_id.blocked_user_field_ids:
            return Response('blocked', status=400)

        if parent_comment_id:
            comment = request.env['post.comment'].sudo().browse(int(parent_comment_id))
            if user_field in comment.user_id.user_fields_id.blocked_user_field_ids:
                return Response('blocked', status=400)

        comment_data = {
            'name': comment,
            'user_id': user.id
        }

        if parent_comment_id:
            comment_data.update({
                'parent_id': parent_comment_id,
                'post_reference_id': post_id
            })
        else:
            comment_data.update({
                'post_id': post_id,
            })

        res = request.env['post.comment'].sudo().create(comment_data)

        track(user, 'Post comment')

        return Response(json.dumps({
            'comment': {
                'id': res.id,
                'content': res.name,
                'likes': res.likes,
                'user': {
                    'id': res.user_id.id,
                    'name': res.user_id.name,
                    'image': '/user_image/%s' % res.user_id.id
                } if res.user_id else {},
                'children': []
            }
        }), content_type='application/json', status=200)

    def _get_comments(self, comment, user_field):
        return {
            'id': comment.id,
            'content': comment.name,
            'likes': comment.likes,
            'liked': comment in user_field.liked_comment_ids,
            'user': {
                'id': comment.user_id.id,
                'name': comment.user_id.name,
                'image': '/user_image/%s' % comment.user_id.id
            } if comment.user_id else {},
            'children': [
                self._get_comments(cmt, user_field) for cmt in comment.child_ids
                    .filtered(lambda c: user_field not in c.user_id.user_fields_id.blocked_user_field_ids)
            ]
        }

    @http.route(['/post/discussion/<int:post_id>'], type='http', auth="user", website=True, cors='*')
    def post_discussion(self, post_id, **kw):
        post = request.env['post'].sudo().browse(post_id)
        user_field = request.env.user.user_fields_id

        if user_field in post.user_id.user_fields_id.blocked_user_field_ids:
            return Response('blocked', status=400)

        res = {
            'post': {
                'id': post.id,
                'title': post.name,
                'image': post.img_url,
                'subtext': post.subtext or '',
                'likes': post.likes,
                'url': post.url,
                'can_load_iframe': post.can_load_iframe,
                'comment_count': post.comment_count,
                'comments': [
                    self._get_comments(cmt, user_field) for cmt in post.comment_ids
                        .filtered(lambda c: user_field not in c.user_id.user_fields_id.blocked_user_field_ids)
                ],
                'user': {
                    'id': post.user_id.id,
                    'name': post.user_id.name,
                    'image': '/user_image/%s' % post.user_id.id
                } if post.user_id else None,
                'liked': user_field in post.liked_user_field_ids
            }
        }

        track(request.env.user, 'Post discussion view', {'post_id': post_id})

        return Response(json.dumps(res), content_type='application/json', status=200)

    @http.route(['/comment/like/<int:comment_id>'], type='http', auth="user", website=True, cors='*')
    def comment_like(self, comment_id, **kw):
        comment = request.env['post.comment'].sudo().browse(comment_id)
        comment.like()

        track(request.env.user, 'Comment like')

        return Response('ok', content_type='application/json', status=200)
