# -*- coding: utf-8 -*-

{
    'name': "Auditors",
    'summary': """
        Registro de Auditores Externos""",
    'category': 'Tribunal Municipal de Cuentas',
    'version': '8.0.1.0.0',
    'author': "Dirección de TI y Calidad",
    'website': "http://www.tmcrosario.gob.ar",
    'depends': [
        u'base',
        u'tmc',
        u'partner_person'
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
