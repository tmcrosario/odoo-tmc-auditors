
from odoo import models, fields


class Institution(models.Model):
    _name = 'auditors.institution'

    name = fields.Char()

    institution_type = fields.Selection([
        (u'university', u'University'),
        (u'school', u'School')
    ])
