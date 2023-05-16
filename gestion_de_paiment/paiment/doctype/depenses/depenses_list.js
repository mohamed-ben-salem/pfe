frappe.listview_settings['Depenses'] ={

  get_indicator: function (doc) {
      if (doc.status === "CREE") {
          return [("CREE"), "green", "status,=,CREE"];
      }
      else if  (doc.status ==="VALIDEE") {
          return [("VALIDEE"), "blue","status,=,VALIDEE"];
      }
      else if (doc.status ==="EMISE") {
          return [("EMISE"), "orange","status,=,EMISE"]
      }
      
  },

  
  
  onload: function (listview) {

    function reglement() {
      var TiersIdentique =[]
      var items_P=[]
      const selected_docs = listview.get_checked_items();
      if (selected_docs == '') 
        frappe.throw("veuillez choisissez au moin une dépense");
      else{
        for (let doc of selected_docs) {
          if (doc.status !='CREE') 
            frappe.throw("Depense doit être CREE");
          else {
          var Tiers ={
            "tiers":doc.tiers,
            "devise":doc.devise,
          }
          TiersIdentique.push(Tiers);
          }
            
          for (var i=1; i<TiersIdentique.length;i++){          
            /*if (TiersIdentique[0]["tiers"] != TiersIdentique[i]["tiers"]) 
              frappe.throw("il faut ont les memes nom");*/
                  
            if (TiersIdentique[0]["devise"] != TiersIdentique[i]["devise"]) 
              frappe.throw("il faut ont les devise");
                      
          }
        }
        var docn = frappe.model.get_new_doc("Emision Reglement");
        for(var i = 0; i < selected_docs.length ; i++) {    
          frappe.call({
            method: "frappe.client.get_value",
            async: false,
            args: {
              doctype: "Depenses",
              filters: {"nom_de_la_depense": selected_docs[i]['nom_de_la_depense']},
              fieldname: ["type_de_tiers", "tiers", "montant_net","devise", "mode_de_réglement", "service_émetteur_de_la_dépense","nature_de_dépense","status"]
            },
            callback: function(r) {   
              var item_P= {
                'nom_de_la_depense' : selected_docs[i]['nom_de_la_depense'],
                'montant_net' : r.message["montant_net"],
                'type_de_tiers' : r.message["type_de_tiers"],
                'tiers' : r.message["tiers"],
                'devise' : r.message["devise"],
                'mode_de_réglement' :r.message["mode_de_réglement"],
                'nature_de_dépense' :r.message["nature_de_dépense"],
                'service_émetteur_de_la_dépense':r.message["ervice_émetteur_de_la_dépense"],
                'status': r.message["status"],
                'numéro_de_chéque': '',
                'date_emission': ''
              };
              items_P.push(item_P);
            }
          });                       
        }
        
      }
      console.log(items_P); 
      docn.liste_depense = items_P;
      items_P = [];
      frappe.set_route('Form','Emision Reglement',docn.name);
    }

    function emis() {
      var itemx_P=[]
      const selected_docs = listview.get_checked_items();
      if (selected_docs == '') 
        frappe.throw("veuillez choisissez au moin une dépense");
      else{
        for (let doc of selected_docs) {
          if (doc.status !='EMISE') 
          frappe.throw("Depense doit être EMISE");
        }
        var doc = frappe.model.get_new_doc("Validation Reglement Emis");
        for(var i = 0; i < selected_docs.length ; i++) {    
          frappe.call({
            method: "frappe.client.get_value",
            async: false,
            args: {
              doctype: "Depenses",
              filters: {"nom_de_la_depense": selected_docs[i]['nom_de_la_depense']},
              fieldname: ["type_de_tiers", "tiers", "montant_net","devise", "mode_de_réglement", "service_émetteur_de_la_dépense","nature_de_dépense","status"]
            },
            callback: function(r) {   
              var item_P= {
                'nom_de_la_depense' : selected_docs[i]['nom_de_la_depense'],
                'montant_net' : r.message["montant_net"],
                'type_de_tiers' : r.message["type_de_tiers"],
                'tiers' : r.message["tiers"],
                'devise' : r.message["devise"],
                'mode_de_réglement' :r.message["mode_de_réglement"],
                'nature_de_dépense' :r.message["nature_de_dépense"],
                'service_émetteur_de_la_dépense':r.message["ervice_émetteur_de_la_dépense"],
                'status': r.message["status"],
                'date_de_validation': ''
              };
              itemx_P.push(item_P);
            }
          });                       
        }
        
      }
      console.log(itemx_P); 
      doc.liste_de_dépenses_emis= itemx_P;
      itemx_P = [];
      frappe.set_route('Form','Validation Reglement Emis',doc.name);
    };




    function edition_journee() {
      var itemt_P=[]
      const selected_docs = listview.get_checked_items();
      if (selected_docs == '') 
        frappe.throw("veuillez choisissez au moin une dépense");
      else{
        for (let doc of selected_docs) {
          if (doc.status !='VALIDEE') 
          frappe.throw("Depense doit être VALIDEE");
        }
        var doc = frappe.model.get_new_doc("Journee depenses");
        for(var i = 0; i < selected_docs.length ; i++) {    
          frappe.call({
            method: "frappe.client.get_value",
            async: false,
            args: {
              doctype: "Depenses",
              filters: {"nom_de_la_depense": selected_docs[i]['nom_de_la_depense']},
              fieldname: ["type_de_tiers", "tiers", "montant_net","devise", "mode_de_réglement", "service_émetteur_de_la_dépense","nature_de_dépense","status"]
            },
            callback: function(r) {   
              var item_P= {
                'nom_de_la_depense' : selected_docs[i]['nom_de_la_depense'],
                'montant_net' : r.message["montant_net"],
                'type_de_tiers' : r.message["type_de_tiers"],
                'tiers' : r.message["tiers"],
                'devise' : r.message["devise"],
                'mode_de_réglement' :r.message["mode_de_réglement"],
                'nature_de_dépense' :r.message["nature_de_dépense"],
                'service_émetteur_de_la_dépense':r.message["ervice_émetteur_de_la_dépense"],
                'status': r.message["status"],
                'date_de_cloture': ''
                //'date_de_validation':r.message["date_de_validation"],
                //'date_emission':r.message["date_emission"],
               // 'référence_du_virement': '',
                //'numéro_de_chéque': '',
              };
              itemt_P.push(item_P);
            }
          });                       
        }
        
      }
      //doc.status = 'Non Cloturée';
      doc.liste_depenses_validee = itemt_P;
      //doc.date_de_cloture = ''
      itemt_P = [];
      frappe.set_route('Form','Journee depenses',doc.name);
    };


      
      
    listview.page.add_inner_button(__("+ Reglement"), function () {
        reglement();
    })
    .addClass("btn-primary");

    listview.page.add_inner_button(__("+ Reglement Emis"), function () {
        emis();
        frappe.new_doc('Validation Reglement Emis', ) 
    })
    .addClass("btn-primary");

    listview.page.add_inner_button(__("+ Edition Journee Depenses"), function () {
      edition_journee();
    })
    .addClass("btn-primary");
    
    listview.page.add_inner_button(__("+ Annuler"), function () {
      annuler();
    })
    .addClass("btn-primary");
    
    listview.refresh();
  },
}










