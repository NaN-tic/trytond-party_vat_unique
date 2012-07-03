#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL

class Party(ModelSQL, ModelView):
    'Party'
    _name = 'party.party'
    _description = __doc__

    def __init__(self):
        super(Party, self).__init__()
        self._sql_constraints.extend([
            ('vat_uniq', 'UNIQUE(vat_number, vat_country)',
             'There is another party with the same VAT.\n'
             'The VAT of the party must be unique!')
        ])

Party()
