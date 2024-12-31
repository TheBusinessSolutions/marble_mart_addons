{
    'name': 'Purchase Price Visibility',
    'version': '1.0',
    'category': 'Purchase',
    'summary': 'Show and Restrict Price Editing in PO Receive Screen',
    'description': 'Allows price visibility in receive screen with editing restrictions',
    'author': 'Your Company',
    'depends': ['purchase_stock', 'stock'],
    'data': [
        'views/stock_picking_views.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}