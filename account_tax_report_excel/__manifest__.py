# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Account Tax Report - Excel',
    'images': ['static/description/ptre.jpg'],
    'depends' : ['account_tax_report'],
    'version' : '6.1.1',
    'price': 79.0,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'category' : 'Accounting/Accounting',
    'license': 'Other proprietary',
    'currency': 'EUR',
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/account_tax_report_excel/277',#'https://youtu.be/jeab2AQf5xM',#'https://youtu.be/r7ywBCf6INo',
    'summary': 'Account Tax Report Odoo 9- Excel',
    'description' : """
          This module adds the account tax report in Excel.
Print Tax   
Print Tax Report
Odoo 9 Tax 
Odoo 9 Tax report
Chart of Taxes
Tax report
Excel report
Excel account tax
Excel tax odoo 9
Tax excel report.
tax report excel
tax in excel
print tax report in excel
    """,
    'website': 'https://www.probuse.com',
    'data': [
        'security/ir.model.access.csv',
        'views/output_xls_report.xml',
         'wizard/tax_wizard_view.xml',
#              'security/ir.model.access.csv' #no need to give acl to transient model
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: