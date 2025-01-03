# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from collections import defaultdict

from odoo import Command, _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrderDiscount(models.TransientModel):
    _name = 'purchase.order.discount'
    _description = "Discount Wizard"

    purchase_order_id = fields.Many2one(
        'purchase.order', default=lambda self: self.env.context.get('active_id'), required=True)
    company_id = fields.Many2one(related='purchase_order_id.company_id')
    currency_id = fields.Many2one(related='purchase_order_id.currency_id')
    discount_amount = fields.Monetary(string="Amount")
    discount_percentage = fields.Float(string="Percentage")
    discount_type = fields.Selection(
        selection=[
            ('pol_discount', "On All Order Lines"),
            ('po_discount', "Global Discount"),
            ('amount', "Fixed Amount"),
        ],
        default='pol_discount',
    )

    # CONSTRAINT METHODS #

    @api.constrains('discount_type', 'discount_percentage')
    def check_discount_amount(self):
        for wizard in self:
            if (
                wizard.discount_type in ('pol_discount', 'po_discount')
                and (wizard.discount_percentage > 1.0 or wizard.discount_percentage < 0.0)
            ):
                raise ValidationError(_("Invalid discount amount"))

    def prepare_discount_product_values(self):
        self.ensure_one()
        return {
            'name': _('Discount'),
            'type': 'service',
            'purchase_method': 'purchase',
            'list_price': 0.0,
            'company_id': self.company_id.id,
            'taxes_id': None,
        }

    def prepare_discount_line_values(self, product, amount, taxes, description=None):
        self.ensure_one()

        vals = {
            'order_id': self.purchase_order_id.id,
            'product_id': product.id,
            'sequence': 999,
            'price_unit': -amount,
            'taxes_id': [Command.set(taxes.ids)],
        }
        if description:
            vals['name'] = description

        return vals

    def create_discount_lines(self):
        """Create POline(s) according to wizard configuration"""
        self.ensure_one()

        discount_product = self.company_id.purchase_discount_product_id
        if not discount_product:
            self.company_id.purchase_discount_product_id = self.env['product.product'].create(
                self.prepare_discount_product_values()
            )
            discount_product = self.company_id.purchase_discount_product_id

        if self.discount_type == 'amount':
            vals_list = [
                self.prepare_discount_line_values(
                    product=discount_product,
                    amount=self.discount_amount,
                    taxes=self.env['account.tax'],
                )
            ]
        else: # po_discount
            total_price_per_tax_groups = defaultdict(float)
            for line in self.purchase_order_id.order_line:
                if not line.product_uom_qty or not line.price_unit:
                    continue

                total_price_per_tax_groups[line.taxes_id] += line.price_subtotal

            if not total_price_per_tax_groups:
                # No valid lines on which the discount can be applied
                return
            elif len(total_price_per_tax_groups) == 1:
                # No taxes, or all lines have the exact same taxes
                taxes = next(iter(total_price_per_tax_groups.keys()))
                subtotal = total_price_per_tax_groups[taxes]
                vals_list = [{
                    **self.prepare_discount_line_values(
                        product=discount_product,
                        amount=subtotal * self.discount_percentage,
                        taxes=taxes,
                        description=_(
                            "Discount: %(percent)s%%",
                            percent=self.discount_percentage*100
                        ),
                    ),
                }]
            else:
                vals_list = [
                    self.prepare_discount_line_values(
                        product=discount_product,
                        amount=subtotal * self.discount_percentage,
                        taxes=taxes,
                        description=_(
                            "Discount: %(percent)s%%"
                            "- On products with the following taxes %(taxes)s",
                            percent=self.discount_percentage*100,
                            taxes=", ".join(taxes.mapped('name'))
                        ),
                    ) for taxes, subtotal in total_price_per_tax_groups.items()
                ]
        return self.env['purchase.order.line'].create(vals_list)

    def action_discount_apply(self):
        self.ensure_one()
        self = self.with_company(self.company_id)
        if self.discount_type == 'pol_discount':
            self.purchase_order_id.order_line.write({'discount': self.discount_percentage*100})
        else:
            self.create_discount_lines()
