# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import msgprint

class Societe(Document):
    def validate (self):
        for item in self.ribs:
            if item.par_defaut == 1:
                self.compte_bancaire = item.cpt_banquaire