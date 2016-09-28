# -*- coding: utf-8 -*-
# (c) 2010 NaN Projectes de Programari Lliure, S.L. (http://www.NaN-tic.com)
# (c) 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# (c) 2014 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Quality assurance",
    "version": "8.0.1.1.0",
    "category": "Quality assurance",
    "license": "AGPL-3",
    "author": "OdooMRP team, "
              "AvanzOSC, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Odoo Community Association (OCA)",
    "website": "http://www.odoomrp.com",
    "contributors": [
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
    ],
    "depends": [
        "product","mrp_operations_extension"
    ],
    "data": [
        "data/quality_assurance_data.xml",
        "security/quality_assurance_security.xml",
        "security/ir.model.access.csv",
        "wizard/qa_test_wizard_view.xml",
        "views/qa_menus.xml",
        "views/qa_inspection_view.xml",
        "views/qa_test_category_view.xml",
        "views/qa_test_view.xml",
        "views/qa_trigger_view.xml",
        "views/product_template_view.xml",
        "views/product_category_view.xml",
    ],
    "demo": [
        "demo/quality_assurance_demo.xml",
    ],
    "installable": True,
}
