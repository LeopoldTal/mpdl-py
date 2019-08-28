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
	validate_params(canvas_size, border_width)
	try:
		instructions = Parser(mpdl_source).parse()
		rectangles = MpdlInterpreter(instructions, canvas_size, border_width).run()
		pixel_array = paint_rectangles(rectangles, canvas_size, border_width)
		painting = to_ppm(pixel_array)
		return painting
	except MpdlException as e:
		# Rethrow with nice description
		raise InterpreterFailureException('Error: %s\n' % (e,))

def validate_params(canvas_size, border_width):
	"""validate_params(canvas_size, border_width) -> None
	
	Assert that canvas and border size are both non-negative ints,
	canvas size is not zero, and canvas size is larger than border"""
	assert_is_int('size', canvas_size)
	assert_is_int('border', border_width)
	if canvas_size == 0:
		raise InterpreterFailureException('Invalid size: cannot be 0\n')
	if border_width > canvas_size:
		raise InterpreterFailureException(
			'Invalid border %dpx: cannot be bigger than size (%dpx)\n'
			% (border_width, canvas_size)
		)

def assert_is_int(name, number):
	try:
		int(number)
	except:
		raise InterpreterFailureException(
			'Invalid %s %s: must be an integer\n' % (name, number)
		)
	if number != int(number):
		raise InterpreterFailureException(
			'Invalid %s %s: must be an integer\n' % (name, number)
		)
	if number < 0:
		raise InterpreterFailureException(
			'Invalid %s %d: cannot be negative\n' % (name, number)
		)
