# -*- coding: utf-8 -*-

from openerp import models, fields


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

    university = fields.Selection([
        (u'UNR', u'Universidad Nacional de Rosario'),
        (u'UCA', u'Universidad Católica Argentina')]
    )

    school = fields.Selection([
        (u'cpcesfe1', u'Consejo Profesional de Ciencias Económicas de Rosario'),
        (u'cpcesfe2', u'Consejo Profesional de Ciencias Económicas de Santa Fe'),
        (u'colabro', u'Colegio de Abogados de Rosario')]
    )

    year_ids = fields.Many2many('auditors.year')

    work = fields.Text()

    control = fields.Text()

    studies = fields.Text()

    interests = fields.Text()
