{
    'name': "TMC Auditors",
    'summary': 'Registro de Auditores Externos',
    'version': '13.0.1.0.0',
    'website': 'https://www.tmcrosario.gob.ar',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [
        'tmc',
        'partner_contact_gender'
    ],
    'data': [
        'security/auditors_group.xml',
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/auditors_menus.xml',
        'views/institution_views.xml',
        'views/institution_menus.xml',
    ],
    'demo': [],
}  # yapf: disable
