from odoo import models, fields

class TruckCleaning(models.Model):
    _name = 'bomba'
    _description = 'Bomba'

    driver_id = fields.Many2one('hr.employee', string='Chofer', required=True)
    service_type = fields.Selection([
        ('wash', 'Normal'),
        ('deep_clean', 'Biogel'),
        ('sanitize', 'Sanitizar')
    ], string='Tipo de Servicio', required=True)
    result = fields.Selection([
        ('ok', 'OK'),
        ('cancel', 'Cancelar')
    ], string='Resultado', required=True)
    truck_id = fields.Char(string='Numero de Jaula', required=True)
    picture_before = fields.Binary(string='Foto Antes')
    picture_after = fields.Binary(string='Foto Despues')
