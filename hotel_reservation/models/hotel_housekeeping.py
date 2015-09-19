from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.exceptions import except_orm, ValidationError
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api, _
import datetime
import time

class rr_housekeeping(models.Model): 
# extend for housekeeping
    
    @api.onchange('requested_by_partner')
    def onchange_partner_id(self):
        '''
        When Customer name is changed respective adress will display
        in Adress field
        @param self: object pointer
        '''
        if not self.requested_by_partner:
            self.partner_address_id = False
        else:
            addr = self.requested_by_partner.address_get(['default'])
            self.partner_address_id = addr['default']
            
    @api.onchange('folio_id')
    def get_folio_id(self):
        '''
        When you change folio_id, based on that it will update
        the requested_by_partner and room_no as well
        ---------------------------------------------------------
        @param self: object pointer
        '''
        for rec in self:
            self.requested_by_partner = False
            self.room_no = False
            if rec.folio_id:
                self.requested_by_partner = rec.folio_id.partner_id.id
                self.room_no = rec.folio_id.room_lines[0].product_id.id
                
    @api.multi
    def confirm_request(self, cr, uid, ids, context=None):
        p=self.pool.get('res.users').browse(cr, uid, uid)
        print "--------------------------",p.id
        self.write(cr, uid, ids, {
            'approved_by':p.name,
            'state':'confirmed'
        })
        return True
    
    _name = "rr.housekeeping"
    _description = "test"
    
    name = fields.Char('Req No',size=30,readonly=True, states={'draft' : [('readonly',False)]})
    date = fields.Datetime('Date Ordered', required=True,readonly=True,
                        states={'draft' : [('readonly',False)]}, 
                        default=(lambda *a:
                        time.strftime
                        (DEFAULT_SERVER_DATETIME_FORMAT)))
    activity =  fields.Selection([('repair','Repair'),('replaced','Replace')], 'Activity', select=True, required=True,readonly=True,states={'draft' : [('readonly',False)]})
    requested_by = fields.Many2one('res.users','Requested By',readonly=True,states={'draft' : [('readonly',False)]})
    requested_by_partner = fields.Many2one('res.partner','Guest Name',readonly=True,states={'draft' : [('readonly',False)]})
    partner_address_id = fields.Many2one('res.partner', string='Address')
    source = fields.Selection([('intern','Internal Observation'),
                               ('guest','Guest')], 'Source',
                               required=True,readonly=True,
                               states={'draft' : [('readonly',False)]},
                               default=lambda *a: 'intern')
    assign_to = fields.Selection([('intern','Internal'),
                                  ('third_party','Third Party')], 
                                 'Assign Method',required=True,readonly=True,
                                 states={'draft' : [('readonly',False)]
                                 ,'confirmed' : [('readonly',False)]},
                                 default=lambda *a: 'intern')
#    assign_to = fields.Selection([('intern','Internal'),('third_party','Third Party')], 'Assign Method')
    assigned_third_party = fields.Many2one('res.partner','Assigned To',readonly=True,states={'draft' : [('readonly',False)],'confirmed' : [('readonly',False)]})
    assigned_internal = fields.Many2one('res.users','Assigned To',readonly=True,states={'draft' : [('readonly',False)],'confirmed' : [('readonly',False)]})
#    room_no = fields.Many2one('hotel.room','Room No',size=64)
    room_no = fields.Many2one('product.product','Room No',size=64)
    room_no_int = fields.Many2one('hotel.room','Room No',size=64)
    approved_by = fields.Char('Approved By',size=20,)
    rr_line_ids = fields.One2many('rr.housekeeping.line','rr_line_id','Repair / Replacement Info',required=True,readonly=True,states={'draft' : [('readonly',False)],'confirmed' : [('readonly',False)]})
    state =  fields.Selection([('draft','Draft'),
                               ('confirmed','Confirmed'),
                               ('assign','Assigned'),
                               ('done','Done'),
                               ('cancel','Cancel')], 
                               'State', readonly=True,select=True,
                               default=lambda *a: 'draft')
    complaint = fields.Char('Complaint',size=250,readonly=True,states={'draft' : [('readonly',False)]})
    warehouse_id = fields.Many2one('stock.warehouse', 'Shop', required=True, readonly=True, states={'draft' : [('readonly',False)]})     
#    company_id =  fields.Related('warehouse_id','company_id',type='many2one',relation='res.company',string='Company',store=True)    
    company_id = fields.Many2one(string='Company', related='warehouse_id.company_id', relation='res.company')
    folio_id = fields.Many2one('hotel.folio', 'Folio Number')
    
    
class rr_housekeeping_line(models.Model):    
    _name = "rr.housekeeping.line"
    
    rr_line_id=fields.Many2one('rr.housekeeping','Housekeeping line id')
    product_id=fields.Many2one('product.product','Product',required=True)
    product_line_ids=fields.One2many('product.product.line','product_line_id','RICH----------')                
    qty=fields.Float('Qty',size=10)
    uom=fields.Many2one('product.uom','UOM')
    source_locatiion=fields.Many2one('stock.location','Source Loaction')
    dest_locatiion=fields.Many2one('stock.location','Destination Loaction')
    info_id=fields.Many2one('issue.material.details','Matarial Id')
    
class product_product_line(models.Model):
    """Product of product"""
    _name = "product.product.line"
    
    product_line_id = fields.Many2one('rr.housekeeping.line','Product line id')
    product_product_id = fields.Many2one('product.product','Product',required=True)
    qty = fields.Float('Qty',size=10)
    uom = fields.Many2one('product.uom','UOM')
    
class issue_material_details(models.Model):    
    _name = "issue.material.details"
    _description = "Issue Material Details"

    name = fields.Char('Issue Slip',size=20)
    request_id = fields.Many2one('rr.housekeeping','Request Number',required=True,readonly=True,states={'draft':[('readonly',False)]})
    repair_ids = fields.One2many('rr.housekeeping.line','info_id','Product Replacement info',readonly=True,states={'draft':[('readonly',False)]})
    complaint = fields.Char('Complaint',size=250,readonly=True,states={'draft':[('readonly',False)]})
    warehouse_id = fields.Many2one('stock.warehouse', 'Shop', required=True,readonly=True,states={'draft':[('readonly',False)]})   
#    company_id = fields.Related('shop_id','company_id',type='many2one',relation='res.company',string='Company',store=True), 
    company_id = fields.Many2one(string='Company', related='warehouse_id.company_id', relation='res.company') 
    state = fields.Selection([('draft','Draft'),
                              ('confirm','Confirm'),
                              ('done','Done')], 
                             'State', readonly=True,select=True, default=lambda *a: 'draft')          