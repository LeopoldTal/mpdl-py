#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from sys import stderr
from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH, DEFAULT_OUT_FILE
from .mpdl import run, InterpreterFailureException

def main():
	parser = argparse.ArgumentParser(
		description = "Mondrian Painting Description Language interpreter"
	)
	parser.add_argument('source_file', help = 'path to MPDL source')
	parser.add_argument(
		'-o', '--out',
		default = DEFAULT_OUT_FILE,
		help = 'path to output file (default "%s")'
			% (DEFAULT_OUT_FILE,)
	)
	parser.add_argument(
		'-s', '--size',
		type = int,
		default = DEFAULT_CANVAS_SIZE,
		help = 'size of square output image in pixels (default %dpx)'
			% (DEFAULT_CANVAS_SIZE,)
	)
	parser.add_argument(
		'-b', '--border',
		type = int,
		default = DEFAULT_BORDER_WIDTH,
		help = 'thickness of border in pixels (default %dpx)'
			% (DEFAULT_BORDER_WIDTH,)
	)
	
	args = parser.parse_args()
	
	# TODO: catch and print nice error messages on file open failure
	with open(args.source_file) as h_in:
		source = h_in.read()
		try:
			image = run(source, args.size, args.border)
			with open(args.out, 'w') as h_out:
				h_out.write(image)
		except InterpreterFailureException as e:
			stderr.write(str(e))

if __name__ == '__main__':
	main()
