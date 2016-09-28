# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class QaTrigger(models.Model):
    _name = 'qa.trigger'
    _description = 'Quality assurance trigger'

    name = fields.Char(string='Name', required=True, select=True,
                       translate=True)
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company',
        default=lambda self: self.env['res.company']._company_default_get(
            'qa.test'))
    partner_selectable = fields.Boolean(
        string='Selectable by partner', default=False, readonly=True,
        help='This technical field is to allow to filter by partner in'
        ' triggers')
