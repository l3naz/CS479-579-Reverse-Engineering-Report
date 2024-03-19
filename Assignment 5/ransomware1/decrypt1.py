#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
	print("Usage:  decrypt1.py INFILE OUTFILENAME")

infile = sys.argv[1]
outfile = sys.argv[2]
key = ord('4')

with open(infile, "rb") as inf:
	with open(outfile, "wb") as ouf:

		contents = inf.read()
		
		for b in contents:
			ouf.write((b ^ key).to_bytes(1, "big"))

#			print(b^key, end ="")
