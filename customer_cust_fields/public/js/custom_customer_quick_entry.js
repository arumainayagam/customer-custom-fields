frappe.provide('frappe.ui.form');

frappe.ui.form.CustomerQuickEntryForm = frappe.ui.form.QuickEntryForm.extend({
	init: function(doctype, after_insert) {
		this._super(doctype, after_insert);
	},

	render_dialog: function() {
		this.mandatory = this.mandatory.concat(this.get_variant_fields());
		this._super();
	},

	get_variant_fields: function() {
		var variant_fields = [{
			fieldtype: "Section Break",
			label: __("Primary Contact Details"),
			collapsible: 1
		},
		{
			label: __("Email Id"),
			fieldname: "email_id",
			fieldtype: "Data"
		},
		{
			label: __("Date of Birth"),
			fieldname: "date_of_birth",
			fieldtype: "Date"
		},		
		{
			fieldtype: "Column Break"
		},
		{
			label: __("Mobile Number"),
			fieldname: "mobile_no",
			fieldtype: "Data"
		},
		{
			label: __("Date of Anniversary"),
			fieldname: "date_of_anniversary",
			fieldtype: "Date"
		},
		{
			fieldtype: "Section Break",
			label: __("Primary Address Details"),
			collapsible: 1
		},
		{
			label: __("Address Line 1"),
			fieldname: "address_line1",
			fieldtype: "Data"
		},
		{
			label: __("Address Line 2"),
			fieldname: "address_line2",
			fieldtype: "Data"
		},
		{
			label: __("ZIP Code"),
			fieldname: "pincode",
			fieldtype: "Data"
		},
		{
			label: __("Party GSTIN"),
			fieldname: "gstin",
			fieldtype: "Data"
		},
		{
			label: __("GST State"),
			fieldname: "gst_state",
			fieldtype: "Select",
			options: ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", 
			"Bihar", "Chandigarh","Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", 
			"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
			"Kerala", "Lakshadweep Islands", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
			"Mizoram", "Nagaland", "Odisha", "Other Territory", "Pondicherry", "Punjab", "Rajasthan", 
			"Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"			
			]
		},
		{
			fieldtype: "Column Break"
		},
		{
			label: __("City"),
			fieldname: "city",
			fieldtype: "Data"
		},
		{
			label: __("State"),
			fieldname: "state",
			fieldtype: "Data"
		},
		{
			label: __("Country"),
			fieldname: "country",
			fieldtype: "Link",
			options: "Country"
		},
		{
			label: __("Customer POS Id"),
			fieldname: "customer_pos_id",
			fieldtype: "Data",
			hidden: 1
		},
		{
			label: __("GST State Number"),
			fieldname: "gst_state_number",
			fieldtype: "Int"
		}];

		return variant_fields;
	},
})