{
    'name': 'Limpieza Camiones',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Modulo para limpiezada de camiones',
    'depends': ['hr','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/truck_cleaning_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_new_module_form/static/src/css/truck_cleaning.css',
            'custom_new_module_form/static/src/js/*.js',
            'custom_new_module_form/static/src/views/*.xml',
        ],
    },
    'images': ['static/description/icon.png'],
}