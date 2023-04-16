# Copyright (c) 2023, Mohamed Ben Salem && Samar Othmeni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Banque(Document):
	def validate(self):

		if self.nom_bank.upper() == 'STB':
			self.code_bank = '10'
			self.bicswift = 'TSIDTNTT'
			self.site_web='www.stb.com.tn'
			self.adresse_email ='Stb@Stb.Com.Tn'
			self.phone = '70 140 000'

		elif self.nom_bank.upper() == 'BCT':
			self.code_bank = '00'
			self.bicswift = 'CCIOCRS'
			self.site_web='https://www.bct.gov.tn/bct/siteprod/index.jsp'
			self.adresse_email ='boc@bct.gov.tn'
			self.phone='71 122 000'

		if self.nom_bank.upper() == 'ATB':
			self.code_bank = '01'
			self.bicswift = 'ATBKTNTT'
			self.site_web='www.atb.com.tn'
			self.adresse_email ='contact@atb.com.tn'
			self.phone='71 351 155'

		elif self.nom_bank.upper() == 'BFT':
			self.code_bank = 'BFTNTNTT'
			self.code_bank = '02'
			

		if self.nom_bank.upper() == 'BNA':
			self.code_bank = '03'
			self.bicswift = 'BNTETNTT'
			self.site_web='www.bna.com.tn'
			self.adresse_email ='www.bna.com.tn'
			self.phone='71 831 000 / 71 831 200'

		elif self.nom_bank.upper() == 'BS':
			self.code_bank = '04'
			self.bicswift = 'RBABCH22'
			self.site_web='www.attijaribank.com.tn'
			self.adresse_email ='relation.client@attijaribank.com.tn'
			self.phone='71 111 300.'

		if self.nom_bank.upper() == 'BT':
			self.code_bank = '05'
			self.bicswift = 'BTBKTNTT'
			self.site_web='www.bt.com.tn'
			self.adresse_email ='callcenter@bt.com.tn'
			self.phone='81 101 212'

		elif self.nom_bank.upper() == 'BIAT':
			self.code_bank = '08'
			self.bicswift = 'BIATTNTT'
			self.site_web='www.biat.com.tn'
			self.adresse_email ='tre@biat.com.tn'
			self.phone='71 131 000 / 31 311 000'

		elif self.nom_bank.upper() == 'BTS':
			self.code_bank = '76'
			self.bicswift='TUSOTNT1'
			self.site_web='www.bts.com.tn'
			self.adresse_email ='bts@bts.com.tn'
			self.phone='70 018 424'

		elif self.nom_bank.upper() == 'UBCI':
			self.code_bank = 'UBCIT'
			self.code_bank = 'UBCITNTT'
			self.site_web='www.ubci.tn'
			self.adresse_email ='bensalah.slaheddine@apbt.org.tn'
			self.phone='70 000 050 '

		elif self.nom_bank.upper() == 'UIB':
			self.code_bank = '12'
			self.bicswift = 'UIBKTNTT'
			self.site_web='www.uib.com.tn'
			self.adresse_email ='uibcontact@uib.com.tn'
			self.phone='81 102 525 / 71 850 248'

		elif self.nom_bank.upper() == 'BH':
			self.code_bank = '14'
			self.bicswift = 'BHBKTNTT'
			self.site_web='www.bh.com.tn'
			self.adresse_email ='contact@bhbank.tn'
			self.phone='71 126 000'

		elif self.nom_bank.upper() == 'BTK':
			self.code_bank = '20'
			self.bicswift = 'BTKOTNTT'
			self.site_web='www.btknet.com'
			self.adresse_email ='satisfaction.client@btknet.com'
			self.phone='80 101 652'

		elif self.nom_bank.upper() == 'QNB':
			self.code_bank = '23'
			self.bicswift = 'QNBAQAQASLB'
			self.site_web='www.qnb.com.tn'
			self.adresse_email ='bellil@tqb.com.tn'
			self.phone='36 004 000'

		elif self.nom_bank.upper() == 'BZ':
			self.code_bank = '25'
			self.bicswift = 'BZBKCH2W'
			self.site_web='www.banquezitouna.com'
			self.adresse_email ='contact@banquezitouna.com'
			self.phone='81 105 555'

		elif self.nom_bank.upper() == 'BTL':
			self.code_bank = '26'
			self.bicswift = 'ATLDTNTT'
			self.site_web='www.btl.com.tn'
			self.adresse_email =' btl@gnet.tn'
			self.phone='70 131 700'
		
		
		
		if self.code_agence is None:
			pass
		elif len(self.code_agence) == 3:
			self.bicswift = self.bicswift + self.code_agence
		elif not self.code_agence:
			pass
		else:
			frappe.throw('code agence se compose de 3 chiffres')
		
		if self.iban is None:
			pass
		elif self.iban[0].upper() != 'T' and self.iban[1].upper !='N':
			frappe.throw('IBAN :les deux premier lettre doit etre TN')
		



