# -*- coding: utf-8 -*-
{
    'name': "QA linked to Work Order",
    'summary': """QA linked to Work Order""",
    'description': """
        QA linked to Work Order
    """,
    'author': "Cahyo",
    'website': "http://www.housecode.net",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['quality_assurance','mrp_operations_extension'],
    'installable':True,
    'application': True,
    'data':[
        'views/inherit_wo_view.xml'
    ],
    'auto_install':False,
}
