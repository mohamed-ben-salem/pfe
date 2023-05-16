// Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
// For license information, please see license.txt

frappe.provide("erpnext.cheque_print");

frappe.ui.form.on('Modele de cheque', {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(frm.doc.check?__("Update Print Format"):__("Create Print Format"),
				function() {
					erpnext.cheque_print.view_cheque_print(frm);
				}).addClass("btn-primary");

			$(frm.fields_dict.cheque_print_preview.wrapper).empty()
			

			var template ='<div style="position: relative; overflow-x: scroll;">\
			<div style="position: relative; height: 8cm;width:17.7cm;">\
			<div style="width: {{ largeur_du_cheque }}cm; \
				height: {{ hauteur_du_cheque }}cm;">\
				<img src="{{logo}}" style="position: absolute; left: {{logo_gauche}}cm; bottom: {{logo_inf}}cm;"/>\
				<span style="top:{{num_supp}}cm;\
                left: {{num_gauche}}cm;\
                position: absolute; font-weight:bolder;"class="color"> 7204237 </span>\
				<span style="top:0.9cm;\
                left: 0.3cm;\
                position: absolute; font-size: x-small; letter-spacing:0.8px">عدد الصك</span>\
				<span style="top:1.18cm;\
                left: 0.3cm;\
                position: absolute;font-size: x-small;">Nº du cheque </span>\
				<span style="top:0.9cm;\
                left: 12.5cm;\
                position: absolute;font-size: 8px;">B.P.D</span>\
				<span style="top:{{chiff_sup}}cm;\
                left: {{chiff_gauche}}cm;\
                position: absolute; font-weight: bold;"> Montant en chiffre</span>\
				<span style="top:0.9cm;\
                left: 17.1cm;\
                position: absolute;font-size: x-small;">م.د</span>\
				<span style="top:2.19cm;\
                left: 0.3cm;\
                position: absolute; font-size:10.7px;">Payer contre ce chèque non endossable</span>\
				<span style="top:2.55cm;\
                left: 0.3cm;\
                position: absolute;font-size: 8px;">Sauf au profit d une banque d un organisme assimilé</span>\
				<span style="top:{{lettre_supp}}cm;\
                left: {{lettre_gauche}}cm;\
                position: absolute;\
                width: {{largeur_du_montant_en_mot}}cm;\
                line-height:{{line_spacing_for_amount_in_words}} cm;\
                font-weight: bold;" > Montant en lettre</span>\
				<span style="top:2.2cm;\
                left: 13cm;\
                position: absolute;font-size:10px;width:4.8cm;">إدفعوا مقابل هذا الصك غير القابل للتّظهير</span>\
				<span style="top:2.55cm;\
                left: 13.3cm;\
                position: absolute;font-size:10px; letter-spacing: 0.25px;">إلاّ لفائدة مصرف أو مؤثة ماليّة مماثلة</span>\
				<span style="top:3.5cm;\
                left: 0.3cm;\
                position: absolute;font-size:10.7px;">A l ordre de</span>\
				<span style="top:{{ben_supp}}cm;\
                left: {{ben_gauche}}cm;\
                position: absolute;font-size:12.5px; font-weight: bold;">Bénéficiaire</span>\
				<span style="top:3.5cm;\
                left: 16.9cm;\
                position: absolute;font-size:11px;">لأمر</span>\
				<fieldset style="position:absolute; top:{{filedset_pay_supp}}cm; left:{{filedset_pay_gauche}}cm; text-align: center;width: 3.5cm; height: 2.1cm; border: 0.5px solid;">\
                <legend style="font-size: 9px; bottom:{{payable_supp}}cm; left:{{payable_gauche}}cm; width:auto; position:absolute; background-color:white;margin:0px ">Payable à  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp يدفع بـ</legend>\
				<div style="position:absolute; bottom:3px; left:30px;">\
					<span style="margin-top: 0.1cm;bottom:{{add_supp}}cm; left:{{add_gauche}}cm; position:absolute">Adresse</span>\
					<span style="left: {{tel_gauche}}cm; bottom:{{tel_supp}}cm;position: absolute;">Telephone</span><br>\
					<span style="left: {{date_cpt_gauche}}cm; bottom: {{date_cpt_supp}}cm;position: absolute;">date</span>\
				</div>\
				</fieldset>\
				<fieldset style="position:absolute; top:{{payable_f_supp}}cm;left:{{payable_f_gauche}}cm; width: 7.2cm;height:1.9cm; text-align: center; border: 0.5px solid; " ">\
					<legend style="font-size: 9px;  width: 200px; padding: 0 5px;position:absolute; left:{{legend_pay_gauche}}cm; bottom:{{legend_pay_supp}}cm; background-color:white"margin-bottom:0px;> Titulaire du compte  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp صاحب الحساب</legend>\
					<legend style="font-size: x-small;  width: auto; padding: 0 5px; top:{{legend_le_supp}}cm;position:absolute;left:{{legend_le_gauche}}cm"> <span style="background-color: white;">le</span></legend>\
					<legend style="font-size: x-small; position: absolute;   right: {{legend_a_droit}}cm;top:{{legend_a_supp}}cm;padding: 0 5px;background: white;width:auto"> <span style="background-color: white;">A</span></legend>\
					<legend style=" font-size: x-small; position: absolute;   left: {{legend_fi_gauche}}cm;top: {{legend_fi_supp}}cm;padding: 0 5px;background: white;width:auto;"> <span style="background-color:white">في</span></legend>\
					<legend style=" font-size: x-small; position: absolute;   left: {{legend_bi_gauche}}cm; top: {{legend_bi_supp}}cm;padding: 0 5px;width:auto; background-color:white;"> <span style=" background-color: white;">بـ</span></legend>\
					<span style="padding-top:0.6cm; background-color:white;right:3.52cm;  top:1.2cm; position:relative">&nbsp</span>\
					<span style="padding-top:0.6cm; background-color:white;left:3.52cm; top:1.2cm; position:relative">&nbsp</span>\
						<div style="position:absolute; bottom:13px; left:70px;">\
							<span style="margin-top: 0.3cm; top:{{num_cpt_supp}}cm; left:{{num_cpt_gauche}}cm" > Numero du compte</span>\
							<span style="position: absolute; bottom:{{nom_supp}}cm; left:{{nom_gauche}}cm"> Nom et Prenom </span></div>\
							<span style="position:absolute;top:{{lieu_supp}}cm;left:{{lieu_gauche}}cm;">Lieu</span>\
							<span style="position:absolute;top:{{date_supp}}cm;left:{{date_gauche}}cm;">Date</span>\
							<span style="position:absolute;top:{{maken_supp}}cm;left:{{maken_gauche}}cm;">المكان</span>\
				</fieldset>\
					<fieldset style="position:absolute; top:{{container_sign_supp}}cm;left:{{container_sign_gauche}}cm; width: 5.6cm;height:2.1cm; text-align: center; border: 0.5px solid;">\
						<legend style="font-size: 9px;  width: auto; padding: 0 6px; margin:0 10px;position:absolute;left:{{legend_sign_gauche}}cm; background-color:white; bottom:{{legend_sign_supp}}cm"> Signature (s) &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp الإمضاء</legend>\
						<div style="position:relative;top:{{sign_supp}}cm; left:{{sign_gauche}}cm" > Signature</div></fieldset>\
						<span style="position: absolute; left:1.3cm ; top: 7.1cm; ">\
						<p class="cmc7">64512168415</p> \
					</span>\
			</div>\
		</div>\
		</div>';

			$(frappe.render(template, frm.doc)).appendTo(frm.fields_dict.cheque_print_preview.wrapper)
		}
	}
});

erpnext.cheque_print.view_cheque_print = function(frm) {
	frappe.call({
		method: "gestion_de_paiment.paiment.doctype.modele_de_cheque.modele_de_cheque.create_or_update_modele_du_cheque",
		args:{
			"template_name": frm.doc.name
		},
		callback: function(r) {
			if (!r.exe && !frm.doc.check) {
				var doc = frappe.model.sync(r.message);
				frappe.set_route("Form", r.message.doctype, r.message.name);
			}
			else {
				frappe.msgprint(__("Print settings updated in respective print format"))
			}
		}
	})
}
