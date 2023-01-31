# -*- coding: utf-8 -*-
{
    "name": "cnb_module",
    "version": "1.0",
    "category": "Sale",
    "author": "Mediod Consulting",
    "price": 250.00,
    'currency': "USD",
    'depends': ['base', 'sale'],
    'summary': """
        This module generates a lawyer contract for customers based on the data in customer model and law firm.
        for faucouneau.fr law firm is the only company and data  company from company model.
        New fields are added in customer model and company model to meet the criteria and insert into the customer
        contract.
    """,
    "website": "https://mediodconsulting.com/",
    "data": [
        'report/cnb_paperformat.xml',
        'report/report_action.xml',
        'report/sales_report_inherit.xml',
        'report/custom_internal_layout.xml',
        'views/res_partner_inherit.xml',
        'views/product_template.xml',
    ],
    "auto_install": False,
    "installable": True,
    'license': 'OPL-1',
}