# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
from frappe import msgprint
class EmisionReglement(Document):
	def validate(self):
		for item in self.liste_depense:
			Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
			Depenses.mode_de_réglement = self.mode_de_réglement
			Depenses
			if Depenses.status == "CREE":
				Depenses.status = "EMISE"
			self.date_emission = today()
			Depenses.save()
			cheque = frappe.new_doc("Cheque")
			cheque.num_de_cheque = self.numéro_de_chéque
			cheque.titulaire_du_compte = self.societe
			cheque.benificiare = item.tiers
			cheque.date = self.date_emission
			cheque.montant_net = item.montant_net
			societe = frappe.get_doc("Societe", self.societe)
			compte = frappe.get_doc("Compte bancaire", societe.compte_bancaire)
			cheque.signature = compte.signature
			cheque.date_de_creation_du_compte = compte.date_ouverture
			cheque.numero_du_compte = compte.num_compte
			banque = frappe.get_doc("Banque", compte.banque)
			cheque.adresse_du_agence = banque.adresse_bank
			cheque.telephone_du_agence = banque.phone
			
			

			

			cheque.insert()


