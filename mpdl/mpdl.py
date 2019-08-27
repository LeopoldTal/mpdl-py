#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stderr
from .mpdl_exception import MpdlException
from .parser import parse
from .interpreter import MpdlInterpreter
from .painter import paint_rectangles
from .ppm_writer import to_ppm

def run(mpdl_source, canvas_size, border_width):
	"""run(mpdl_source) -> string
	
	Interpret and run an MPDL program
	Returns the output as a PPM"""
	# TODO: validate args: 0 <= border_width <= canvas_size > 0
	try:
		instructions = parse(mpdl_source)
		rectangles = MpdlInterpreter(instructions, canvas_size, border_width).run()
		pixel_array = paint_rectangles(rectangles, canvas_size, border_width)
		painting = to_ppm(pixel_array)
		return painting
	except MpdlException as e: # TODO: hmm. throw new exception and catch in main?
		stderr.write('Error: %s\n' % (e,))
