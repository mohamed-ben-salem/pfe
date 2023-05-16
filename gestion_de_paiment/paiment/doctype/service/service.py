# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
import string
from frappe.model.document import Document

class Service(Document):
	def validate (self):
		if self.responsable is not None:
			for char in self.responsable:
				if char not in string.ascii_letters:
					frappe.throw("nom invalide")
		else:
			pass
			

		
