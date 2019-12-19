# This file is part party_vat_unique module for Tryton.  The COPYRIGHT file at
# the top level of this repository contains the full copyright notices and
# license terms.
from trytond.pool import PoolMeta
from trytond.model import Exclude
from trytond import backend
from sql.operators import Equal

__all__ = ['Party', 'PartyIdentifier', 'PartyReplace']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    @classmethod
    def copy(cls, parties, default=None):
        if default is None:
            default = {}
        default['identifiers'] = None
        return super(Party, cls).copy(parties, default=default)


class PartyIdentifier(metaclass=PoolMeta):
    __name__ = 'party.identifier'

    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        super().__register__(module_name)
        table = TableHandler(cls, module_name)

        # Drop number_uniq constraint
        table.drop_constraint('number_uniq')

    @classmethod
    def __setup__(cls):
        super(PartyIdentifier, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('number_excl', Exclude(t, (t.type, Equal), (t.code, Equal),
                where=(t.type == 'eu_vat')), 'party_vat_unique.msg_vat_unique'),
        ]

    @staticmethod
    def default_type():
        return 'eu_vat'


class PartyReplace(metaclass=PoolMeta):
    __name__ = 'party.replace'

    @classmethod
    def fields_to_replace(cls):
        fields_to_replace = super(PartyReplace, cls).fields_to_replace()
        pidentifier = ('party.identifier', 'party')
        if pidentifier not in fields_to_replace:
            fields_to_replace.append(pidentifier)
        return fields_to_replace
