from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'),
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['unidad_negocio'] = self.unidad_negocio
        return invoice_vals

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.origin:
                quote = self.env['sale.order'].search([('name', '=', order.origin)], limit=1)
                if quote:
                    order.unidad_negocio = quote.unidad_negocio
        return res

class AccountMove(models.Model):
    _inherit = 'account.move'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'),
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'), 
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')

    def _prepare_invoice(self):
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals['unidad_negocio'] = self.unidad_negocio
        return invoice_vals

class Project(models.Model):
    _inherit = 'project.project'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'),
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'),
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    sueldo_nominal = fields.Float(string='Sueldo Nominal')
    sueldo_maquila = fields.Float(string='Sueldo Maquila')
    fecha_entrada = fields.Date(string='Fecha Entrada')
    horas_semanales = fields.Float(string='Horas Semanales')

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    unidad_negocio = fields.Selection([
        ('bioseguridad', 'Bioseguridad'),
        ('mantenimiento', 'Mantenimiento'),
        ('taller', 'Taller'),
        ('mineral', 'Mineral')
    ], string='Unidad de Negocio')
