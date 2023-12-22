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

def extract_value(pdf, field, target_text):
    field_element = pdf.pq(f'LTTextLineHorizontal:contains("{field}") + LTTextLineHorizontal').eq(0)
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

name = extract_value(pdf, "NAME", target_text)
date_of_birth = extract_value(pdf, "DATE OF BIRTH", target_text)
pmi_number = extract_value(pdf, "PMI NUMBER", target_text)
insurance_number = extract_value(pdf, "INSURANCE NUMBER", target_text)
address = extract_value(pdf, "ADDRESS", target_text)
city = extract_value(pdf, "CITY", target_text)
state = extract_value(pdf, "STATE", target_text)
zip_code = extract_value(pdf, "ZIP CODE", target_text)
email = extract_value(pdf, "EMAIL ADDRESS", target_text)
preferred_phone = extract_value(pdf, "PREFERRED PHONE", target_text)
country_of_residence = extract_value(pdf, "COUNTY OF RESIDENCE", target_text)
cfr = extract_value(pdf, "(CFR)", target_text)
waiver_type = extract_value(pdf, "(WAIVER TYPE)", target_text)

person_receiving_services = {
    "name": name,
    "date_of_birth": date_of_birth,
    "pmi_number": pmi_number,
    "insurance_number": insurance_number,
    "address": address,
    "city": city,
    "state": state,
    "zip": zip_code,
    "email": email,
    "preferred_phone": preferred_phone,
    "country_of_residence": country_of_residence,
    "cfr": cfr,
    "waiver_type": waiver_type
}

print(person_receiving_services)
