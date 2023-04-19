# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).

{
    "name": "Purchase latest shipment date Notify",
    "version": "14.0.1.0.0",
    "category": "Purchase Management",
    "author": "mesi2640@gmail.com",
    "website": "",
    "license": "AGPL-3",
    "depends": ["web", "bus", "base","purchase_stock"],
    
     'data': [
        'data/ir_cron_data.xml',
        'views/main.xml',
        'views/web_notify.xml'
        
    ],
    'demo': ['views/res_users_demo.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
