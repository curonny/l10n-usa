# -*- coding: utf-8 -*-
# Copyright 2017 Ursa Information Systems <http://www.ursainfosystems.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'US Check Printing with Payee Address',
    'summary': 'Print US Checks',
    'version': '10.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'Ursa Information Systems, Odoo Community Association (OCA)',
    'category': 'Localization/Checks Printing',
    'maintainer': 'Ursa Information Systems',
    'website': 'http://www.ursainfosystems.com',
    'depends': [
        'l10n_us_check_printing',
    ],
    'data': [
        'report/print_check.xml',
    ],
    'installable': True,
}