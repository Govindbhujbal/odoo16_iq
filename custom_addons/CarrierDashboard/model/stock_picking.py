from odoo import fields, models, api, _


class StockPicking(models.Model):
    # _name = "salescarrier.carrier"     # sale_order
    _inherit = 'stock.picking'
    _description = 'Stock Picking records'

    custom_field = fields.Char(string='Custom Field')
    sale_description = fields.Char(string='Sale Description')

    stock_picking_id = fields.Many2one('res.users',string="Stock Picking Id")

    document_name = fields.Char(string='Document Name', help='Input placeholder for document')
    document = fields.Many2many('ir.attachment', string='Upload Documents', help='Attach multiple documents')
