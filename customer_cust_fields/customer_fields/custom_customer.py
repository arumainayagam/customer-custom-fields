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
	
	if not doc.customer_primary_contact and (doc.dob or doc.doa):
		contact = frappe.get_doc({
			'doctype': 'Contact',
			'first_name': doc.name,
			'mobile_no': doc.mobile_no,
			'email_id': doc.email_id,
			'dob': doc.dob,
			'doa': doc.doa,
			'is_primary_contact': is_primary_contact,
			'links': [{
				'link_doctype': doc.doctype,
				'link_name': doc.name
			}]
		}).insert()
		# frappe.db.set_value("Customer", doc.name, 'customer_primary_contact', contact.name)
		doc.db_set('customer_primary_contact', contact.name)
		doc.save()
	print(doc.customer_primary_contact)
