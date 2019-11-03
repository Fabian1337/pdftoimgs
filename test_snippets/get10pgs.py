from PyPDF2 import PdfFileReader, PdfFileWriter

with open(r"pdf_files\large.pdf", 'rb') as infile:

    reader = PdfFileReader(infile)
    writer = PdfFileWriter()
    for page in range(10):
        writer.addPage(reader.getPage(page))

    with open('output.pdf', 'wb') as outfile:
        writer.write(outfile)