from odoo import models, fields, api


class Exporter(models.Model):
    _name = 'exporter.exporter'  # exporter_exporter
    _description = 'exporter.exporter'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")


class FarmerExporter(models.Model):
    _inherit = 'farmer.crop'

    # farmer_crop_id = fields.Many2one('farmer.crop', string='Farmer Crop')
    # fields.Button()

    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')


    def action_approved(self):
        for rec in self:
            rec.status = 'approved'

    def action_reject(self):
        for rec in self:
            rec.status = 'rejected'

    def action_send_to_approve(self):
        for rec in self:
            rec.status = 'pending'
