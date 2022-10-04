from mixpanel import Mixpanel
import os
import logging
from odoo.http import request
import requests as r
import json

mp = Mixpanel(os.environ.get('MIXPANEL_PROJECT_TOKEN'))
_logger = logging.getLogger(__name__)


def track(user, event, props=None):
    if  request.httprequest.environ.get('HTTP_CF_CONNECTING_IP', False): # prod only
        log = {
            'last_ip': request.httprequest.environ['HTTP_CF_CONNECTING_IP'],
            'country': request.httprequest.environ['HTTP_CF_IPCOUNTRY'],
            'last_agent': request.httprequest.environ['HTTP_USER_AGENT'],
        }

        try:
            res = r.get('https://ipinfo.io/%s/json' % request.httprequest.environ['HTTP_CF_CONNECTING_IP'])
            data = json.loads(res.text)
            log.update({
                'loc': data.get('loc'),
                'org': data.get('org'),
                'city': data.get('city'),
            })
        except:
            _logger.exception('Geolocation query failed.')

        user.user_fields_id.write(log)

        org = log.get('org', '')
        if user.login not in [
            'trung8358573@gmail.com',
            'trung83585715@gmail.com',
            'tim.tran@deepsel.com',
            'timtran303@outlook.com'
        ] and 'Apple Inc.' not in org and 'Facebook, Inc.' not in org and 'Google LLC' not in org:
            _logger.info('TRACK ' + event)
            _logger.info(user.login)
            if props:
                props.update({'ip': log['last_ip']})
                mp.track(user.id, event, props)
            else:
                mp.track(user.id, event, {'ip': log['last_ip']})
