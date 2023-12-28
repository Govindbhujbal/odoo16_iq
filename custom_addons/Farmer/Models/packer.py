from odoo import fields, models, api, _

class packer(models.Model):
    _name = "farmer.packer.goods" # inside database name inside _name . will be replaced by _
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'packer records'


    name = fields.Char(string='Name', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender', tracking=True)
    packer_date_of_birth = fields.Date(string="Date Of Birth")
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    active = fields.Boolean(default=True)
    age = fields.Integer(string='Age')

    tag_ids = fields.Many2many('res.partner.category','scm_packer_tag_rel','packer_id','tag_id',string='Tags')


    #
    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         name = f'{rec.ref} - {rec.name}'
    #         res.append((rec.id,name))
    #     return res

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'].next_by_code('farmer.packer.goods')
        return super(packer,self).create(vals_list)