from odoo import fields, models


class Year(models.Model):

    _name = "auditors.year"
    _description = "Year"

    name = fields.Char()

    auditor_ids = fields.Many2many(
        comodel_name="res.partner", domain=[("active", "=", False)]
    )
