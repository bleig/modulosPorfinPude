# -*- coding: utf-8 -*-
{
    'name': "airac_move_commitment_date",

    'summary': """
        Este campo es para definir la fecha de entrega de la Orden de Trabajo en Manufactura para el pedido en cuestion..""",

    'description': """
        Ventas 00
    """,

    'author': "gabriel ble",
    'website': "http://www.arrowg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_form.xml',
        'report_saleorder.xml'
    ],
    'installable': True,
    'auto_installable': True,
}
