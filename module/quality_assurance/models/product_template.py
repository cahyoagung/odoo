# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    qa_triggers = fields.One2many(
        comodel_name="qa.trigger.product_template_line",
        inverse_name="product_template",
        string="Quality assurance triggers")
