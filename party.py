#This file is part party_vat_unique module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        cls._sql_constraints.extend([
            ('vat_uniq', 'UNIQUE(vat_number, vat_country)',
             'There is another party with the same VAT.\n'
             'The VAT of the party must be unique!')
        ])

