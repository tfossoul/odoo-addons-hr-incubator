# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import Form
from odoo.tests.common import TransactionCase


class TestCoopanameCustom(TransactionCase):
    def test_onchange_partner_id_updates_applicant(self):
        applicant = self.browse_ref("hr_recruitment.hr_case_salesman0")
        partner = self.browse_ref("base.res_partner_1")

        with Form(applicant) as form:
            form.partner_id = partner

        self.assertEquals(applicant.name, partner.name)
        self.assertEquals(applicant.partner_name, partner.name)
