import json
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class TruckCleaningController(http.Controller):

    @http.route('/truck_cleaning/create_quote', type='json', auth='public', methods=['POST'], csrf=False)
    def create_quote(self, **kwargs):
        _logger.info('Received request to create quote')
        request.env['truck.cleaning'].sudo().get_viajes_and_create_quote()
        _logger.info('Processed request to create quote')
        return {'status': 'success', 'message': 'Quote created successfully'}
