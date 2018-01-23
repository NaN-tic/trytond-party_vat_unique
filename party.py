# This file is part party_vat_unique module for Tryton.  The COPYRIGHT file at
# the top level of this repository contains the full copyright notices and
# license terms.
from trytond.pool import PoolMeta
from trytond.model import Unique

__all__ = ['Party', 'PartyIdentifier']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'

    @classmethod
    def copy(cls, parties, default=None):
        if default is None:
            default = {}
        default['identifiers'] = None
        return super(Party, cls).copy(parties, default=default)


class PartyIdentifier:
    __metaclass__ = PoolMeta
    __name__ = 'party.identifier'

    @classmethod
    def __setup__(cls):
        super(PartyIdentifier, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('number_uniq', Unique(t, t.type, t.code),
                'There is another code with the same number.\n'
                'The code of the party must be unique!'),
        ]

    @staticmethod
    def default_type():
        return 'eu_vat'
