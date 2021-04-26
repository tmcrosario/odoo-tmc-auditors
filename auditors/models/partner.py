from odoo import fields, models


class Partner(models.Model):

    _name = "res.partner"
    _inherit = "res.partner"

    auditor = fields.Boolean()

    profession = fields.Selection(
        [
            ("contador", "Contador Público"),
            ("abogado", "Abogado"),
            ("ingeniero", "Ingeniero Civil"),
        ]
    )

    registration_number = fields.Char()

    university_id = fields.Many2one(
        comodel_name="auditors.institution",
        domain=[("institution_type", "=", "university")],
    )

    school_id = fields.Many2one(
        comodel_name="auditors.institution",
        domain=[("institution_type", "=", "school")],
    )

    year_ids = fields.Many2many(comodel_name="auditors.year")

    work = fields.Text()

    control = fields.Text()

    studies = fields.Text()

    interests = fields.Text()
