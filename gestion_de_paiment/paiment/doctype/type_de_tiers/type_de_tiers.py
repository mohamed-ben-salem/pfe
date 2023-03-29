# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Typedetiers(Document):
	pass


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def type_tiers(doctype, txt, searchfield, start, page_len, filters):
    cond = ""
    return frappe.db.sql(
        """select name from `tabType de tiers`
            where `{key}` LIKE %(txt)s {cond}
            order by name limit %(page_len)s offset %(start)s""".format(
            key=searchfield, cond=cond),
        {"txt": "%" + txt + "%", "start": start, "page_len": page_len},
    )
        