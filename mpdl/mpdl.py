#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .mpdl_exception import MpdlException
from .parser import Parser
from .interpreter import MpdlInterpreter
from .painter import paint_rectangles
from .ppm_writer import to_ppm

class InterpreterFailureException(Exception):
	pass

def run(mpdl_source, canvas_size, border_width):
	"""run(mpdl_source) -> string
	
	Interpret and run an MPDL program
	Returns the output as a PPM"""
	# TODO: validate args: 0 <= border_width <= canvas_size > 0
	try:
		instructions = Parser(mpdl_source).parse()
		rectangles = MpdlInterpreter(instructions, canvas_size, border_width).run()
		pixel_array = paint_rectangles(rectangles, canvas_size, border_width)
		painting = to_ppm(pixel_array)
		return painting
	except MpdlException as e:
		# Rethrow with nice description
		raise InterpreterFailureException('Error: %s\n' % (e,))
