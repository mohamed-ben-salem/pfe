# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Societe(Document):
	def validate_abbr(self):
		self.abbr = "".join(c[0] for c in self.nom_de_la_société.split()).upper()
