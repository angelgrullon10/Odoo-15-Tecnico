# -*- coding: utf-8 -*-
{
    'name': "Gestion Taller",

    'summary': """
        Practica curso odoo 15 para gestion de taller
        """,

    'description': """
        Practica curso odoo 15 para gestion de taller
    """,

    'author': "PROSERT",
    'website': "http://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
    ],
}
