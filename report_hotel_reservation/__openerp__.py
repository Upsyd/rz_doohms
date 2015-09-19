{
    "name": "Hotel Reservation Management - Reporting",
    "version": "0.03",
    "author": "Riza and Team",
    "website": "rizaontheblog.blogspot.com",
    "depends": ["hotel_reservation"],
    "category": "Generic Modules/Hotel Reservation",
    "data": [
        "security/ir.model.access.csv",
        "views/report_hotel_reservation_view.xml",
    ],
    "description": """
    Module shows the status of room reservation
     * Current status of reserved room
     * List status of room as draft or done state
    """,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
