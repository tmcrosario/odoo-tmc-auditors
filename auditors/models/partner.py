# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    auditor = fields.Boolean(
        string='Auditor'
    )

    civil_status = fields.Selection(
        [(u'single', u'Single'),
         (u'married', u'Married'),
         (u'divorced', u'Divorced')]
    )

    profession = fields.Selection([
        ('uContador', u'Contador Público'),
        ('uAbogado', u'Abogado'),
        ('uIngeniero', u'Ingeniero Civil')]
    )

    registration_number = fields.Char()

    university_id = fields.Many2one(
        comodel_name='auditors.institution',
        domain=[('institution_type', '=', 'university')]
    )

    school_id = fields.Many2one(
        comodel_name='auditors.institution',
        domain=[('institution_type', '=', 'school')]
    )

    year_ids = fields.Many2many('auditors.year')

    work = fields.Text()

    control = fields.Text()

    studies = fields.Text()

    interests = fields.Text()
