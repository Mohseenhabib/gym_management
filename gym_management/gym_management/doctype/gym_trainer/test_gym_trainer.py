# Copyright (c) 2023, Mohseen Habib and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymTrainer(FrappeTestCase):
	
	def test_gym_member(self):
		test_gym_trainer = frappe.get_doc({
			"doctype": "Gym Trainer" ,
			"first_name": "habeeb" ,
			"last_name": "haroon" ,
		
		}).insert()

