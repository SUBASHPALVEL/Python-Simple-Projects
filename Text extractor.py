# 1 Importing statements

import PyPDF2

# 2 Reading the pdf file

Pdf_File= open("mypdf.pdf", "rb")

# 3 Initialising the pdf reader

PDF_Reader = PyPDF2.PdfFileReader(Pdf_File)

# 4 Extracting the text

Text = PDF_Reader.getPage(0).extractText()

# 5 Displaying the extracted text

print(Text)
