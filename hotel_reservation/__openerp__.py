{
    "name": "Hotel Reservation Management",
    "version": "0.07",
    "author": "Riza Kurniawan and Team",
    "category": "Generic Modules/Hotel Reservation",
    "website": "rizaontheblog.blogspot.com",
    "depends": ["hotel", "stock", 'mail', "hotel_report_layout",
                'email_template'],
    "demo": [
        "views/hotel_reservation_data.xml",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/hotel_reservation_wizard.xml",
        "report/hotel_reservation_report.xml",
        "views/hotel_reservation_sequence.xml",
        "views/hotel_reservation_workflow.xml",
        "views/hotel_reservation_view.xml",
        "views/hotel_scheduler.xml",
        "views/report_checkin.xml",
        "views/report_checkout.xml",
        "views/max_room.xml",
        "views/room_res.xml",
        "views/room_summ_view.xml",
        "views/email_temp_view.xml",
    ],
    "description": """
    Module for Hotel/Resort/Property management. You can manage:
    * Guest Reservation
    * Group Reservartion
      Different reports are also provided, mainly for hotel statistics.
    """,
    'js': ["static/src/js/hotel_room_summary.js", ],
    'qweb': ['static/src/xml/hotel_room_summary.xml'],
    'css': ["static/src/css/room_summary.css"],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
