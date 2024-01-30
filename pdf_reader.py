import pdfquery
pdf = pdfquery.PDFQuery('request.pdf')

def page_count(pdf):
    pass

def find_page_number(pdf, text):
    for i in range(0, 20):
        pdf.load(i)
        start_element = pdf.pq(f'LTTextLineHorizontal:contains("{text}")')
        if start_element:
            return i


def is_between(pdf, start_text, end_text, target_text, target_text_eq_value):
    start_element = pdf.pq(f'LTTextLineHorizontal:contains("{start_text}")')
    end_element = pdf.pq(f'LTTextLineHorizontal:contains("{end_text}")')
    target_text = pdf.pq(f'LTTextLineHorizontal:contains("{target_text}") + LTTextLineHorizontal').eq(target_text_eq_value)
    if start_element and end_element and target_text:
        start_bbox = [float(start_element.attr('x0')), float(start_element.attr('y0')),
                      float(start_element.attr('x1')), float(start_element.attr('y1'))]
        end_bbox = [float(end_element.attr('x0')), float(end_element.attr('y0')),
                    float(end_element.attr('x1')), float(end_element.attr('y1'))]
        target_bbox = [float(target_text.attr('x0')), float(target_text.attr('y0')),
                       float(target_text.attr('x1')), float(target_text.attr('y1'))]
        
        print(start_bbox)
        print(end_bbox)
        print(target_bbox)
        if start_bbox[1] > target_bbox[1] > end_bbox[1]:
            return target_text.text()
        else:
            return False
    else:
        return False
    
def is_after(pdf, start_text, target_text, target_text_eq_value):
    start_element = pdf.pq(f'LTTextLineHorizontal:contains("{start_text}")')
    target_text = pdf.pq(f'LTTextLineHorizontal:contains("{target_text}") + LTTextLineHorizontal').eq(target_text_eq_value)
    if start_element and target_text:
        start_bbox = [float(start_element.attr('x0')), float(start_element.attr('y0')),
                      float(start_element.attr('x1')), float(start_element.attr('y1'))]
        target_bbox = [float(target_text.attr('x0')), float(target_text.attr('y0')),
                       float(target_text.attr('x1')), float(target_text.attr('y1'))]
        
        print(start_bbox)
        print(target_bbox)
        if start_bbox[1] > target_bbox[1]:
            return target_text.text()
        else:
            return False
    else:
        return False
    
def is_before(pdf, end_text, target_text, target_text_eq_value):
    end_element = pdf.pq(f'LTTextLineHorizontal:contains("{end_text}")')
    target_text = pdf.pq(f'LTTextLineHorizontal:contains("{target_text}") + LTTextLineHorizontal').eq(target_text_eq_value)
    if end_element and target_text:
        end_bbox = [float(end_element.attr('x0')), float(end_element.attr('y0')),
                    float(end_element.attr('x1')), float(end_element.attr('y1'))]
        target_bbox = [float(target_text.attr('x0')), float(target_text.attr('y0')),
                       float(target_text.attr('x1')), float(target_text.attr('y1'))]
        
        print(end_bbox)
        print(target_bbox)
        if target_bbox[1] > end_bbox[1]:
            return target_text.text()
        else:
            return False
    else:
        return False
    

def single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number):
    json_data = {}
    
    if start_text_page_number == end_text_page_number:
        for target_text in fields:
            eq_value = 0
            while True:
                value = is_between(pdf, start_text, end_text, target_text, eq_value)
                if value:
                    json_data[target_text] = value
                    break
                eq_value += 1
                if eq_value > 10:
                    break
        return json_data
    else:
        for target_text in fields:
            while True:
                value = is_after(pdf, start_text, target_text, eq_value)
                if value:
                    json_data[target_text] = value
                    break
                eq_value += 1
                if eq_value > 10:
                    break
        eq_value = 0
        for target_text in fields:
            while True:
                value = is_before(pdf, end_text, target_text, eq_value)
                if value:
                    json_data[target_text] = value
                    break
                eq_value += 1
                if eq_value > 10:
                    break
        return json_data

start_text = 'Person Receiving Services'
start_text_page_number = find_page_number(pdf, start_text)
end_text = 'Parent/Legal Representative/Managing Party'
end_text_page_number = find_page_number(pdf, end_text)
fields = ['NAME', 'DATE OF BIRTH', 'PMI NUMBER', 'applicable)', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'EMAIL ADDRESS', 'NUMBER', 'COUNTY OF RESIDENCE', '(CFR)', '(WAIVER TYPE)']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = 'Parent/Legal Representative/Managing Party'
start_text_page_number = find_page_number(pdf, start_text)
end_text = "Lead Agency/County"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['NAME', 'EMAIL ADDRESS', 'HOME PHONE NUMBER', 'CELL', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = "Lead Agency/County"
start_text_page_number = find_page_number(pdf, start_text)
end_text = "Fiscal Support Entity"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'CONTACT', 'EMAIL ADDRESS', 'NUMBER', 'FAX']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = "Fiscal Support Entity"
start_text_page_number = find_page_number(pdf, start_text)
end_text = "Page 1 of"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'CONTACT', 'EMAIL ADDRESS', 'PHONE', 'FAX']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = "Support Planner"
start_text_page_number = find_page_number(pdf, start_text)
end_text = "Employment Model"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'CONTACT', 'EMAIL ADDRESS', 'NUMBER', 'FAX']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = "Additional Contacts"
start_text_page_number = find_page_number(pdf, start_text)
end_text = "HOSPITAL"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['DOCTOR', 'CLINIC', 'PHONE', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

start_text = "HOSPITAL"
start_text_page_number = find_page_number(pdf, start_text)
end_text = "SCHOOL"
end_text_page_number = find_page_number(pdf, end_text)
fields = ['HOSPITAL', 'CLINIC', 'PHONE', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE']
json_data = single_person_information_extract(pdf, fields, start_text, end_text, start_text_page_number, end_text_page_number)
print(json_data)

