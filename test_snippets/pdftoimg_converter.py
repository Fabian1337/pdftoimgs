from wand.image import Image


def pfd_to_imgs(pdf=None, out_folder=None, pages=[0, 1], outfilename="pdf_page_", file_format="jpg"):
    with(Image(filename=pdf, resolution=150)) as pdf:
        images = pdf.sequence
        if pages[1] > len(images) or pages[1] == -1:
            pages[1] = len(images)
        if pages[1] <= len(images):
            for i in range(pages[0], pages[1], 1):
                outname = "{}{}{}.{}".format(out_folder, outfilename, i, file_format)
                Image(images[i]).save(filename=outname)


pfd_to_imgs("./pdf_files/test.pdf", "./img_files/", pages=[0, -1])
