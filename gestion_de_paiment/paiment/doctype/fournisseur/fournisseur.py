# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Fournisseur(Document):
	def validate(self):
		for item in self.ribs:
			if item.par_defaut == 1:
				cpt = frappe.get_doc("Compte bancaire",item.tiers)
				cpt.rib = item.rib
				cpt.save()




