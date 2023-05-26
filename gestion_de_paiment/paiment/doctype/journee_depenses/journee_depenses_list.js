frappe.listview_settings['Journee depenses'] ={
    get_indicator: function (doc) {
        if (doc.status === "Cloturée") {
            return [("Cloturée"), "green", "status,=,Cloturée"];
        }
        else if (doc.status ==="Non Cloturée") {
            return [("Non Cloturée"), "orange","status,=,Non Cloturée"]
        }
        
    },

    //refresh: function(listview){
		//frappe.route_options = {
			//"status": ["=", "Non Cloturée"]
		//};
	//},

    onload:function(listview){
        function cloturer_journee(){
            
            const selected_docs = listview.get_checked_items();
            if (selected_docs == ''){
                
            frappe.throw("veuillez sélectionner au moin une dépense");}  
            else{
                console.log(selected_docs[0]['status'])
                for (let doc of selected_docs) {
                    if(doc.status!= 'Non Cloturée')
                    frappe.throw("Toutes les dépenses doivent etre à l'etat non cloturée")
                }
                //var doc = frappe.model.get_new_doc("Journee depenses");
                for(var i = 0; i < selected_docs.length ; i++) {  
                    frappe.db.get_doc("Journee depenses",null,{"name":selected_docs[i]['name']})
                    .then(doc => {  
                        frappe.db.set_value('Journee depenses', doc.name, {
                            'status': 'Cloturée',
                        });
                    });
                    
                }
            } 
        }

        listview.page.add_inner_button(__("+ Cloturer"), function () {
            cloturer_journee();
        })
        .addClass("btn-primary");
        listview.refresh();


    }
}