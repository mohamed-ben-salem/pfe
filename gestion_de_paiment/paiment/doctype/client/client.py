# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Client(Document):
	def validate(self):
		'''
		for item in self.ribs:
			cpt_bancaire = frappe.get_doc("Compte bancaire",item.cpt_banquaire)
			if self.par_defaut == 1:
				cpt_bancaire.rib = self.rib
		
		cpt_bancaire.save()'''
		pass

