import pdfquery
def extract_value(pdf, field, target_text, eq_value):
    field_element = pdf.pq(f'LTTextLineHorizontal:contains("{field}") + LTTextLineHorizontal').eq(eq_value)
    print(field_element.text())
    if field_element:
        target_element = pdf.pq(f'LTTextLineHorizontal:contains("{target_text}")')
        if target_element:
            # Get bounding boxes of the elements
            field_bbox = [float(field_element.attr('x0')), float(field_element.attr('y0')),
                          float(field_element.attr('x1')), float(field_element.attr('y1'))]

            target_bbox = [float(target_element.attr('x0')), float(target_element.attr('y0')),
                            float(target_element.attr('x1')), float(target_element.attr('y1'))]
            
            print(field_bbox)
            print(target_bbox)

            # Check if the target text is after the field
            if target_bbox[1] < field_bbox[3]:
                return field_element.text()
            else:
                print(f"{target_text} is before {field}.")
                return None
        else:
            print(f"{target_text} not found.")
            return None
    else:
        print(f"{field} not found.")
        return None

pdf = pdfquery.PDFQuery('request.pdf')
pdf.load()

target_text = "Parent/Legal"
trace = 0
person_receiving_service_name = extract_value(pdf, "NAME", target_text, trace)
person_receiving_service_date_of_birth = extract_value(pdf, "DATE OF BIRTH", target_text, trace)
person_receiving_service_pmi_number = extract_value(pdf, "PMI NUMBER", target_text, trace)
person_receiving_service_insurance_number = extract_value(pdf, "applicable)", target_text, trace)
person_receiving_service_address = extract_value(pdf, "ADDRESS", target_text, trace)
person_receiving_service_city = extract_value(pdf, "CITY", target_text, trace)
person_receiving_service_state = extract_value(pdf, "STATE", target_text, trace)
person_receiving_service_zip_code = extract_value(pdf, "ZIP CODE", target_text, trace)
person_receiving_service_email = extract_value(pdf, "EMAIL ADDRESS", target_text, trace)
person_receiving_service_preferred_phone = extract_value(pdf, "NUMBER", target_text, trace+2)
person_receiving_service_country_of_residence = extract_value(pdf, "COUNTY OF RESIDENCE", target_text, trace)
person_receiving_service_cfr = extract_value(pdf, "(CFR)", target_text, trace)
person_receiving_service_waiver_type = extract_value(pdf, "(WAIVER TYPE)", target_text, trace)

person_receiving_services = {
    "name": person_receiving_service_name,
    "date_of_birth": person_receiving_service_date_of_birth,
    "pmi_number": person_receiving_service_pmi_number,
    "insurance_number": person_receiving_service_insurance_number,
    "address": person_receiving_service_address,
    "city": person_receiving_service_city,
    "state": person_receiving_service_state,
    "zip": person_receiving_service_zip_code,
    "email": person_receiving_service_email,
    "preferred_phone": person_receiving_service_preferred_phone,
    "country_of_residence": person_receiving_service_country_of_residence,
    "cfr": person_receiving_service_cfr,
    "waiver_type": person_receiving_service_waiver_type
}

# print(person_receiving_services)

target_text = "Lead Agency/County"
legal_representative_list = []
while True:
    trace += 1
    legal_representative_name = extract_value(pdf, "NAME", target_text, trace)
    if not legal_representative_name:
        break
    legal_representative_email = extract_value(pdf, "EMAIL ADDRESS", target_text, trace)
    legal_representative_home_phone = extract_value(pdf, "HOME PHONE NUMBER", target_text, trace-1)
    legal_representative_cell_phone = extract_value(pdf, "CELL PHONE NUMBER", target_text, trace-1)
    legal_representative_address = extract_value(pdf, "ADDRESS", target_text, trace+2)
    legal_representative_city = extract_value(pdf, "CITY", target_text, trace)
    legal_representative_state = extract_value(pdf, "STATE", target_text, trace)
    legal_representative_zip = extract_value(pdf, "ZIP CODE", target_text, trace)
    legal_representative_list.append({
        'legal_representative_name': legal_representative_name,
        'legal_representative_email' : legal_representative_email,
        'legal_representative_home_phone': legal_representative_home_phone,
        'legal_representative_cell_phone': legal_representative_cell_phone,
        'legal_representative_address': legal_representative_address,
        'legal_representative_city': legal_representative_city,
        'legal_representative_state': legal_representative_state,
        'legal_representative_zip': legal_representative_zip
        })

# print(legal_representative_list)

target_text = "Fiscal"

lead_agency_name = extract_value(pdf, "NAME", target_text, trace)
lead_agency_address = extract_value(pdf, "ADDRESS", target_text, trace+2)
lead_agency_city = extract_value(pdf, "ITY", target_text, trace)
lead_agency_state = extract_value(pdf, "STATE", target_text, trace)
lead_agency_zip = extract_value(pdf, "ZIP CODE", target_text, trace)
lead_agency_contact_name = extract_value(pdf, "NAME", target_text, trace+1)
lead_agency_email = extract_value(pdf, "EMAIL ADDRESS", target_text, trace)
lead_agency_phone = extract_value(pdf, "NUMBER", target_text, trace+2)
lead_agency_fax = extract_value(pdf, "NUMBER", target_text, trace+3)

lead_agency = {
    'lead_agency_name': lead_agency_name,
    'lead_agency_address': lead_agency_address,
    'lead_agency_city': lead_agency_city,
    'lead_agency_state': lead_agency_state,
    'lead_agency_zip': lead_agency_zip,
    'lead_agency_contact_name': lead_agency_contact_name,
    'lead_agency_email': lead_agency_email,
    'lead_agency_phone': lead_agency_phone,
    'lead_agency_fax': lead_agency_fax
}
print(lead_agency)
trace += 1
target_text = "Page 1 of"
fiscal_support_name = extract_value(pdf, "NAME", target_text, trace+1)
fiscal_support_address = extract_value(pdf, "ADDRESS", target_text, trace+3)
fiscal_support_city = extract_value(pdf, "ITY", target_text, trace)
fiscal_support_state = extract_value(pdf, "STATE", target_text, trace)
fiscal_support_zip = extract_value(pdf, "ZIP CODE", target_text, trace)
fiscal_support_contact_name = extract_value(pdf, "NAME", target_text, trace+2)
fiscal_support_email = extract_value(pdf, "EMAIL ADDRESS", target_text, trace)
fiscal_support_phone = extract_value(pdf, "NUMBER", target_text, trace+3)
fiscal_support_fax = extract_value(pdf, "NUMBER", target_text, trace+4)

fiscal_support = {
    'fiscal_support_name': fiscal_support_name,
    'fiscal_support_address': fiscal_support_address,
    'fiscal_support_city': fiscal_support_city,
    'fiscal_support_state': fiscal_support_state,
    'fiscal_support_zip': fiscal_support_zip,
    'fiscal_support_contact_name': fiscal_support_contact_name,
    'fiscal_support_email': fiscal_support_email,
    'fiscal_support_phone': fiscal_support_phone,
    'fiscal_support_fax': fiscal_support_fax
}
print(fiscal_support)

