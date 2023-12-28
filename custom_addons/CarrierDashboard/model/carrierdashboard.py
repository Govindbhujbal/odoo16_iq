from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date


class CarrierDashboard(models.Model):
    _name = "carrierdashboard.carrier"  # inside database name inside _name . will be replaced by _
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'CarrierDashboard records'
    _rec_name = "order_id"

    ref = fields.Char(string="reference", default=lambda self: _('Orders'))
    order_id = fields.Char(string="Order ID", default=lambda self: _('New'))
    From = fields.Char(string="From")
    to = fields.Char(string="To")
    status = fields.Char(string="Status", default="Pending")
    image = fields.Binary(string='Image', attachment=True)
    mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                            string="Mode Of Transport")

    product = fields.Char(string="Product")
    quantity = fields.Integer(string="Quantity")
    description = fields.Text(string="Description")

    vehicle_type = fields.Char(string="Vehicle Type")
    vehicle_no = fields.Char(string="Vehicle No")
    driver_name = fields.Char(string="Driver Name")
    driver_contact_number = fields.Char(string="Driver Contact Number")
    carrier_name = fields.Char(string="Carrier Name")
    tracking_number = fields.Char(string="Tracking Number")

    document_name = fields.Char(string='Document Name', help='Input placeholder for document')
    document = fields.Many2many('ir.attachment', string='Upload Documents', help='Attach multiple documents')

    tag_ids = fields.One2many('carrierdashboard.packer.lines', 'carrier_id',
                              string="CarrierDashboard Packer Lines")

    @api.model
    def create(self, vals_list):
        if vals_list.get('order_id', 'New') == 'New':
            vals_list['order_id'] = self.env['ir.sequence'].next_by_code('CarrierDashboard.carrier') or 'New'
            result = super(CarrierDashboard, self).create(vals_list)
            return result


class carrierdashboardpackerlines(models.Model):
    _name = "carrierdashboard.packer.lines"  # inside database name inside _name . will be replaced by _ appointment_packer_lines   carrierdashboard_packer_lines
    _description = 'CarrierDashboard Packer Lines'

    # product_id = fields.Many2one('product.product', required=True)
    # price_unit = fields.Float(related='product_id.list_price')
    date = fields.Date(string="Date")
    current_location = fields.Char(string="Current Location")
    # mode_of_transport = fields.Date(string="Mode of Transport")
    mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                            string="Mode Of Transport")
    carrier_name = fields.Char(string="Carrier Name")
    remark = fields.Char(string="Remark")
    carrier_id = fields.Many2one('carrierdashboard.carrier', string="Carrier Id")


