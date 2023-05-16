# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document


class Modeledecheque(Document):
	pass



@frappe.whitelist()
def create_or_update_modele_du_cheque(template_name):
	if not frappe.db.exists("Print Format", template_name):
		cheque_print = frappe.new_doc("Print Format")
		cheque_print.update(
			{
				"doc_type": "Cheque",
				"standard": "No",
				"custom_format": 1,
				"print_format_type": "Jinja",
				"name": template_name,
			}
		)
	else:
		cheque_print = frappe.get_doc("Print Format", template_name)

	doc = frappe.get_doc("Modele de cheque", template_name)

	cheque_print.html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500&display=swap');	.print-format {
		padding: 0px;
	}
	@media screen {
		.print-format {
			padding: 0in;
		}
	}
	@font-face {
        font-family: 'myFont';
        src: url('/CMC7____.TTF') format('TTF');
    }
	.cmc7 {
		font-family: 'cmc7';
	}
	.print-format p{
	margin:3px 0px 14px;
	text-align: justify;
	font-size:13px;
	}
	legend{
		border:none;
		margin-bottom:0px;
	}
	

</style>
<div style="position: relative;">
	<div style="position:relative; padding:30px; top:80px;">
		<p>Date: <strong>{{doc.date}}</strong><br>
		À <strong>{{doc.benificiare}}</strong><br>
		<strong>{{doc.adresse_du_agence}}</strong>
		</p>
		
		
		<p><strong>Objet : Émission d'un chèque</strong></p>
		<p>Madame, Monsieur,</p>
		<p>Je soussigné(e) <strong>{{doc.titulaire_du_compte}}</strong>, titulaire du compte n°<strong> {{doc.numero_du_compte}}</strong>, demande l'émission d'un chèque d'un montant de <strong>{{frappe.utils.money_in_words(doc.montant_net)}}</strong> (en chiffres : {{doc.montant_net}} TND).</p>
		<p>Le bénéficiaire du chèque est <strong>{{doc.benificiare}}</strong>, et l'objet de ce chèque est [précisez l'objet du chèque, par exemple "paiement de facture"].</p>
		<p>Je vous prie de bien vouloir débiter mon compte du montant de ce chèque et de l'envoyer directement au bénéficiaire à l'adresse suivante : <strong>{{doc.lieu}}</strong>.</p>
		<p>Je vous remercie de votre attention et vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.</p>
		<p>Signature : <img src = {{doc.signature}} style="max-width:250px;"/></p>
		<p><strong>{{doc.titulaire_du_compte}}</strong></p>
	</div>
		<div style="position: relative;top: %(a4_supp)scm; left:1.5cm;" >
    <div style="position: relative; height: 8cm;width:17.7cm;">
        <div style="width:  %(largeur_du_cheque)s cm; 
            height: %(hauteur_du_cheque)s cm;">
            <img src="%(logo)s "style="position: absolute; left: %(logo_gauche)scm; bottom: %(logo_inf)scm;"/>
            <span style="top:%(num_supp)scm;
            left: %(num_gauche)scm;
            position: absolute; font-weight:bolder;"> {{doc.num_de_cheque}} </span>
            <span style="top:0.9cm;
            left: 0.3cm;
            position: absolute; font-size: x-small; letter-spacing:0.8px">عدد الصك</span>
            <span style="top:1.18cm;
            left: 0.3cm;
            position: absolute;font-size: x-small;">Nº du cheque </span>
            <span style="top:0.9cm;
            left: 12.5cm;
            position: absolute;font-size: 8px;">B.P.D</span>
            <span style="top:%(chiff_sup)scm;
            left: %(chiff_gauche)scm;
            position: absolute; font-weight: bold;"> {{doc.montant_net}} TND²</span>
            <span style="top:0.9cm;
            left: 17.1cm;
            position: absolute;font-size: x-small;">م.د</span>
            <span style="top:2.19cm;
            left: 0.3cm;
            position: absolute; font-size:10.7px;">Payer contre ce chèque non endossable</span>
            <span style="top:2.55cm;
            left: 0.3cm;
            position: absolute;font-size: 8px;">Sauf au profit d une banque d un organisme assimilé</span>
            <span style="top:%(lettre_supp)scm;
            left: %(lettre_gauche)scm;
            position: absolute;
            width: auto;
            line-height:%(line_spacing_for_amount_in_words)scm;
            font-weight: bold; font-size : 10px;" > {{frappe.utils.money_in_words(doc.montant_net)}}</span>
            <span style="top:2.2cm;
            left: 13cm;
            position: absolute;font-size:10px;width:4.8cm;">إدفعوا مقابل هذا الصك غير القابل للتّظهير</span>
            <span style="top:2.55cm;
            left: 13.3cm;
            position: absolute;font-size:10px; letter-spacing: 0.25px;">إلاّ لفائدة مصرف أو مؤثة ماليّة مماثلة</span>
            <span style="top:3.5cm;
            left: 0.3cm;
            position: absolute;font-size:10.7px;">A l ordre de</span>
            <span style="top:%(ben_supp)scm;
            left: %(ben_gauche)scm;
            position: absolute;font-size:12.5px; font-weight: bold;">{{doc.benificiare}}</span>
            <span style="top:3.5cm;
            left: 16.9cm;
            position: absolute;font-size:11px;">لأمر</span>
            <fieldset style="position:absolute; top:%(filedset_pay_supp)scm; left:%(filedset_pay_gauche)scm; text-align: center;width: 3.5cm; height: 2.1cm; border: 0.5px solid;">
            <legend style="font-size: 9px;padding: 0 5px; bottom:%(payable_supp)scm; left:%(payable_gauche)scm; width:auto; position:absolute; background-color:white;margin:0px ">Payable à  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp يدفع بـ</legend>
            <div style="position:absolute; bottom:3px; left:30px;">
                <span style=" margin-top: 0.1cm;bottom:%(add_supp)scm; left:%(add_gauche)scm; position:absolute">{{doc.adresse_du_agence}}</span>
                <span style="left: %(tel_gauche)scm; bottom:%(tel_supp)scm;position: absolute;">{{doc.telephone_du_agence}}</span>
                <span style="left: %(date_cpt_gauche)scm; bottom: %(date_cpt_supp)scm;position: absolute; width: 67px;">{{doc.date_de_creation_du_compte}}</span>
            </div>
            </fieldset>
            <fieldset style="position:absolute; top:%(payable_f_supp)scm;left:%(payable_f_gauche)scm; width: 7.2cm;height:1.9cm; text-align: center; border: 0.5px solid; " ">
                <legend style="font-size: 9px;  width: 200px; padding: 0 5px;position:absolute; left:%(legend_pay_gauche)scm; bottom:%(legend_pay_supp)scm; background-color:white"> Titulaire du compte  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp صاحب الحساب</legend>
                <legend style="font-size: x-small;  width: auto; padding: 0 5px; top:%(legend_le_supp)scm;position:absolute;left:%(legend_le_gauche)scm"> <span style="background-color: white;">le</span></legend>
                <legend style="font-size: x-small; position: absolute;   right: %(legend_a_droit)scm;top:%(legend_a_supp)scm;padding: 0 5px;background: white;width:auto"> <span style="background-color: white;">A</span></legend>
                <legend style=" font-size: x-small; position: absolute;   left: %(legend_fi_gauche)scm;top: %(legend_fi_supp)scm; padding: 0 5px;background: white;width:auto;"> <span style="background-color:white">في</span></legend>
                <legend style=" font-size: x-small; position: absolute;   left: %(legend_bi_gauche)scm; top: %(legend_bi_supp)scm;padding: 0 5px;width:auto; background-color:white;"> <span style=" background-color: white;">بـ</span></legend>
                <span style="padding-top:0.6cm; background-color:white;right:3.52cm;  top:1.2cm; position:relative">&nbsp</span>
                <span style="padding-top:0.6cm; background-color:white;left:3.52cm; top:1.2cm; position:relative">&nbsp</span>
                    <div style="position:absolute; bottom:13px; left:70px;">
                        <span style="  margin-top: 0.3cm; top:%(num_cpt_supp)scm; left:%(num_cpt_gauche)scm" > {{doc.numero_du_compte}}</span>
                        <span style="position: absolute; bottom:%(nom_supp)scm; left:%(nom_gauche)scm; width : 200px;"> {{doc.titulaire_du_compte}} </span></div>
                        <span style="position:absolute;top:%(lieu_supp)scm;left:%(lieu_gauche)scm;">{{doc.lieu}}</span>
                        <span style="position:absolute;top:%(date_supp)scm;left:%(date_gauche)scm;">{{doc.date}}</span>
                        <span style="position:absolute;top:%(maken_supp)scm;left:%(maken_gauche)scm;">{{doc.المكان}}</span>
            </fieldset>
                <fieldset style="position:absolute; top:%(container_sign_supp)scm;left:%(container_sign_gauche)scm; width: 5.6cm;height:2.1cm; text-align: center; border: 0.5px solid;">
                    <legend style="font-size: 9px;  width: auto; padding: 0 6px; margin:0 10px;position:absolute;left:%(legend_sign_gauche)scm; background-color:white; bottom:%(legend_sign_supp)scm"> Signature (s)s &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp الإمضاء</legend>
                    <div style="position:relative;top:%(sign_supp)scm; left:%(sign_gauche)scm" > 
                        <img src={{doc.signature}} />
                    </div>
                </fieldset>
                <span style="position: absolute; left:1.3cm ; top: 7.1cm; ">
                    <p class="cmc7">[{{doc.num_de_cheque}}1{{doc.numero_du_compte[:5]}}]{{doc.numero_du_compte[5:]}}{</p> 
                </span>
        </div>
    </div>
</div>

	</div>""" % {
		"largeur_du_cheque": doc.largeur_du_cheque,
		"hauteur_du_cheque": doc.hauteur_du_cheque,
		"logo_inf": doc.logo_inf,
		"logo_gauche": doc.logo_gauche,
		"logo":doc.logo,
		"num_supp": doc.num_supp,
		"num_gauche": doc.num_gauche,
		"chiff_sup": doc.chiff_sup,
		"chiff_gauche": doc.chiff_gauche,
		"lettre_supp": doc.lettre_supp,
		"lettre_gauche": doc.lettre_gauche,
		"largeur_du_montant_en_mot": doc.largeur_du_montant_en_mot,
		"line_spacing_for_amount_in_words": doc.line_spacing_for_amount_in_words,
		"ben_supp": doc.ben_supp,
		"ben_gauche": doc.ben_gauche,
		"sign_supp": doc.sign_supp,
		"sign_gauche": doc.sign_gauche,
		"add_supp": doc.add_supp,
		"add_gauche": doc.add_gauche,
		"tel_supp": doc.tel_supp,
		"tel_gauche": doc.tel_gauche,
		"date_cpt_supp": doc.date_cpt_supp,
		"date_cpt_gauche": doc.date_cpt_gauche,
		"num_cpt_supp": doc.num_cpt_supp,
		"num_cpt_gauche": doc.num_cpt_gauche,
		"nom_supp": doc.nom_supp,
		"nom_gauche": doc.nom_gauche,
		"lieu_supp": doc.lieu_supp,
		"lieu_gauche": doc.lieu_gauche,
		"date_supp": doc.date_supp,
		"date_gauche": doc.date_gauche,
		"a4_supp":doc.a4_supp,
		"legend_bi_gauche":doc.legend_bi_gauche,
		"legend_bi_supp":doc.legend_bi_supp,
		"legend_fi_gauche":doc.legend_fi_gauche,
		"legend_fi_supp":doc.legend_fi_supp,
		"legend_le_gauche":doc.legend_le_gauche,
		"legend_le_supp":doc.legend_le_supp,
		"legend_a_droit":doc.legend_a_droit,
		"legend_a_supp":doc.legend_a_supp,
		"legend_pay_gauche":doc.legend_pay_gauche,
		"legend_pay_supp":doc.legend_pay_supp,
		"filedset_pay_gauche":doc.filedset_pay_gauche,
		"filedset_pay_supp":doc.filedset_pay_supp,
		"payable_f_supp":doc.payable_f_supp,
		"payable_f_gauche":doc.payable_f_gauche,
		"container_sign_supp":doc.container_sign_supp,
		"container_sign_gauche":doc.container_sign_gauche,
		"legend_sign_supp":doc.legend_sign_supp,
		"legend_sign_gauche":doc.legend_sign_gauche,
		"payable_supp":doc.payable_supp,
		"payable_gauche":doc.payable_gauche,
		"payable_f_supp":doc.payable_f_supp,
		"payable_f_gauche":doc.payable_f_gauche,
		"maken_supp":doc.maken_supp,
		"maken_gauche":doc.maken_gauche,
		"cmc7_supp":doc.cmc7_supp,
		"cmc7_gauche":doc.cmc7_gauche,
	}

	cheque_print.save(ignore_permissions=True)

	frappe.db.set_value("Modele de cheque", template_name, "check", 1)

	return cheque_print
