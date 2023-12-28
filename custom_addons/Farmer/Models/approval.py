from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class approval(models.Model):
    _name = "farmer.packer.approval" # inside database name inside _name . will be replaced by _
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'farmer packer records'
    _rec_name = 'ref'

    name = fields.Char(string='Packer Name',required=True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Packer Gender', tracking=True)
    # ref = fields.Char(string="Reference",required=True)
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    active = fields.Boolean(default=True)


    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id,name))
        return res