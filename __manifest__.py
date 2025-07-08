{
    'name': 'Gestión de Recargas TAE',
    'version': '1.0',
    'summary': 'Gestión de recargas para TAE',
    'description': '''
        Módulo para gestionar recargas realizadas en ventas y POS
        cuando se usa lista de precios TAE
    ''',
    'author': 'Tu Nombre',
    'depends': ['sale', 'point_of_sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/recarga_views.xml',
        'views/pos_order_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
