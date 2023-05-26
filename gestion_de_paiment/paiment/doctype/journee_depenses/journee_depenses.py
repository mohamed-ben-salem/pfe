# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class Journeedepenses(Document):
    def validate(self):
        if self.is_new():
            self.status='Non Cloturée'
    def after_insert(self):       
        for item in self.liste_depenses_validee:
            Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
            Depenses.journee_cloture= self.name
            self.date_de_cloture = today()
            Depenses.date_de_cloture = self.date_de_cloture
            Depenses.save()
            
            
             
             

