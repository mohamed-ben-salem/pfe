# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Chequier(Document):
	def autoname(self):
		self.name = "CHQ-" + str(self.first_num) + "_" + str(self.last_num)
