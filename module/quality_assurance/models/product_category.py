# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProductCategory(models.Model):
    _inherit = "product.category"

    qa_triggers = fields.One2many(
        comodel_name="qa.trigger.product_category_line",
        inverse_name="product_category",
        string="Quality assurance triggers")
