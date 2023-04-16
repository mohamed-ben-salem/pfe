// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.ui.form.on('Emision Reglement', {
    societe: function(frm){
        var items = []
        if(frm.doc.societe) {
            frappe.model.with_doc("Societe", frm.doc.societe, function() {
                var table_transfer = frappe.model.get_doc("Societe", frm.doc.societe)
                $.each(table_transfer.ribs, function(index, row){
                    var item = {
                        "rib" : row.rib,
                        "banque" : row.banque,
                        "compte_bancaire" : row.cpt_banquaire,
                        "par_defaut" : row.par_defaut

                    }
                    items.push(item)
                });
                console.log(items)
                frm.set_value("ribss", items);
                frm.refresh_field("ribss");
            });  
            items = [];
        }
    }

});
	

