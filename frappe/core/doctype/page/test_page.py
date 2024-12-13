# Copyright (c) 2015, Altrix Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
from frappe.tests.utils import AltrixTestCase

test_records = frappe.get_test_records("Page")


class TestPage(AltrixTestCase):
	def test_naming(self):
		self.assertRaises(
			frappe.NameError,
			frappe.get_doc(dict(doctype="Page", page_name="DocType", module="Core")).insert,
		)
