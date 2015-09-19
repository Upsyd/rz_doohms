{
    "name": "Hotel Restaurant Management",
    "version": "3.0",
    "author": "Riza Kurniawan",
    "category": "Generic Modules/Hotel Restaurant",
    "website": "http://rizaontheblog.blogspot.com",
    "depends": ["hotel", "hotel_report_layout"],
    "demo": [
        "views/hotel_restaurant_data.xml",
    ],
    "data": [
        "security/ir.model.access.csv",
        "report/hotel_restaurant_report.xml",
        "wizard/hotel_restaurant_wizard.xml",
        "views/res_table.xml",
        "views/kot.xml",
        "views/bill.xml",
        "views/folio_order_report.xml",
        "views/hotel_restaurant_workflow.xml",
        "views/hotel_restaurant_sequence.xml",
        "views/hotel_restaurant_view.xml",
    ],
    "description": """
    Module for Hotel/Resort/Restaurant management. You can manage:
    * Configure Property
    * Restaurant Configuration
    * table reservation
    * Generate and process Kitchen Order ticket,
    * Payment

    Different reports are also provided, mainly for Restaurant.
    """,
    "active": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
