from openerp import models, fields, api


class hotel_reservation_wizard(models.TransientModel):

    _name = 'hotel.reservation.wizard'

    date_start = fields.Datetime('Start Date', required=True)
    date_end = fields.Datetime('End Date', required=True)

    @api.multi
    def report_reservation_detail(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.reservation',
            'form': self.read(['date_start', 'date_end'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_reservation.report_roomres_qweb',
                                     data=data)

    @api.multi
    def report_checkin_detail(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.reservation',
            'form': self.read(['date_start', 'date_end'])[0],
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_reservation.report_checkin_qweb',
                                     data=data)

    @api.multi
    def report_checkout_detail(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.reservation',
            'form': self.read(['date_start', 'date_end'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_reservation.report_checkout_qweb',
                                     data=data)

    @api.multi
    def report_maxroom_detail(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.reservation',
            'form': self.read(['date_start', 'date_end'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_reservation.report_maxroom_qweb',
                                     data=data)


class make_folio_wizard(models.TransientModel):

    _name = 'wizard.make.folio'

    grouped = fields.Boolean('Group the Folios')

    @api.multi
    def makeFolios(self):
        order_obj = self.env['hotel.reservation']
        newinv = []
        for order in order_obj.browse(self._context['active_ids']):
            for folio in order.folio_id:
                newinv.append(folio.id)
        return {
            'domain': "[('id','in', [" + ','.join(map(str, newinv)) + "])]",
            'name': 'Folios',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hotel.folio',
            'view_id': False,
            'type': 'ir.actions.act_window'
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
