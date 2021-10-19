======================
Party Replace Scenario
======================

Imports::

    >>> from proteus import Model, Wizard
    >>> from trytond.tests.tools import activate_modules

Install party VAT unique::

    >>> config = activate_modules('party_vat_unique')

Create a party::

    >>> Party = Model.get('party.party')
    >>> party = Party(name='Pam')
    >>> _ = party.identifiers.new(code="Identifier", type=None)
    >>> _ = party.contact_mechanisms.new(type='other', value="mechanism")
    >>> party.save()
    >>> address, = party.addresses
    >>> address.street = "St sample, 15"
    >>> address.city = "City"
    >>> address.save()

Create a party2::

    >>> party2 = Party(name='Pam')
    >>> _ = party2.identifiers.new(code="Identifier2", type=None)
    >>> _ = party2.contact_mechanisms.new(type='other', value="mechanism")
    >>> party2.save()
    >>> address2, = party2.addresses
    >>> address2.street = "St sample 2, 15"
    >>> address2.city = "City 2"
    >>> address2.save()
