from odoo import models, fields

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    credit_allowed_days = fields.Integer(string='Credit Allowed Days')
