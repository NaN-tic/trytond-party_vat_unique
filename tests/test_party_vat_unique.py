# This file is part of the party_vat_unique module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PartyVatUniqueTestCase(ModuleTestCase):
    'Test Party Vat Unique module'
    module = 'party_vat_unique'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyVatUniqueTestCase))
    return suite