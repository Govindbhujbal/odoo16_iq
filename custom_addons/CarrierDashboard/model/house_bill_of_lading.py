from odoo import fields, models, api, _


class HouseBillOfLading(models.Model):
    _name = "sale.housebilloflading"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'sale House Bill Of Lading Records'

    shipper = fields.Char(string="shipper", help='Reference from Res.Users records')  # this is exporter
    pages = fields.Char(string="pages")  # list of pages for ex : 1 of 1
    shipper_reference_id = fields.Many2one('sale.order', string="shipper's reference",
                                           help='Reference from Sales Order records')  # this is sales order no
    bill_of_lading_number = fields.Char(string="bill of lading number",
                                        default=lambda self: _('New'))  # hardcode its value as BL12152023
    carriers_reference = fields.Char(
        string="carrier's reference")  # this is Tracking reference from delivery page additional info tab
    unique_consignment_reference = fields.Char(string="unique consignment reference")  # keep it blank

    consignee = fields.Char(string="consignee")  # this is customer from sale.order
    carrier_name = fields.Char(string="carrier name")  # carrier name from delivery page additional info tab
    place_of_receipt = fields.Char(string="place of receipt")  # hardcode as : Kenya
    vessel_aircraft = fields.Char(string="vessel / aircraft")  # keep it blank
    voyage_no = fields.Char(string="voyage no")  # keep it blank
    port_of_loading = fields.Char(string="port of loading")  # hardcode as : Lamu, Kenya
    port_of_discharge = fields.Char(string="port of discharge")  # hardcode as : The Hauge, Netherland
    place_of_delivery = fields.Char(string="place of delivery")  # hardcode as : The Hauge, Netherland
    final_destination = fields.Char(string="final destination")  # hardcode as : The Hauge, Netherland
    order_id = fields.Char(string="order ID")  # this is sales order no
    no_of_packages = fields.Char(string="no of packages")  # keep it blank
    product_name = fields.Char(string="product name")  # this is name of product inside sale.order notebook section
    lot_no = fields.Char(string="lot no.")  # keep it blank
    net_weight_kg = fields.Char(string="net weight(kg)")  # weight from product/inventory
    gross_weight_kg = fields.Char(string="gross weight(kg)")  # weight from product/inventory
    volume_m3 = fields.Char(string="volume (m³)")  # volume from product/inventory
    consignment_total = fields.Char(string="consignment total")  # same value as in gross wt, net wt, volume
    container_nos = fields.Char(string="container no(s)")  # keep it blank
    container_type = fields.Char(string="container type")  # keep it blank
    cargo_weight_kg = fields.Char(string="cargo weight(kg)")  # keep it blank
    original_bills_of_lading = fields.Char(string="no. of original bills of lading")  # hardcode as : 1
    incoterms_2020 = fields.Char(string="incoterms® 2020")  # keep it blank
    payable_at = fields.Char(string="payable at")  # keep it blank
    freight_charges = fields.Char(string="freight charges")  # keep it blank
    shipped_on_board_date = fields.Char(string="shipped on board date")  # keep it blank
    place_and_date_of_issue = fields.Char(string="place and date of issue")  # ?
    signatory_company = fields.Char(string="signatory company")  # hardcode as : East Africa Trade
    name_of_authorized_signatory = fields.Char(
        string="name of authorized signatory")  # this is exporter or user who is sending
    signature = fields.Char(string="signature")  # hardcode the signature

    # below code is added recently
    document_name = fields.Char(string='Document Name', help='Input placeholder for document')
    # image = fields.Many2many('ir.attachment', string='Upload Signature', help='Attach multiple documents')
    image = fields.Binary('Upload Signature', attachment=True)

    # ref = fields.Char(string="Reference", default=lambda self: _('New'))

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['bill_of_lading_number'] = self.env['ir.sequence'].next_by_code('sale.housebilloflading')
    #     return super(HouseBillOfLading, self).create(vals_list)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['place_of_receipt'] = "Kenya"
            vals['port_of_loading'] = "Lamu, Kenya"
            vals['port_of_discharge'] = "The Hauge, Netherland"
            vals['place_of_delivery'] = "The Hauge, Netherland"
            vals['final_destination'] = "The Hauge, Netherland"
            vals['original_bills_of_lading'] = "1"
            vals['signatory_company'] = "East Africa Trade"
            vals['pages'] = "1 of 1"

            vals['bill_of_lading_number'] = self.env['ir.sequence'].next_by_code('sale.housebilloflading')

        return super(HouseBillOfLading, self).create(vals_list)

    @api.onchange('shipper_reference_id')
    def onchange_shipper_reference_id(self):
        if self.shipper_reference_id:
            self.order_id = self.shipper_reference_id.name
            self.consignee = self.shipper_reference_id.partner_id.name
            self.shipper = self.shipper_reference_id.user_id.name
            self.name_of_authorized_signatory = self.shipper_reference_id.user_id.name
        else:
            self.order_id = ''
            self.consignee = ''
            self.shipper = ''
            self.name_of_authorized_signatory = ''

        for records in self:
            # sale_orders = self.env['sale.order'].search([('name','=',records.order_id)])
            # if sale_orders:
            #     print("inside sale_orders")
            #     records.shipper = sale_orders[0].user_id.name
            #     records.name_of_authorized_signatory = sale_orders[0].user_id.name
            # else:
            #     print("in else of sale_orders")
            #     records.shipper = ''
            #     records.name_of_authorized_signatory = ''
            sale_order_lines = self.env['sale.order.line'].search([('order_id', '=', records.order_id)])
            stock_pickings = self.env['stock.picking'].search([('sale_id', '=', records.order_id)])
            if stock_pickings:
                stock_picking_id = stock_pickings[0].id
                stock_move_lines = self.env['stock.move.line'].search([('picking_id', '=', stock_picking_id)])
                if stock_move_lines:
                    records.lot_no = stock_move_lines[0].lot_id.name
                else:
                    records.lot_no = ''
                records.carrier_name = stock_pickings[0].carrier_id.name
                records.carriers_reference = stock_pickings[0].carrier_tracking_ref
                records.net_weight_kg = stock_pickings[0].weight
                records.gross_weight_kg = stock_pickings[0].weight

            else:
                records.carrier_name = ''
                records.carriers_reference = ''
                records.net_weight_kg = ''
                records.gross_weight_kg = ''

            if sale_order_lines:
                print("inside if of sale_order_lines")
                # print(sale_order_lines.name)
                len_of_pol = len(sale_order_lines)
                for i in range(len_of_pol):
                    print(i)
                    records.product_name = sale_order_lines[0].name
            else:
                print("inside else of sale_order_lines")
                records.product_name = ''
