from PyPDF2 import PdfFileReader, PdfFileWriter


def Merge(infilelist,outfile):
    pdffilewrite = PdfFileWriter()

    for filename in infilelist:
        pdffilereader = PdfFileReader(open(filename,'rb'))
        numpage = pdffilereader.getNumPages()
        for i in range(0, numpage):
            page = pdffilereader.getPage(i)
            pdffilewrite.addPage(page)

    pdffilewrite.addBlankPage()
    pdffilewrite.write(open(outfile, 'wb'))


if __name__ == "__main__":
    read_file = input()
    write_file = input()
    Merge(read_file, write_file)


