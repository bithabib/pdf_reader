import pdfquery
pdf = pdfquery.PDFQuery('request.pdf')
pdf.load()

target_text = "Parent/Legal"


label = pdf.pq('LTPage:contains("{}")'.format(target_text))
page_pq = next(label.iterancestors('LTPage'))
pageNum = int(page_pq.layout.pageid)

print(pageNum)