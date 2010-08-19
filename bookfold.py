#!/usr/bin/python
#
# bookfold printing
# http://blogs.gnome.org/cneumair/2007/03/15/printing-instruction-manuals-how-to-reorder-postscript-files/

import sys
n = int(sys.argv[1])

if n % 2:
	sys.exit("Expected an even number, but %s is not even! Aborting" % n)
for i in range(1, n/2+1):
	if i % 2:
		print n+1-i, i,
	else:
		print i, n+1-i,
print
