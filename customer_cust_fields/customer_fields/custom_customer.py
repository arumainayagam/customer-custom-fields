# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
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


@frappe.whitelist()
def update_contact(doc, method):
	is_primary_contact=1

	# if not doc.mobile_no and not doc.email_id:
	# 	contact = frappe.get_doc({
	# 		'doctype': 'Contact',
	# 		'first_name': doc.name,
	# 		'mobile_no': doc.mobile_no,
	# 		'email_id': doc.email_id,
	# 		'dob': doc.date_of_birth,
	# 		'doa': doc.date_of_anniversary,
	# 		'is_primary_contact': is_primary_contact,
	# 		'links': [{
	# 			'link_doctype': doc.doctype,
	# 			'link_name': doc.name
	# 		}]
	# 	}).insert()
	# 	# frappe.db.set_value("Customer", doc.name, 'customer_primary_contact', contact.name)
	# 	doc.db_set('customer_primary_contact', contact.name)
	# 	doc.save()

	# if doc.mobile_no or doc.email_id:	
		# frappe.db.set_value("Contact", doc.customer_primary_contact, 'dob', doc.date_of_birth)
		# frappe.db.set_value("Contact", doc.customer_primary_contact, 'doa', doc.date_of_anniversary)
		# doc.save()
	# print(doc.date_of_birth)


		# if doc.gstin or doc.gst_state or doc.gst_state_number:

			# address = frappe.get_doc({
			# 	'doctype': 'Address',
			# 	'address_title': doc.name,
			# 	'address_line1': doc.address_line1,
			# 	'address_line2': doc.address_line2,
			# 	'city': doc.city,
			# 	'state': doc.state,
			# 	'pincode': doc.pincode,
			# 	'country': doc.country,
			# 	'gstin': doc.gstin,
			# 	'gst_state': doc.gst_state,
			# 	'gst_state_number': doc.gst_state_number,
			# 	'links': [{
			# 		'link_doctype': doc.doctype,
			# 		'link_name': doc.name
			# 	}]
			# }).insert()
