from openerp import models, fields

class state_area(models.Model):
    _name = 'state.area'
    name = fields.Char(string='State Area', required=True)
    
class state_add(models.Model):
    _inherit = 'res.country.state'
    state_area = fields.Many2one(comodel_name='state.area',delegate=True)

