from openerp.osv import osv, fields

class res_partner(osv.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'state_area' : fields.Char(string='State Area', size=128, required=False)
    }

res_partner()    
