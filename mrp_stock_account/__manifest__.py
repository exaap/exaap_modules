# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#

{
    'name': 'MRP Stock',
    'category': 'Manufacturing',
    'version': '11.0.0.0.1',
    'author':
    'Joan Marín Github@joanodoo, Guillermo Montoya Github@guillermm, Alejandro Olano Github@alejo-code',
    'website': 'http://www.exaap.com',
    'license': 'AGPL-3',
    'summary': 'Functionalities for MRP - Odoo version 11',
    'depends': ['mrp', 'stock_account'],
    'data': [
        'views/mrp_production.xml',
    ],
    'installable': True,
}