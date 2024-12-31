from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def write(self, vals):
        # Prevent editing price from stock picking
        if self.env.context.get('from_stock_picking'):
            vals.pop('price_unit', None)
        return super().write(vals)