{
    'name': "Pos Kitchen Screen",
    'version': "17.0.0.1",
    'category': "Tools",
    'summary': """
        Point of sale Kitchen Screen | Pos Restaurant Screen | POS Bar Screen | POS Kitchen Screen
        | Point of sale bar screen | Odoo Kitchen Display | POS Kitchen display system | Point of sale restaurant screen 
        | vista de cocina en punto de venta | cocina en POS
    """,
    'author': "Javier Fernández",
    'website': "https://asdelmarketing.com",
    'license': 'OPL-1',
    'price': 37.99,
    'currency': 'EUR',
    'data': [
        'views/kitchen_menu_view.xml',
        'views/product_views.xml',
        'views/user_views.xml',
        'views/res_config_settings_views.xml',
        'views/pos_config_view.xml',
    ],
    'demo': [],
    'images': [
        'static/description/thumbnail.gif',
    ],
    'depends': [
        'web',
        'point_of_sale',
        'pos_restaurant'
    ],
    "assets": {
        "web.assets_backend": [
            "adm_pos_kitchen_screen/static/src/js/kitchen.js",
            "adm_pos_kitchen_screen/static/src/js/kitchen-orders.js",
            "adm_pos_kitchen_screen/static/src/css/custom.css",
            "adm_pos_kitchen_screen/static/src/xml/kitchen.xml",
        ],
        'point_of_sale._assets_pos': [
            'adm_pos_kitchen_screen/static/src/js/order_to_kitchen/order_to_kitchen_button.js',
            'adm_pos_kitchen_screen/static/src/js/order_to_kitchen/order_to_kitchen_button.xml',
        ],
    },
    'post_init_hook': 'setup_default_kitchen_config',
    'installable': True,
}