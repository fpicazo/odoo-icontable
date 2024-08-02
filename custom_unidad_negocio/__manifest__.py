{
    'name': 'Unidad de negocio Module',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Agregar custom fields a los modelos',
    'depends': ['crm','sale', 'purchase', 'account', 'hr', 'project', 'hr_expense'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/purchase_order_view.xml',
        'views/hr_employee_view.xml',
        'views/project_view.xml',
        'views/expense_view.xml',
        'views/crm_view.xml',
    ],
}
