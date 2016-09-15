from openerp import models, fields, api

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    state_area = fields.Many2one(comodel_name='state.area',delegate=True)
    
    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id,'state_area': state.state_area.id}}
        return {}  
