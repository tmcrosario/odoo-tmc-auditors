
from odoo import models, fields


class Year(models.Model):
    _name = 'auditors.year'

    name = fields.Char()

    auditor_ids = fields.Many2many(
        comodel_name='res.partner',
        domain=[('active', '=', False)]
    )
