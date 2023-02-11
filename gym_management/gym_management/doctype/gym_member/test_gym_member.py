# Copyright (c) 2023, Mohseen Habib and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMember(FrappeTestCase):
	def test_our_gym_member(self):
		test_gym = frappe.get_doc({
			"doctype": "Gym Member" ,
			"first_name": "habeb" ,
			"last_name": "haroon" ,
			"email" : "mohseen@gmail.com"	
		}).insert()
