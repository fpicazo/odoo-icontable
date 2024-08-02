import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class TruckCleaning(models.Model):
    _name = 'truck.cleaning'
    _description = 'Truck Cleaning'

    driver = fields.Char(string='Chofer', required=True)
    service_type = fields.Selection([
        ('wash', 'Normal'),
        ('deep_clean', 'Biogel'),
        ('sanitize', 'Sanatizar')
    ], string='Tipo de Servicio', required=True) 
    result = fields.Selection([
        ('ok', 'OK'),
        ('cancel', 'Cancelar')
    ], string='Resultado', required=True)
    truck_id = fields.Char(string='Numero de Jaula', required=True)
    picture_before = fields.Binary(string='Foto Antes')
    picture_after = fields.Binary(string='Foto Despues')
    signature = fields.Binary(string='Firma del Conductor')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('invoiced', 'Facturado')
    ], string='Estado', default='draft')

    def action_create_quote(self):
        self.get_viajes_and_create_quote()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def get_viajes_and_create_quote(self):
        _logger.info('Starting get_viajes_and_create_quote method')
        service_counts = self.read_group(
            [('state', '!=', 'invoiced')],
            ['service_type'],
            ['service_type']
        )
        _logger.info('Service counts: %s', service_counts)

        if not service_counts:
            _logger.warning('No service counts found')
            return

        order_lines = []
        for service in service_counts:
            service_type = service['service_type']
            service_qty = service['service_type_count']
            _logger.info('Processing service type: %s with quantity: %s', service_type, service_qty)

            product_id = self.env['product.product'].search([('default_code', '=', service_type)], limit=1)
            if not product_id:
                _logger.warning('No product found for service type: %s', service_type)
                continue

            _logger.info('Product found: %s for service type: %s', product_id.name, service_type)
            order_lines.append((0, 0, {
                'product_id': product_id.id,
                'product_uom_qty': service_qty,
            }))

        _logger.info('Order lines: %s', order_lines)
        if order_lines:
            sale_order = self.env['sale.order'].create({
                'partner_id': self.env.user.partner_id.id,  # or a specific customer id
                'order_line': order_lines
            })
            _logger.info('Sale order created with order lines: %s', order_lines)

            # Update the state of the processed records to 'invoiced'
            cleaning_records = self.search([('state', '!=', 'invoiced')])
            cleaning_records.write({'state': 'invoiced'})
            _logger.info('State updated to invoiced for records: %s', cleaning_records.ids)
        else:
            _logger.warning('No order lines to create sale order')
