# -*- coding: utf-8 -*-

{
    'name': "TMC Auditors",
    'summary': 'Registro de Auditores Externos',
    'version': '10.0.1.0.0',
    'website': 'https://www.tmcrosario.gob.ar',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [
        u'tmc',
        u'partner_contact_gender'
    ],
    'data': [
        'security/auditors_group.xml',
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/institution.xml',
        'views/menu.xml',
    ],
    'demo': [],
}
