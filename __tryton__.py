#This file is part party_vat_unique module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Party Vat Unique',
    'name_ca_ES': 'NIF/CIF únic als tercers',
    'name_es_ES': 'NIF/CIF único para terceros',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''This module prevents duplicated VATs in parties''',
    'description_ca_ES': '''Aquest mòdul evita la duplicació dels NIF/CIF en els \
tercers''',
    'description_es_ES': '''Este módulo evita la duplicación de los NIF/CIF en \
los terceros''',
    'depends': [
        'ir',
        'res',
        'party'
    ],
    'xml': [
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
