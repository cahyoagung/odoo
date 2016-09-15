# -*- coding: utf-8 -*-
{
    'name': "State Area",
    'summary': """Add new field State Area""",
    'description': """
        Add new field State Area in Master Customer and Master State
    """,
    'author': "Cahyo",
    'website': "http://www.housecode.net",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['sale','base'],
    'installable':True,
    'application': True,
    'data':[
        'views/state_area_view.xml',
        'views/add_state_area_view.xml',
        'views/res_partner_state_area_view.xml'
    ],
}
