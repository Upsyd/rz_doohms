from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp import models, fields, api, _, netsvc
from openerp.exceptions import ValidationError
import time

class LaundryManagement(models.Model):
    _name = 'laundry.mangement'
    _description = 'Laundry Management'
    
    name = fields.Char(size=24, string="Order Reference")
    company_id = fields.Many2one('res.company','Company')
    date_order = fields.Datetime('Request Date')
    deadline_date = fields.Datetime('Request Deadline')
#    invoice_ids = fields.Many2many
    is_chargable = fields.Boolean('Chargable')
#    laundry_service_product_ids = fields.One2many
    partner_id = fields.Many2one('res.partner','Guest Name')
#    pricelist_id = fields.Many2one('')
    request_type = fields.Selection([('internal','Internal'),
                                     ('fromroom','From Room'),],'Request Type')
    room_number = fields.Many2one('hotel.room','Room No.')
    service_type = fields.Selection([('intern','Internal'),
                                     ('third','Third Party'),],'Service Type')
    shop_id = fields.Many2one('stock.warehouse','Shop')
    state = fields.Selection([('draft','Draft'),
                              ('confirmed','Confirmed'),
                              ('sent_to_laundry','Sent to Laundry'),
                              ('laundry_returned','Laundry Returned'),
                              ('customer_returned','Customer Returned'),
                              ('done','Done'),],'State')
    supplier_id = fields.Many2one('res.partner','Supplier')
#    supplier_id_temp = fields.
    user_id = fields.Many2one('res.user','Responsible')
    
class HotelLaundry(models.Model):
    _name = 'hotel.laundry'
    _description = 'Hotel Laundry'
    
    laundry_service_ids = fields.One2many('hotel.laundry.services','hotel_laundry_service_id', 'Laundry Service')
    name = fields.Char('Name')
    partner_id = fields.Many2one('res.partner','Supplier Name')
    state = fields.Selection([('draft','Draft'),
                              ('confirmed','Confirmed')],'Selection')
    
class LaundryService(models.Model):
    _name = 'hotel.laundry.services'
    _description = 'Hotel Laundry Service'
    
    name = fields.Char('Name')
    category_id = fields.Integer('Category')
    hotel_laundry_service_id = fields.Many2one('hotel.laundry')
    laundry_services_id = fields.Many2one('product.product','Service Name')
    laundry_services_items_ids = fields.One2many('hotel.laundry.services.items','laundry_items_id','Laundry Service Item')
    supplier_id = fields.Integer('Supplier ID')
    
class LaundryServiceItem(models.Model):
    _name = 'hotel.laundry.services.items'
    _description = 'Laundry services Items Details'
    
    category_id1 = fields.Integer('Category')
    cost_price = fields.Float('Cost Price')
    item_id = fields.Many2one('product.product','Items')
    laundry_items_id = fields.Many2one('hotel.laundry.services')
    name = fields.Char('Name')
    sale_price = fields.Float('Sale Price')
    

    
class LaundryServiceProductLine(models.Model):
    _name = 'laundry.service.product.line'
    _description = 'laundry.service.product.line'
    
    cost_price = fields.Float('Cost Price')
    cost_subtotal = fields.Float('Cost Sub Total')
    item_id = fields.Many2one(' product.product ','Item')
    item_id_ref = fields.Many2one('hotel.laundry.services.items','Items')
    laundry_service_line_id = fields.Many2one('laundry.service.product','Service Line ID')
    qty = fields.Float('Quantity')
    qty_uom = fields.Many2one('product.uom','UoM')
    sales_price = fields.Float('Sales Price')
    sale_subtotal = fields.Float('Sale Sub Total')
    
    
class LaundryServiceProduct(models.Model):
    _name = 'laundry.service.product'
    _description = 'Laundry Service Product'
    
    cost_rate = fields.Float('Cost Rate')
    cost_subtotal = fields.Float('Cost Sub Total')
    laundry_service_id = fields.Many2one('laundry.management')
#  CHECK  laundry_service_product_line_ids = fields.One2many(' laundry.service.product.line ',' laundry_service_line_id ','Laundry Product Service Line')
    laundry_services_id = fields.Many2one('hotel.laundry.services','Service Name')
    pricelist_id = fields.Many2one(' product.pricelist ','Price List')
    sales_rate = fields.Float('Sales Rate')
    sale_subtotal = fields.Float('Sales Sub Total')
    supplier_id = fields.Many2one('res.partner','Supplier')    
    
    
    
class HotelFolioLaundryLine(models.Model):
    _name = 'hotel_folio_laundry.line'
    _description = 'Hotel Folio Laundry Line'
    
    folio_id = fields.Many2one('hotel.folio','Folio Ref.')
    laundry_line_id = fields.Many2one('sale.order.line','laundry Ref.')
    source_origin = fields.Char('Source Origin')
    
class ReturnPicking(models.Model):
    _name = 'hotel.laundry.picking'
    _description = 'Return Picking'
    
    invoice_state = fields.Selection([('draft','Draft'),
                                      ('confirm','Confirm')],'Invoicing')
# CHECK-->Moves    product_return_moves = fields.One2many(' hotel.laundry.picking.memory ','Moves')
    
class HotelLaundryPickingMemory(models.Model):
    _name = 'hotel.laundry.picking.memory'
    _description = 'Hotel laundry Picking Memory'
    
    move_id = fields.Many2one('stock.move', 'Move')
    product_id = fields.Many2one('product.product','Product')
    quantity = fields.Float('Quantity')
    wizard_id = fields.Many2one(' hotel.laundry.picking ','Wizard')
    