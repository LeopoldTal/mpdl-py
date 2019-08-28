#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from sys import stderr
from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH, DEFAULT_OUT_FILE
from .mpdl import run, InterpreterFailureException

def parse_args():
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
	
	return parser.parse_args()

def get_source(source_file):
	try:
		return open(source_file)
	except IOError:
		stderr.write('Couldn\'t read source file %s\n' % (source_file,))
		exit(1)

def write_image(out_file, image):
	try:
		with open(out_file, 'w') as h_out:
			h_out.write(image)
	except IOError:
		stderr.write('Couldn\'t write to output file %s\n' % (out_file,))
		exit(1)

def main():
	args = parse_args()
	
	with get_source(args.source_file) as h_in:
		source = h_in.read()
		try:
			image = run(source, args.size, args.border)
		except InterpreterFailureException as e:
			stderr.write(str(e))
			exit(1)
		write_image(args.out, image)

if __name__ == '__main__':
	main()
