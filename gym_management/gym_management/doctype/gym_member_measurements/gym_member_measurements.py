# Copyright (c) 2023, Mohseen Habib and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
class GymMemberMeasurements(Document):
	# Calculate BMI
	def before_save(self):
		if self.height:
			self.bmi = (self.weight / (self.height * self.height))
			return self.bmi
    #Calculate BMR
	def after_save(self):
		if self.weight:
			self.bmr = (66.5 + ( 13.75 * self.weight) + ( 5.003 * (self.height * 100.00) ))
