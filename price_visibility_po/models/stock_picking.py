from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    purchase_price = fields.Float(
        related='purchase_line_id.price_unit',
        string='Unit Price',
        readonly=True,
        store=True
    )
    purchase_currency_id = fields.Many2one(
        related='purchase_line_id.currency_id',
        string='Currency',
        readonly=True,
        store=True
    )