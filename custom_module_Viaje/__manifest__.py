# custom_facturacion/__manifest__.py
{
    'name': 'Viajes',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Modulo para Control de Viajes',
    'depends': ['hr', 'maintenance', 'custom_module_bodega'],
    'data': [
        'security/ir.model.access.csv',
        'views/viajes_view.xml',
        'views/viajes_report_template.xml',
        'views/viajes_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_module_Viaje/static/src/css/viajes.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
}
