from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date

class farmer(models.Model):
    _name = "farmer.crop" # inside database name inside _name . will be replaced by _
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'farmer records'

    name = fields.Char(string='Name',required=True, tracking=True)
    # capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name',store=True)
    # message_follower_ids
    country = fields.Char(string='Country',required=True,default='India')
    farmer_date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age',compute='_compute_age', tracking=True,store=True)
    # is_child = fields.Boolean(string='Is Child ?', tracking=True)
    notes = fields.Text(string='Notes')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('others','Others')],string='Gender', tracking=True)
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    packer_id = fields.Many2one('farmer.packer.goods',string="Packer Id & Name")
    packing_Datetime = fields.Datetime(string="Harvesting Time")  #,default=fields.Datetime.now
    packer_name = fields.Char(string="Packer Name",related='packer_id.name')
    active = fields.Boolean(string='Active', default=True)

    state = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')], string='status')

    # status = fields.Selection([
    #     ('pending','Pending'),
    #     ('in_consultation','In Consultation'),
    #     ('done','Done')], string="Status", reqired=True)


    packer_gender = fields.Selection(related="packer_id.gender")
    tag_ids = fields.Many2many('res.partner.category','scm_farmer_tag_rel','farmer_id','tag_id',string='Tags')



    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'].next_by_code('farmer.crop')
        return super(farmer,self).create(vals_list)



    @api.depends('farmer_date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.farmer_date_of_birth:
                rec.age = today.year - rec.farmer_date_of_birth.year
            else:
                rec.age = 0


    def action_send_to_approve(self):
        for rec in self:
            rec.state = 'pending'