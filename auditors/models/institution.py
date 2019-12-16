from odoo import models, fields


class Institution(models.Model):

    _name = 'auditors.institution'
    _description = 'Institution'

    name = fields.Char()

    institution_type = fields.Selection([('university', 'University'),
                                         ('school', 'School')])
