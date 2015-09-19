{
    "name": "Hotel POS Restaurant Management",
    "version": "0.10",
    "author": "Riza Kurniawan and Team",
    "category": "Generic Modules/Hotel Restaurant Management",
    "website": "rizaontheblog.blogspot.com",
    "depends": ["pos_restaurant", "hotel"],
    "demo": ["views/hotel_pos_data.xml"],
    "data": ["security/ir.model.access.csv",
             "views/pos_restaurent_view.xml",
             "views/hotel_pos_report.xml",
             "views/report_pos_management.xml",
             "wizard/hotel_pos_wizard.xml"],
    "description": """
    Module for POS management.
     """,
    "auto_install": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
