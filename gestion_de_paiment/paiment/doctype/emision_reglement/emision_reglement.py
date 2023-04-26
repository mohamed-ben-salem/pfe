# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
class EmisionReglement(Document):
	def validate(self):
		for item in self.liste_depense:
			Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
			Depenses.mode_de_réglement = self.mode_de_réglement
			Depenses
			if Depenses.status == "CREE":
				Depenses.status = "EMISE"
			Depenses.save()
		self.date_emission = today()


