{
    'name': 'Bodega',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Modulo para registro de bodegas',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/bodega_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_module_bodega/static/src/css/bodega.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
}
