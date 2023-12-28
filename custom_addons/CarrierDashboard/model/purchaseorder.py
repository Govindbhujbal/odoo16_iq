from odoo import fields, models, api, _

class purchaseorder(models.Model):
    _inherit = ['purchase.order.line']
    _description = 'purchase order line records'

    open_quantity = fields.Integer(string="Open Quantity", compute='_compute_open_quantity')

    @api.depends('product_qty', 'qty_received')
    def _compute_open_quantity(self):
        for rec in self:
            rec.open_quantity = rec.product_qty - rec.qty_received


class purchaseorderhelper(models.Model):
    _inherit = ['purchase.order']
    _description = 'purchase order records'

    open_quantity = fields.Integer(string="Open Quantity", compute='_compute_helper')
    order_id = fields.Integer(string="order id")

    def _compute_helper(self):
        for records in self:
            purchase_order_lines = self.env['purchase.order.line'].search([('order_id', '=', records.id)],limit=1)
            if purchase_order_lines:
                records.open_quantity = purchase_order_lines[0].open_quantity
            else:
                records.open_quantity = 0
