from odoo import fields, models, api, _


class salescarrier(models.Model):
    # _name = "salescarrier.carrier"     # sale_order
    _inherit = 'sale.order'
    _description = 'CarrierDashboard sales records'

    custom_field = fields.Char(string='Custom Field')
    sale_description = fields.Char(string='Sale Description')

    document_name = fields.Char(string='Document Name', help='Input placeholder for document')
    document = fields.Many2many('ir.attachment', string='Upload Documents', help='Attach multiple documents')

    tag_ids = fields.One2many('sales.carrier.details', 'carrier_id',string="")
    tracking_number_ids = fields.One2many('sales.carrier.details', 'tracking_number_id',string="")




class SalesCarrierDetails(models.Model):
    _name = "sales.carrier.details"
    _description = 'Sales Carrier Details'

    date = fields.Date(string="Date")
    current_location = fields.Char(string="Current Location")
    mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                            string="Mode Of Transport")
    carrier_name = fields.Char(string="Carrier Name")
    remark = fields.Char(string="Remark")
    carrier_id = fields.Many2one('sale.order', string="Carrier Id")
    color = fields.Char(string="color")

    vehicle_type = fields.Char(string="Vehicle Type")
    vehicle_no = fields.Char(string="Vehicle No")
    driver_name = fields.Char(string="Driver Name")
    driver_contact_number = fields.Char(string="Driver Contact Number")
    tracking_number_id = fields.Many2one('sale.order', string="Tracking Id")