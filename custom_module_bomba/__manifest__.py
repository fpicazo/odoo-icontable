{
    'name': 'Bomba',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Modulo para Manejo de bombas',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/bomba_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_module_bomba/static/src/css/bomba.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
}
