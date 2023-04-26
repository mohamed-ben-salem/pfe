frappe.listview_settings['importTest'] ={
    onload: function(listview) {
    listview.page.add_inner_button(__("import"), function () {
        listview.page.set_primary_action(__("Import data"), function () {
            listview.import_test();
        });
        frappe.new_doc('Data Import', ) 
    })
    .addClass("btn-primary");
}
}