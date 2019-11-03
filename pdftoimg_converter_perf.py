from wand.image import Image, Color
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import tempfile


def pfd_to_imgs(pdf_filepath=None, out_folder=None, pages=[0, 1], outfilename="pdf_page_", file_format="png"):
    with open(pdf_filepath, 'rb') as infile:

        pdf = tempfile.TemporaryFile()
        reader = PdfFileReader(infile)

        numPages = reader.getNumPages()

        if pages[1] > numPages or pages[1] == -1:
            pages[1] = numPages

        writer = PdfFileWriter()

        for page in range(pages[0], pages[1], 1):
            writer.addPage(reader.getPage(page))

        writer.write(pdf)

        pdf.seek(0)

        _pfd_to_imgs(pdf_fileobj=pdf, out_folder=out_folder, pages=pages,
                     outfilename=outfilename, file_format=file_format)


def _pfd_to_imgs(pdf_fileobj=None, out_folder=None, pages=[0, 1], outfilename="pdf_page_", file_format="png"):
    with(Image(file=pdf_fileobj, resolution=150)) as pdfs:
        images = pdfs.sequence
        if pages[1] > len(images) or pages[1] == -1:
            pages[1] = len(images)
        if pages[1] <= len(images):
            for i in range(pages[0], pages[1], 1):
                outname = "{}{}{}.{}".format(out_folder, outfilename, i, file_format)
                with Image(images[i]) as img:
                    img.format = 'png'
                    img.background_color = Color('white') # Set white background.
                    img.alpha_channel = 'remove'
                    img.save(filename=outname)


pfd_to_imgs(pdf_filepath="./pdf_files/large.pdf", out_folder="./img_files/",
            pages=[0, 20], outfilename="pdf_page_", file_format="png")
