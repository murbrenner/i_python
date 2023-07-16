import PyPDF2

#Now give the pdf name
pdfFileObj = open('C:\\Users\\Murilo Brenner\\Downloads\\relatorio.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFileObj)
print(len(reader.pages))
# will give total number of pages in pdf

pageObj = reader.pages[1]
print(pageObj)

text = (pageObj.extract_text())
text = text.split(",")
print(text)

search_keywords = ['.0482']
pg = (len(reader.pages))

print(len(reader.pages))
