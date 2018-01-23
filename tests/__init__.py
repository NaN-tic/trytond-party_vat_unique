# This file is part party_vat_unique module for Tryton.  The COPYRIGHT file at
# the top level of this repository contains the full copyright notices and
# license terms.
try:
    from trytond.modules.party_vat_unique.tests.test_party_vat_unique import suite
except ImportError:
    from .test_party_vat_unique import suite

__all__ = ['suite']
