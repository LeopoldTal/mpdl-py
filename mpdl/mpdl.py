#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH
from .parser import parse
from .interpreter import MpdlInterpreter
from .painter import paint_rectangles
from .ppm_writer import to_ppm

def run(mpdl_source, canvas_size, border_width):
	"""run(mpdl_source) -> string
	
	Interpret and run an MPDL program
	Returns the output as a PPM"""
	instructions = parse(mpdl_source)
	rectangles = MpdlInterpreter(instructions, canvas_size, border_width).run()
	pixel_array = paint_rectangles(rectangles, canvas_size, border_width)
	painting = to_ppm(pixel_array)
	return painting

def main():
	# TODO: read source file from args
	source = 'v25 h71 v93 h50 c4 c1 c1 c2 h71 c3 h44 c1 c1'
	image = run(source, DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH)
	print(image)

if __name__ == '__main__':
	main()
