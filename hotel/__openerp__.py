{
    "name": "Hotel Management",
    "version": "0.10",
    "author": "Riza Kurniawan and Team",
    "category": "Generic Modules/Hotel Management",
    "website": "http://rizaontheblog.blogspot.com",
    "depends": ["sale_stock", "point_of_sale", "hotel_report_layout"],
    "demo": ["views/hotel_data.xml"],
    "data": [
        "security/hotel_security.xml",
        "security/ir.model.access.csv",
        "views/hotel_sequence.xml",
        "views/hotel_folio_workflow.xml",
        "views/hotel_report.xml",
        "views/report_hotel_management.xml",
        "views/hotel_view.xml",
        "wizard/hotel_wizard.xml",
    ],
    "description": """
    Module for Hotel/Resort/Property management. You can manage:
    * Configure Property
    * Hotel Configuration
    * Check In, Check out
    * Manage Folio
    * Payment

    Different reports are also provided, mainly for hotel statistics.
    """,
    'css': ["static/src/css/room_kanban.css"],
    "auto_install": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
