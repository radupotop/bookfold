#!/usr/bin/python

class bookfold():
	'''
	Transforms input PDF into a PDF that's printable as a book.
	Algorithm described here <http://blogs.gnome.org/cneumair/2007/03/15/printing-instruction-manuals-how-to-reorder-postscript-files/>
	'''

	def __init__(self, inputDoc):
		from pyPdf import PdfFileWriter, PdfFileReader

		blank  = PdfFileReader(file("blank.pdf", "rb"))
		input1 = PdfFileReader(file(inputDoc, "rb"))
		output = PdfFileWriter()

		# copy input doc to output
		numPages = input1.getNumPages()
		for page in range(numPages):
			output.addPage(input1.getPage(page))

		# append blank pages until total no. of pages is a multiple of 4
		blankPages = 0
		while ((numPages+blankPages) % 4):
			blankPages += 1
		for page in range(blankPages):
			output.addPage(blank.getPage(0))

		# write output
		outputStream = file("temp.pdf", "wb")
		output.write(outputStream)
		outputStream.close()

		# read output as input
		input2 = PdfFileReader(file("temp.pdf", "rb"))
		output = PdfFileWriter()
		totalPages = input2.getNumPages()

		# re-arrange pages
		for i in range(1, totalPages/2+1):
			if i % 2:
				output.addPage(input2.getPage(totalPages-i))
				output.addPage(input2.getPage(i-1))
				print totalPages+1-i, i,
			else:
				output.addPage(input2.getPage(i-1))
				output.addPage(input2.getPage(totalPages-i))
				print i, totalPages+1-i,

		# write output
		outputStream = file("output.pdf", "wb")
		output.write(outputStream)
		outputStream.close()

		import os
		os.remove("temp.pdf")


import sys
bookfold = bookfold(sys.argv[1])
