import time
from openerp import api
from openerp.osv import osv, fields

class Kursus (osv.osv):
    @api.one
    @api.depends('name','product_id')
    def _get_uom_name(self):
        for rec in self:
            if rec.product_id:
                rec.uom_name = 'name'
            else:
                rec.uom_name = 'empty'

    def _getuom(self, cr, uid, ids, name, arg, context=None):
        """ 
        get the alerts to display on the order form 
        """
        result = {}
        #alert_msg = self._default_alerts_get(cr, uid, context=context)
        for order in self.browse(cr, uid, ids, context=context):
            if order.product_id:
                if order.product_id.uom_id:
                    result[order.id] = order.product_id.uom_id.name
                else:
                    result[order.id] = ''
            else:
                result[order.id] = ''
        return result

    _name = 'training.kursus'
    _columns = {
        'name': fields.char('Judul Kursus', 128, required=True),
		'mentor': fields.char('Mentor', 128),
		'kapasitas': fields.integer('Kapasitas',size=4),
		'keterangan': fields.text('Keterangan'),
		'nomor': fields.integer('Nomor',size=4),
        'product_id': fields.many2one('product.template', 'Product', required=False, ondelete='cascade',default='',
            help="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios."),
		#'uom_name': fields.char(compute='_get_uom_name',string='Uom Name',store=False)
        'uom_name': fields.function(_getuom, type='char', string='Uom Name')
	}

Kursus()
