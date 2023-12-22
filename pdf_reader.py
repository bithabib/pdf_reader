import pdfquery

pdf = pdfquery.PDFQuery('request.pdf')

pdf.load()


name = pdf.pq('LTTextLineHorizontal:contains("NAME") + LTTextLineHorizontal').eq(0).text()
date_of_birth = pdf.pq('LTTextLineHorizontal:contains("DATE OF BIRTH") + LTTextLineHorizontal').eq(0).text()
pmi_number = pdf.pq('LTTextLineHorizontal:contains("PMI NUMBER") + LTTextLineHorizontal').eq(0).text()
insurance_number = pdf.pq('LTTextLineHorizontal:contains("INSURANCE NUMBER") + LTTextLineHorizontal + LTTextLineHorizontal').eq(0).text()
address = pdf.pq('LTTextLineHorizontal:contains("ADDRESS") + LTTextLineHorizontal').eq(0).text()
city = pdf.pq('LTTextLineHorizontal:contains("CITY") + LTTextLineHorizontal').eq(0).text()
state = pdf.pq('LTTextLineHorizontal:contains("STATE") + LTTextLineHorizontal').eq(0).text()
zip = pdf.pq('LTTextLineHorizontal:contains("ZIP CODE") + LTTextLineHorizontal').eq(0).text()
email = pdf.pq('LTTextLineHorizontal:contains("EMAIL ADDRESS") + LTTextLineHorizontal').eq(0).text()
prefered_phone = pdf.pq('LTTextLineHorizontal:contains("PREFERRED PHONE") + LTTextLineHorizontal + LTTextLineHorizontal').eq(0).text()
country_of_residence = pdf.pq('LTTextLineHorizontal:contains("COUNTY OF RESIDENCE") + LTTextLineHorizontal').eq(0).text()
cfr = pdf.pq('LTTextLineHorizontal:contains("(CFR)") + LTTextLineHorizontal').eq(0).text()
waiver_type = pdf.pq('LTTextLineHorizontal:contains("(WAIVER TYPE)") + LTTextLineHorizontal').eq(0).text()




person_receiving_services = {
    "name": name,
    "date_of_birth": date_of_birth,
    "pmi_number": pmi_number,
    "insurance_number": insurance_number,
    "address": address,
    "city": city,
    "state": state,
    "zip": zip,
    "email": email,
    "prefered_phone": prefered_phone,
    "country_of_residance": country_of_residence,
    "cfr": cfr,
    "waiver_type": waiver_type
}

print(person_receiving_services)

