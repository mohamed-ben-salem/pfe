# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Comptebancaire(Document):
	pass



@frappe.whitelist()
def get_party_bank_account(type_de_tiers, tiers):
    return frappe.db.get_value(type_de_tiers, tiers, "default_bank_account")