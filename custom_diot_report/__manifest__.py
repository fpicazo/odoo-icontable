{
    'name': 'Custom DIOT Report',
    'version': '1.0',
    'summary': 'Add custom column to DIOT report',
    'depends': ['base', 'l10n_mx_reports'],
    'data': [
        'views/res_partner_bank_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}