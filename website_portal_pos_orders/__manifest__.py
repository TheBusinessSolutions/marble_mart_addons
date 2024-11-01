# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Customer Portal - Point of Sale Orders",
    'price': 59.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """Allow customers to login in My Account on website and view Point of Sale Orders and Print receipts.""",
    'description': """
Website Customer Portal Show Point of Sale Orders
This module show Point of Sale Orders on My Account.
Allow customer to login in My Account and view Point of Sale Orders and Print Receipts.
Print Point of Sale Orders
Print Receipt on Portal
customer portal pos orders
Customer Portal - Point of Sale Orders
customer portal receipts
customer view portal
Allow customers to login in My Account on website and view Point of Sale Orders and Print receipts.
portal customer 
portal
my account page
my account login
my account portal page
my account customer payment
customer print receipts
Website Customer Portal Show Point of Sale Orders
Point of Sale Orders Show to Customer - My Account
Customer - Print Receipts from My Account



Allow customers to login in My Account / Portal on website and view Point of Sale Orders and Print/Download POS Order receipts.

Login Customer into My Account - Portal

Allow your customers to see own Point of Sale Orders and print Receipts.

    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/image.jpg'],
    'version': '8.7',
    'category' : 'Website/Website',
    'depends': [
#         'website_portal_sale',
        'point_of_sale',
        'sale',
        'portal',
#         'pos_order_report' #odoo13
    ],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/website_portal_pos_orders/697',#'https://youtu.be/iILc27kECaw',
    'data':[
            'security/ir.model.access.csv',
            'security/portal_pos_orders_security.xml',
            'views/report_reg.xml',
            'views/report_pos_order.xml',
            'views/website_portal_sale.xml'
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
