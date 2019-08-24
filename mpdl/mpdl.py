#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH
from .parser import parse
from .interpreter import MpdlInterpreter
from .painter import paint_rectangles
from .ppm_writer import to_ppm

def run(mpdl_source): # TODO: more params
	"""run(mpdl_source) -> string
	
	Interpret and run an MPDL program
	Returns the output as a PPM"""
	instructions = parse(mpdl_source)
	rectangles = MpdlInterpreter(
		instructions,
		DEFAULT_CANVAS_SIZE,
		DEFAULT_BORDER_WIDTH
		).run()
	pixel_array = paint_rectangles(rectangles)
	painting = to_ppm(pixel_array)
	return painting

def main():
	# TODO: read source file from args
	run('v30 c1 c2')

if __name__ == '__main__':
	main()
