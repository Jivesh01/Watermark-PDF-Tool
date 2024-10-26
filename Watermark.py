import PyPDF2

# Open the PDF files
file = PyPDF2.PdfReader(open('merged_output.pdf','rb'))
watermark_file = PyPDF2.PdfReader(open('wtr.pdf','rb'))

# Create a PdfWriter object to write the output
output = PyPDF2.PdfWriter()

# Loop through each page of the original PDF
for i in range(len(file.pages)):
    page = file.pages[i]
    page.merge_page(watermark_file.pages[0])
    output.add_page(page)

# Write the watermarked PDF to a new file
with open('watermark_pdf.pdf','wb') as file:
    output.write(file)