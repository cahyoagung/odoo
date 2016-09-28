# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


def _filter_trigger_lines(trigger_lines):
    filtered_trigger_lines = []
    unique_tests = []
    for trigger_line in trigger_lines:
        if trigger_line.test not in unique_tests:
            filtered_trigger_lines.append(trigger_line)
            unique_tests.append(trigger_line.test)
    return filtered_trigger_lines


class QaTriggerLine(models.AbstractModel):
    _name = "qa.trigger.line"
    _description = "Abstract line for defining triggers"

    trigger = fields.Many2one(comodel_name="qa.trigger", required=True)
    test = fields.Many2one(comodel_name="qa.test", required=True)
    user = fields.Many2one(
        comodel_name='res.users', string='Responsible',
        track_visibility='always', default=lambda self: self.env.user)
    partners = fields.Many2many(
        comodel_name='res.partner', string='Partners',
        help='If filled, the test will only be created when the action is done'
        ' for one of the specified partners. If empty, the test will always be'
        ' created.', domain="[('parent_id', '=', False)]")

    def get_trigger_line_for_product(self, trigger, product, partner=False):
        """Overridable method for getting trigger_line associated to a product.
        Each inherited model will complete this module to make the search by
        product, template or category.
        :param trigger: Trigger instance.
        :param product: Product instance.
        :return: Set of trigger_lines that matches to the given product and
        trigger.
        """
        return set()


class QaTriggerProductCategoryLine(models.Model):
    _inherit = "qa.trigger.line"
    _name = "qa.trigger.product_category_line"

    product_category = fields.Many2one(comodel_name="product.category")

    def get_trigger_line_for_product(self, trigger, product, partner=False):
        trigger_lines = super(
            QaTriggerProductCategoryLine,
            self).get_trigger_line_for_product(trigger, product,
                                               partner=partner)
        category = product.categ_id
        while category:
            for trigger_line in category.qa_triggers.filtered(
                    lambda r: r.trigger == trigger and (
                    not r.partners or not partner or
                    partner.commercial_partner_id in r.partners)):
                trigger_lines.add(trigger_line)
            category = category.parent_id
        return trigger_lines


class QaTriggerProductTemplateLine(models.Model):
    _inherit = "qa.trigger.line"
    _name = "qa.trigger.product_template_line"

    product_template = fields.Many2one(comodel_name="product.template")

    def get_trigger_line_for_product(self, trigger, product, partner=False):
        trigger_lines = super(
            QaTriggerProductTemplateLine,
            self).get_trigger_line_for_product(trigger, product,
                                               partner=partner)
        for trigger_line in product.product_tmpl_id.qa_triggers.filtered(
                lambda r: r.trigger == trigger and (
                not r.partners or not partner or
                partner.commercial_partner_id in r.partners)):
            trigger_lines.add(trigger_line)
        return trigger_lines


class QaTriggerProductLine(models.Model):
    _inherit = "qa.trigger.line"
    _name = "qa.trigger.product_line"

    product = fields.Many2one(comodel_name="product.product")

    def get_trigger_line_for_product(self, trigger, product, partner=False):
        trigger_lines = super(
            QaTriggerProductLine,
            self).get_trigger_line_for_product(trigger, product,
                                               partner=partner)
        for trigger_line in product.qa_triggers.filtered(
                lambda r: r.trigger == trigger and (
                not r.partners or not partner or
                partner.commercial_partner_id in r.partners)):
            trigger_lines.add(trigger_line)
        return trigger_lines
