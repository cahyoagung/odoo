from openerp import models, fields, api

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    state_area = fields.Many2one(comodel_name='state.area',delegate=False,store=False,compute='state_area_compute')
    
    def state_area_compute(self):
        for obj in self:
            if obj.state_id:
                state=obj.state_id
                if state.state_area:
                    area=state.state_area
                    obj.state_area=area.id
    
    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            if state.state_area:
                return {'value': {'country_id': state.country_id.id,'state_area': state.state_area.id}}
            else:
                return {'value': {'country_id': state.country_id.id,'state_area': ''}}
        return {}  
