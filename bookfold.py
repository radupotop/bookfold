#!/usr/bin/python
"""
BookFold: Makes a PDF suitable for printing

Usage: ./bookfold.py input.pdf

Algorithm described at:
http://blogs.gnome.org/cneumair/2007/03/15/printing-instruction-manuals-how-to-reorder-postscript-files/
"""
import sys
import math
from os.path import splitext
from pyPdf import PdfFileWriter, PdfFileReader

def generate_output_name(input_name):
    """
    mybook.pdf -> mybook-bookfold.pdf
    hello.pdf -> hello-bookfold.pdf
    """
    (root, ext) = splitext(input_name)
    suffix = "-bookfold"
    return root + suffix + ext

def get_cloned_output_writer(inp, blank):
    """
    Returns a PdfFileWriter object containing pages from input padded with pages from blank so that total number of pages is a multiple of 4.
    """
    output = PdfFileWriter()
    num_pages = inp.getNumPages()
    
    # Copy Input Pages
    for page in xrange(num_pages):
        output.addPage(inp.getPage(page))

    # Pad if necessary
    if num_pages % 4 == 0:
        return output

    blank_to_add = int(math.ceil(num_pages / 4.0)) * 4 - num_pages

    for _ in xrange(blank_to_add):
        output.addPage(blank.getPage(0))
    
    return output

def get_rearranged_output_writer(inp):
    """
    Returns a PdfFileWriter object which rearranges the output from input so that it is suitable for a booklet style printing.
    """
    output = PdfFileWriter()
    total_pages = inp.getNumPages()

    for i in range(1, total_pages/2 + 1):
        if i % 2:
            output.addPage(inp.getPage(total_pages - i))
            output.addPage(inp.getPage(i - 1))
            print total_pages + 1 - i, "," ,i, "," ,
        else:
            output.addPage(inp.getPage(i - 1))
            output.addPage(inp.getPage(total_pages - i))
            print i , "," , total_pages + 1 - i, "," ,
    return output
    
def main():
    # Handle Arguments
    if len(sys.argv) < 2:
        print "Usage: bookfold.py input.pdf"
        sys.exit(1)
    else:
        print sys.argv[1]
        input_doc = sys.argv[1]

    blank  = PdfFileReader(file("blank.pdf", "rb"))
    input1 = PdfFileReader(file(input_doc, "rb"))

    # Copy the Input Document to Output (padding if necessary)
    output = get_cloned_output_writer(input1, blank)

    # write temp
    with file("temp.pdf", "wb") as outputStream:
        output.write(outputStream)

    # read temp as input
    input2 = PdfFileReader(file("temp.pdf", "rb"))
    output = get_rearranged_output_writer(input2)

    # write output
    output_doc = generate_output_name(input_doc)
    with file(output_doc, "wb") as outputStream:
        output.write(outputStream)

    import os
    os.remove("temp.pdf")

if __name__ == "__main__":
    main()
