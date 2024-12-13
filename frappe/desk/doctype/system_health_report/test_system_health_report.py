# Copyright (c) 2024, Altrix Technologies and Contributors
# See license.txt

import frappe
from frappe.tests.utils import AltrixTestCase


class TestSystemHealthReport(AltrixTestCase):
	def test_it_works(self):
		frappe.get_doc("System Health Report")
