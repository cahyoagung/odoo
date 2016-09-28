from openerp import models, fields, api

class QaWorkOrder(models.Model):
    _inherit = 'mrp.production.workcenter.line'
    
    @api.one
    def on_produce_here_change(self,do_production):
        obj=self
        data=self.pool.get('mrp.production.workcenter.line').search([('production_id','=',obj.production_id.id)])
        ketemu=False
        for raw in data:
            if obj.id!=raw.id:
                if do_production==raw.do_production:
                    ketemu=True
                    obj.do_production=False
                    return {'value':{'do_production':False}}
        
        if ketemu==False:
            return {}