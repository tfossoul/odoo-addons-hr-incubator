from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    some_field = fields.Char(string="Some Field", required=False)
