# This file is part of the party_vat_unique module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.tests.test_tryton import doctest_teardown
from trytond.tests.test_tryton import doctest_checker
from trytond.pool import Pool
from trytond.exceptions import UserError


class PartyVatUniqueTestCase(ModuleTestCase):
    'Test Party Vat Unique module'
    module = 'party_vat_unique'

    @with_transaction()
    def test_identifier_unique(self):
        'Test Identifier uniqueness'
        pool = Pool()
        Party = pool.get('party.party')
        Identifier = pool.get('party.identifier')

        party = Party(name='test')
        party.save()

        identifier = Identifier(party=party, code='ES47690558N',
            type='eu_vat')
        identifier.save()

        duplicated_identifier = Identifier(party=party, code='ES47690558N',
            type='eu_vat')
        with self.assertRaises(UserError):
            duplicated_identifier.save()

    @with_transaction()
    def test_identifier_unique_diferent_parties(self):
        'Test Identifier uniqueness with diferent parties'
        pool = Pool()
        Party = pool.get('party.party')
        Identifier = pool.get('party.identifier')

        party = Party(name='test')
        party.save()

        identifier = Identifier(party=party, code='ES47690558N',
            type='eu_vat')
        identifier.save()
        # Test with diferent party
        new_party = Party(name='test')
        new_party.save()
        duplicated_identifier = Identifier(party=new_party, code='ES47690558N',
            type='eu_vat')
        with self.assertRaises(UserError):
            duplicated_identifier.save()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyVatUniqueTestCase))
    suite.addTests(doctest.DocFileSuite(
            'scenario_party_replace.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
