
{
    "name": "Hotel Housekeeping Management",
    "version": "0.05",
    "author": "Riza Kurniawan and Team",
    "category": "Generic Modules/Hotel Housekeeping",
    "website": "rizaontheblog.blogspot.com",
    "depends": ["hotel"],
    "demo": [
        "views/hotel_housekeeping_data.xml",
    ],
    "data": [
        "security/ir.model.access.csv",
        "report/hotel_housekeeping_report.xml",
        "views/activity_detail.xml",
        "wizard/hotel_housekeeping_wizard.xml",
        "views/hotel_housekeeping_workflow.xml",
        "views/hotel_housekeeping_view.xml",
    ],
    "description": """
    Module for Hotel/Hotel Housekeeping. You can manage:
    * Housekeeping process
    * Housekeeping history room wise

      Different reports are also provided, mainly for hotel statistics.
    """,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
