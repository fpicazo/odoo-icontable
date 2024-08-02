from odoo import models, fields

class Viajes(models.Model):
    _name = 'viajes'
    _description = 'Viajes'

    comments = fields.Text(string='Comentarios')
    fecha = fields.Date(string='Fecha', required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string='Equipamiento', required=True)
    line_ids = fields.One2many('viajes.line', 'viaje_id', string='Líneas de Viaje')
    chofer_id = fields.Many2one('res.partner', string='Chofer', required=True)

class ViajesLine(models.Model):
    _name = 'viajes.line'
    _description = 'Movimientos'

    viaje_id = fields.Many2one('viajes', string='Viaje', required=True)
    bodega_origin_id = fields.Many2one('bodega', string='Bodega Origen', required=True)
    bodega_dest_id = fields.Many2one('bodega', string='Bodega Destino', required=True)
    km_distance = fields.Float(string='Distancia (km)', required=True)
