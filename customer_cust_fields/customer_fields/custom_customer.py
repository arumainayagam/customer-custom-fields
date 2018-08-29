# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
import frappe
from frappe.model.naming import make_autoname
from frappe import _, msgprint, throw
import frappe.defaults
from frappe.utils import flt, cint, cstr
from frappe.desk.reportview import build_match_conditions
from erpnext.utilities.transaction_base import TransactionBase
from erpnext.accounts.party import validate_party_accounts, get_dashboard_info, get_timeline_data # keep this
from frappe.contacts.address_and_contact import load_address_and_contact, delete_contact_and_address
from frappe.model.rename_doc import update_linked_doctypes
import erpnext.selling.doctype.customer.customer

def qwupdate(doc, method):
	# print('asdasd')
	tas = frappe.db.get_list("Dynamic Link", 
		fields= ["parent"],
		filters={"link_doctype": doc.doctype, "link_name": doc.name, "parenttype": "Address"})[0].parent

	if tas and (doc.get('gst_state_number') or doc.get('gst_state') or doc.get('gstin')):
		frappe.db.set_value("Address", tas, 'gst_state_number', doc.get('gst_state_number'))
		frappe.db.set_value("Address", tas, 'gst_state', doc.get('gst_state'))
		frappe.db.set_value("Address", tas, 'gstin', doc.get('gstin'))
		print(doc.get('gst_state_number'))
	# 	if doc.gst_state_number or doc.gst_state or doc.gstin:
	# 		frappe.db.set_value("Address", tas, 'gst_state_number', doc.gst_state_number)
	# 		frappe.db.set_value("Address", tas, 'gst_state', doc.gst_state)
	# 		frappe.db.set_value("Address", tas, 'gstin', doc.gstin)
	# 	print(tas)

	# if doc.flags.is_new_doc and doc.get('address_line1'):
	# 	address = frappe.get_doc({
	# 		'doctype': 'Address',
	# 		'gst_state_number': doc.get('gst_state_number'),
	# 		'gst_state': doc.get('gst_state'),
	# 		'gstin': doc.get('gstin'),
	# 		'address_title': doc.get('name'),
	# 		'address_line1': doc.get('address_line1'),
	# 		'address_line2': doc.get('address_line2'),
	# 		'city': doc.get('city'),
	# 		'state': doc.get('state'),
	# 		'pincode': doc.get('pincode'),
	# 		'country': doc.get('country'),
	# 		'links': [{
	# 			'link_doctype': doc.get('doctype'),
	# 			'link_name': doc.get('name')
	# 		}]
	# 	}).insert()

	# 	return address		