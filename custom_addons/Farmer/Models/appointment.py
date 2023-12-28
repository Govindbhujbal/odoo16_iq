from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class appointment(models.Model):
    _name = "farmer.packer.appointment"  # inside database name inside _name . will be replaced by _
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'farmer packer appointment'
    _rec_name = 'ref'

    farmer_id = fields.Many2one('farmer.crop', string="farmer ID", help='Reference from farmer records')
    packer_id = fields.Many2one('farmer.packer.goods', string="Packer Id & Name")
    exporter_id = fields.Many2one('res.users', string='Exporter')
    packer_line_ids = fields.One2many('appointment.packer.lines','appointment_id',string="Packer Lines")
    packer_name = fields.Char(string='Packer Name', related='packer_id.name', tracking=True)
    farmer_name = fields.Char(string='Farmer Name', related='farmer_id.name', tracking=True)
    farmer_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                                     string='Farmer Gender', related="farmer_id.gender", tracking=True)
    packer_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                                     string='Packer Gender', related="packer_id.gender", tracking=True)

    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    packing_Datetime = fields.Datetime(string="Packing Time", default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='priority')

    state = fields.Selection([
        ('draft', 'Draft'),  # draft
        ('done', 'Done'),  # done
        ('cancel', 'Cancelled'),  # cancel
        ('in_consultation', 'In Consultation')], default='pending', string='status')  # in_consultation

    additional_note = fields.Html(string="Addition Note")

    tag_ids = fields.Many2many('res.partner.category', 'scm_appointment_tag_rel', 'appointment_id', 'tag_id',
                               string='Tags')


    hide_sales_price = fields.Boolean(string="Hide Sales Price")

    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         name = f'{rec.ref} - {rec.name}'
    #         res.append((rec.id,name))
    #     return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('farmer.packer.appointment')
        return super(appointment, self).create(vals_list)

    def action_test(self):
        print('object button clicked !!!')
        return {
            'effect': {
                'fadeout': 'slow',
                # fadeout slow attribute will automatically fadeout rainbow_main after some time if won't give this attribute then rainbow_main will not fadeout until we do another action
                'message': 'click successful',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'


    def action_done(self):
        for rec in self:
            rec.state = 'done'


    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


class AppointmentPackerLines(models.Model):
    _name = "appointment.packer.lines"  # inside database name inside _name . will be replaced by _ appointment_packer_lines
    _description = 'Appointment Packer Lines'

    product_id = fields.Many2one('product.product',required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string="Quantity",default=1)
    appointment_id = fields.Many2one('farmer.packer.appointment',string="Appointment")