from openerp import models, fields, api


class wizard_hotel_restaurant(models.TransientModel):

    _name = 'wizard.hotel.restaurant'

    date_start = fields.Datetime('Start Date', required=True)
    date_end = fields.Datetime('End Date', required=True)

    @api.multi
    def print_report(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.restaurant.reservation',
            'form': self.read(['date_start', 'date_end'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_restaurant.report_res_table',
                                     data=data)

wizard_hotel_restaurant()


class folio_rest_reservation(models.TransientModel):
    _name = 'folio.rest.reservation'
    _rec_name = 'date_start'

    date_start = fields.Datetime('Start Date')
    date_end = fields.Datetime('End Date')
    check = fields.Boolean('With Details')

    @api.multi
    def print_rest_report(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.folio',
            'form': self.read(['date_start', 'date_end', 'check'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_restaurant.report_rest_order',
                                     data=data)

    @api.multi
    def print_reserv_report(self):
        data = {
            'ids': self.ids,
            'model': 'hotel.folio',
            'form': self.read(['date_start', 'date_end', 'check'])[0]
        }
        return self.env['report'
                        ].get_action(self,
                                     'hotel_restaurant.report_reserv_order',
                                     data=data)


folio_rest_reservation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
