// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.ui.form.on('Compte bancaire', {
    setup: function(frm) {
        frm.set_query("type_de_tiers", function() {
            return {
                query: "gestion_de_paiment.paiment.doctype.type_de_tiers.type_de_tiers.type_tiers"
            };
        });
    },
});

