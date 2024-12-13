// Copyright (c) 2017, Altrix Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Print Style", {
	refresh: function (frm) {
		frm.add_custom_button(__("Print Settings"), () => {
			frappe.set_route("Form", "Print Settings");
		});
	},
});
