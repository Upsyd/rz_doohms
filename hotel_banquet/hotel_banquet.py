from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp import models, fields, api, _, netsvc
from openerp.exceptions import ValidationError
import time

class BanquetQuotation(models.Model):
    _name = 'banquet.quotation'
    _description = 'Banquet Quotation'

    name = fields.Char(size=12,string="Quotation No.")
    address = fields.Char(size=64, string="Address")
    adult = fields.Integer('Adult Persons')
    agent_id = fields.Many2one('res.partner','Agent')
    board_toread = fields.Char(size=64,string="Board to Read")
    checkin_date = fields.Datetime('Prefer Start Date')
    checkout_date = fields.Datetime('Prefer End Date')
    child = fields.Integer('Child')
    company_id = fields.Many2one('res.company','Company')
    contact_name = fields.Char(size=64,string="Contact Name")
    current_date = fields.Date('Enquiry Date')
    deposit_policy = fields.Selection([('dep','Deposit Percentage'),
                                       ('nodep','No Deposit'),],'Deposit Policy')
    email_id = fields.Char(size=64,string="Email")
#    food_items_ids = fields.One2many
    invoiced = fields.Boolean('Invoiced')
    lead = fields.Many2one('crm.lead','Lead')
    min_dep_amount = fields.Float('Minimum Deposit Amount')
    mobile = fields.Char(size=12,string="Mobile Number")
    number_of_days = fields.Integer('Number of Days')
    number_of_rooms = fields.Integer('Number of Rooms')
#    other_items_ids = fields.One2many('other.items','Other Items')
    percentage = fields.Float('Percentage/Deposit Amount')
    pricelist_id = fields.Many2one('product.pricelist','Pricelist')
    pur_tax_amt = fields.Float('Purchase Taxes')
    pur_total_amt = fields.Float('Purchase Total Amount')
    pur_untax_amt = fields.Float('Purchase Untaxed Amount')
#    room_ids = fields.One2many('hotel.reservation.line','banquet_id','Room Details')
    sale_tax_amt = fields.Float('Sale Taxes')
    sale_total_amt = fields.Float('Sale Total Amount')
    sale_untax_amt = fields.Float('Sale Untaxed Amount')
    seating_id = fields.Many2one('seating.plan','Seating Plan')
    shop_id = fields.Many2one('stock.warehouse','Shop')
    state = fields.Selection([('draft','Draft'),
                              ('confirm','Confirm'),
                              ('send_to','Send To'),
                              ('approve','Approve'),
                              ('done','Done'),],'State')
    theme_id = fields.Many2one('theme.plan','Theme Plan')
    via = fields.Selection([('direct','Direct'),
                            ('agent','Agent'),],'Via')
    

class SeatingPlan(models.Model):
    _name = 'seating.plan'
    _description = 'Seating Plan'
    name = fields.Char('Name')
    code = fields.Char('Code')
    
class ThemePlan(models.Model):
    _name = 'theme.plan'
    _description = 'Theme Plan'
    name = fields.Char('Name')
    code = fields.Char('Code')