{
    "name": "Restaurant Management - Reporting",
    "version": "0.03",
    "author": "Riza and Team",
    "website": "rizaontheblog.blogspot.com",
    "depends": ["hotel_restaurant", "report_hotel_reservation"],
    "category": "Generic Modules/Hotel Restaurant",
    "data": [
        "security/ir.model.access.csv",
        "views/report_hotel_restaurant_view.xml",
    ],
    "description": """
    Module shows the status of restaurant reservation
     * Current status of reserved tables
     * List status of tables as draft or done state
    """,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
