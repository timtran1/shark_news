# -*- coding: utf-8 -*-

{
    'depends': [
        'base',
        'website',
        'token_authentication'
    ],
    'data': [
        'data/res_users.xml',
        'data/res_config_settings.xml',
        'data/ir_cron.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'author': 'Trung Tran',
    'sequence': 0,
    'name': 'SharkNews',
    'summary': 'SharkNews ',
    'description':
        """
SharkNews
    """,
}
