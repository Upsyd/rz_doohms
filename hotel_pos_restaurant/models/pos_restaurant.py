from openerp import models, fields, api


class hotel_folio(models.Model):

    _inherit = 'hotel.folio'
    _order = 'folio_pos_order_ids desc'

    folio_pos_order_ids = fields.Many2many('pos.order', 'hotel_pos_rel',
                                           'hotel_folio_id', 'pos_id',
                                           'Orders', readonly=True)


class pos_order(models.Model):

    _inherit = "pos.order"

    folio_id = fields.Many2one('hotel.folio', 'Folio Number')
    room_no = fields.Char('Room Number')

    @api.onchange('folio_id')
    def get_folio_partner_id(self):
        '''
        When you change folio_id, based on that it will update
        the guest_name and room_no as well
        ---------------------------------------------------------
        @param self: object pointer
        '''
        for rec in self:
            self.partner_id = False
            self.room_no = False
            if rec.folio_id:
                self.partner_id = rec.folio_id.partner_id.id
                self.room_no = rec.folio_id.room_lines[0].product_id.name

    @api.multi
    def action_paid(self):
        '''
        When pos order created this method called,and sale order line
        created for current folio
        --------------------------------------------------------------
        @param self: object pointer
        '''
        hotel_folio_obj = self.env['hotel.folio']
        hsl_obj = self.env['hotel.service.line']
        so_line_obj = self.env['sale.order.line']
        for order_obj in self:
                hotelfolio = order_obj.folio_id.order_id.id
                if order_obj.folio_id:
                    for order1 in order_obj.lines:
                        values = {'order_id': hotelfolio,
                                  'name': order1.product_id.name,
                                  'product_id': order1.product_id.id,
                                  'product_uom_qty': order1.qty,
                                  'price_unit': order1.price_unit,
                                  'price_subtotal': order1.price_subtotal,
                                  }
                        sol_rec = so_line_obj.create(values)
                        hsl_obj.create({'folio_id': order_obj.folio_id.id,
                                        'service_line_id': sol_rec.id})
                        hf_rec = hotel_folio_obj.browse(order_obj.folio_id.id)
                        hf_rec.write({'folio_pos_order_ids':
                                      [(4, order_obj.id)]})
        return super(pos_order, self).action_paid()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
