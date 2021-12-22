# -*- coding: utf-8 -*-
{
    'name': 'Payment Reference For POS',
    'summary': """
        add payment reference to pos 
         """,
    'description': """
        Allow to record payment reference/note per payment line inside pos payment screen
    """,
    'author': "Agile Solutions",
    'website': "www.agileitsolution.com",
    'category': 'point of sale',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_ref.xml',
        'views/pos_order_view.xml',
    ],
    'qweb': ['static/src/xml/pos_payment_ref.xml'],
    'images': ['static/description/cover.png'],
    'auto_install': False,
    'installable': True,
    'application': True,
    'price': 35,
    'currency': 'USD',
    'support': 'apps@agileitsolution.com',
}
