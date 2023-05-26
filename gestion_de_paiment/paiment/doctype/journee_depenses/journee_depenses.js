// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.ui.form.on('Journee depenses', {
	refresh: function(frm) {
		frm.add_custom_button(__('Cloturer'), function() {
			frm.set_value('status', 'Cloturée');
            frm.save();
		})
		.addClass("btn-primary");

	}
});