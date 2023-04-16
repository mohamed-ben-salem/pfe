# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Depenses(Document):
    pass
	#def validate(self):
		##self.status ="CREE"
                
	


@frappe.whitelist()
def get_party_bank_account(type_de_tiers, tiers):
    return frappe.db.get_value(type_de_tiers, tiers, "default_bank_account")
