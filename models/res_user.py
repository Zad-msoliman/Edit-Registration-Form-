from odoo import models, fields, api





class ResUser(models.Model):
    _inherit = 'res.users'

    mobile = fields.Char(related='partner_id.mobile',string='Mobile' )
    phone = fields.Char(related='partner_id.phone',string='Phone' )