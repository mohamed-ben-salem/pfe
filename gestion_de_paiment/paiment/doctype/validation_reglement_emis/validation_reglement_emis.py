# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class ValidationReglementEmis(Document):
    def validate(self):
        for item in self.liste_de_dépenses_emis:
            Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
            if Depenses.status == "EMISE":
                Depenses.status = "VALIDEE"
            self.date_de_validation= today()
            Depenses.date_de_validation= self.date_de_validation
            
            Depenses.save()
            
	
            
