// Copyright (c) 2023, Mohseen Habib and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Gym Trainer", {
 	after_save :function(frm) {
           frappe.msgprint("Trainer has successfully been created")
 	},
 });
