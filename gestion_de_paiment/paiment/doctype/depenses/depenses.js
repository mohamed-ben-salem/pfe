// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.ui.form.on('Depenses', {
	
	setup: function(frm) {
        frm.set_query("type_de_tiers", function() {
            return {
                query: "gestion_de_paiment.paiment.doctype.type_de_tiers.type_de_tiers.type_tiers"
            };
        });
    },

	tiers: function(frm){
        var items = []
        if(frm.doc.type_de_tiers == 'Fournisseur') {
            frappe.model.with_doc("Fournisseur", frm.doc.tiers, function() {
                var TabFournisseur= frappe.model.get_doc("Fournisseur", frm.doc.tiers)
                $.each(TabFournisseur.ribs, function(index, row){
                    var item = {
                        "rib" : row.rib,
                        "banque" : row.banque,
                        "compte_bancaire" : row.cpt_banquaire,
                        "par_defaut" : row.par_defautG
                    }
                    items.push(item)
                });
                frm.set_value("ribss", items);
                frm.refresh_field("ribss");
            });  
            
            items = [];
        } 
        else if (frm.doc.type_de_tiers == 'Client') {
            frappe.model.with_doc("Client", frm.doc.tiers, function() {
                var TabClient= frappe.model.get_doc("Client", frm.doc.tiers)
                $.each(TabClient.ribs, function(index, row){
                    var item = {
                        "rib" : row.rib,
                        "banque" : row.banque,
                        "compte_bancaire" : row.cpt_banquaire,
                        "par_defaut" : row.par_defaut
                    }
                    items.push(item)
                });
                frm.set_value("ribss", items);
                frm.refresh_field("ribss");
            }); 
            items = [];
        }
    }

	
})


