from odoo import models, fields

class Bodega(models.Model):
    _name = 'bodega'
    _description = 'Bodega'


    nombre = fields.Char(string='Nombre', required=True)
    idIentificacion = fields.Char(string='Id Identificacion', required=True)
    calle = fields.Char(string='Calle', required=True)
    numeroInt = fields.Char(string='Numero interior', required=True)
    numeroExt = fields.Char(string='Numero exterior', required=True)
    colonia = fields.Char(string='Colonia', required=True)
    ciudad = fields.Char(string='Ciudad', required=True)
    estado = fields.Char(string='Estado', required=True)
    codigoPostal = fields.Char(string='Codigo Postal', required=True)