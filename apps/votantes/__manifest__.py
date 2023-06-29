# -*- coding: utf-8 -*-
{
    'name': "Gestion de Votantes",

    'summary': """
        Modulo para la gestion de los votantes o militantes electorales.""",

    'description': """
        Modulo para la gestion de los votantes o militantes electorales.
    """,

    'author': "PROSERT SRL",
    'website': "https://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
