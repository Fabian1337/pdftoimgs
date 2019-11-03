from wand.image import Image, Color
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import tempfile

import io

pdf = io.BytesIO()
with open("./pdf_files/large.pdf", 'rb') as infile:
    reader = PdfFileReader(infile)

    writer = PdfFileWriter()

    for page in range(10):
        writer.addPage(reader.getPage(page))
    writer.write(pdf)

    pdf.seek(0)

    with(Image(file=pdf, resolution=120)) as source: 
        images = source.sequence
        pages = len(images)
        for i in range(pages):
            n = i + 1
            newfilename = "./img_files/pdf_page_" + str(n) + '.png'
            with Image(images[i]) as img:
                img.format = 'png'
                img.background_color = Color('white') # Set white background.
                img.alpha_channel = 'remove'
                img.save(filename=newfilename)