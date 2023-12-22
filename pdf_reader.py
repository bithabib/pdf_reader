# import pdfquery

# pdf = pdfquery.PDFQuery('request.pdf')

# pdf.load()


# name = pdf.pq('LTTextLineHorizontal:contains("NAME") + LTTextLineHorizontal').eq(0).text()
# date_of_birth = pdf.pq('LTTextLineHorizontal:contains("DATE OF BIRTH") + LTTextLineHorizontal').eq(0).text()
# pmi_number = pdf.pq('LTTextLineHorizontal:contains("PMI NUMBER") + LTTextLineHorizontal').eq(0).text()
# insurance_number = pdf.pq('LTTextLineHorizontal:contains("INSURANCE NUMBER") + LTTextLineHorizontal + LTTextLineHorizontal').eq(0).text()
# address = pdf.pq('LTTextLineHorizontal:contains("ADDRESS") + LTTextLineHorizontal').eq(0).text()
# city = pdf.pq('LTTextLineHorizontal:contains("CITY") + LTTextLineHorizontal').eq(0).text()
# state = pdf.pq('LTTextLineHorizontal:contains("STATE") + LTTextLineHorizontal').eq(0).text()
# zip = pdf.pq('LTTextLineHorizontal:contains("ZIP CODE") + LTTextLineHorizontal').eq(0).text()
# email = pdf.pq('LTTextLineHorizontal:contains("EMAIL ADDRESS") + LTTextLineHorizontal').eq(0).text()
# prefered_phone = pdf.pq('LTTextLineHorizontal:contains("PREFERRED PHONE") + LTTextLineHorizontal + LTTextLineHorizontal').eq(0).text()
# country_of_residence = pdf.pq('LTTextLineHorizontal:contains("COUNTY OF RESIDENCE") + LTTextLineHorizontal').eq(0).text()
# cfr = pdf.pq('LTTextLineHorizontal:contains("(CFR)") + LTTextLineHorizontal').eq(0).text()
# waiver_type = pdf.pq('LTTextLineHorizontal:contains("(WAIVER TYPE)") + LTTextLineHorizontal').eq(0).text()




# person_receiving_services = {
#     "name": name,
#     "date_of_birth": date_of_birth,
#     "pmi_number": pmi_number,
#     "insurance_number": insurance_number,
#     "address": address,
#     "city": city,
#     "state": state,
#     "zip": zip,
#     "email": email,
#     "prefered_phone": prefered_phone,
#     "country_of_residance": country_of_residence,
#     "cfr": cfr,
#     "waiver_type": waiver_type
# }

# print(person_receiving_services)



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

print(person_receiving_services)

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

print(legal_representative_list)
