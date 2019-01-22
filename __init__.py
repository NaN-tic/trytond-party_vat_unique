# This file is part party_vat_unique module for Tryton.  The COPYRIGHT file at
# the top level of this repository contains the full copyright notices and
# license terms.
from trytond.pool import Pool
from . import party


def register():
    Pool.register(
        party.Party,
        party.PartyIdentifier,
        module='party_vat_unique', type_='model')
    Pool.register(
        party.PartyReplace,
        module='party_vat_unique', type_='wizard')
