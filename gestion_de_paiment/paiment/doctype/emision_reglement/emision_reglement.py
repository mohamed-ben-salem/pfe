# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
from frappe import msgprint
class EmisionReglement(Document):
	def validate(self):
		compteur = 0
		if self.mode_de_payment == 'Chèque':
				chequier = frappe.get_doc('Chequier', {"account": self.societe})
				if chequier.numero_dernier_cheque == chequier.first_num:
					numero_cheque = chequier.numero_dernier_cheque
				else:
					numero_cheque = chequier.numero_dernier_cheque + 1
				if self.liste_depense:
					for item in self.liste_depense:
						compteur += 1
						if compteur != 1:
							numero_cheque = numero_cheque + 1
						item.num_cheque = numero_cheque
						if compteur == len(self.liste_depense):
							chequier.numero_dernier_cheque = item.num_cheque
						row = chequier.append('cheques_details', {})
						#Set values for the item fields
						row.num_cheque = item.num_cheque
						row.account = self.societe
						row.bank = "BNA"
						row.debit_operation = item.montant_net
						row.credit_operation = '0.00'
						row.type_operation = 'Chéque Emis'
						row.type_ben = item.type_de_tiers
						row.tiers = item.tiers
						row.amount = item.montant_net
						row.date_emission = self.date_emission
						row.depose = 0
						chequier.save()
		for item in self.liste_depense:
			Depenses = frappe.get_doc("Depenses",item.nom_de_la_depense)
			Depenses.mode_de_réglement = self.mode_de_payment
			Depenses
			if Depenses.status == "CREE":
				Depenses.status = "EMISE"
			self.date_emission = today()
			Depenses.numero_de_chéque = item.num_cheque
			Depenses.date_demission = self.date_emission
			Depenses.save()
			cheque = frappe.new_doc("Cheque")
			cheque.num_de_cheque = item.num_cheque
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


