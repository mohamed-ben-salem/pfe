# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Annulationdepense(Document):
	def validate(self):
		for item in self.liste_dépense_annulé:
			Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
			if Depenses.status == "VALIDEE":
				Depenses.status = "CREE"
				Depenses.motif_dannulation= self.motif_dannulation
			Depenses.save()
