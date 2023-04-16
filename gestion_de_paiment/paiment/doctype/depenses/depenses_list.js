frappe.listview_settings['Depenses'] ={

    get_indicator: function (doc) {
        if (doc.status === "CREE") {
            return [("CREE"), "green", "status,=,CREE"];
        }
        else if  (doc.status ==="VALIDEE") {
            return [("VALIDEE"), "red","status,=,VALIDEE"];
        }
        
    },

   
    
    onload: function (listview) {

        function reglement() {
            var TiersIdentique =[]
            const selected_docs = listview.get_checked_items();
            if (selected_docs == '') {
                frappe.throw("veuillez choisissez au moin une dépense");
            }
            else  for (let doc of selected_docs) {
                
                if (doc.status !='CREE') {
                    frappe.throw("Depense doit être CREE");
                }
                else {
                    var Tiers ={
                        "tiers":doc.tiers,
                        "mode de payment": doc.mode_de_réglement,
                        "devise":doc.devise,
                        

                    }
                    TiersIdentique.push(Tiers);
                    
                   

                }
                console.log(TiersIdentique[0]["tiers"]);

                for (var i=1; i<TiersIdentique.length;i++){
                    
                    if (TiersIdentique[0]["tiers"] != TiersIdentique[i]["tiers"]) {
                        frappe.throw("il faut ont les memes nom");
                    }

                    if (TiersIdentique[0]["mode de payment"] != TiersIdentique[i]["mode de payment"]) {
                        frappe.throw("il faut ont les mode de payment");
                    }

                    if (TiersIdentique[0]["devise"] != TiersIdentique[i]["devise"]) {
                        frappe.throw("il faut ont les devise");
                    }
                    
                    
                }
            }
            

          
        }

        
        
        listview.page.add_inner_button(__("+ Reglement"), function () {
            reglement();
            frappe.new_doc('Emision Reglement', ) 
        })
        .addClass("btn-primary");
        
        listview.refresh();
                
},

}










