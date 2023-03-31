// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fournisseur', {
	 refresh: function(frm) {
		frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "Compte Bancaire",
                filters: {"fournisseur": frm.doc.name},
                fieldname: "numero_compte_bancaire"
            },
            callback: function(r) {
                if(r.message) {
                    frm.set_value("numero_du_compte_bancaire", r.message.numero_compte_bancaire);
                }
            }
        });

	 }
});
