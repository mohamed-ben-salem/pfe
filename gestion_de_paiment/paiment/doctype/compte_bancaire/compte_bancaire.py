# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Comptebancaire(Document):
	def on_update(self):
            if self.type_du_compte == "Compte courant":
                if self.type_de_tiers == 'Fournisseur':
                    Fournisseur = frappe.get_doc("Fournisseur",self.tiers)
                    row=Fournisseur.append("ribs", {})
                    row.rib=self.rib
                    row.banque = self.banque
                    row.cpt_banquaire = self.nom_compte
                    Fournisseur.save()

                elif self.type_de_tiers == 'Client':
                    Client = frappe.get_doc("Client",self.tiers)
                    row=Client.append("ribs", {})
                    row.rib=self.rib
                    row.banque = self.banque
                    row.cpt_banquaire = self.nom_compte
                    Client.save()

            elif self.type_du_compte == "Compte bancaire pour entreprise":

                Societe = frappe.get_doc("Societe",self.societe)
                row=Societe.append("ribs", {})
                row.rib=self.rib
                row.banque = self.banque
                row.cpt_banquaire = self.nom_compte
                Societe.save()

            
            
@frappe.whitelist()
def get_party_bank_account(type_de_tiers, tiers):
    return frappe.db.get_value(type_de_tiers, tiers, "default_bank_account")



   