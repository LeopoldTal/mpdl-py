#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
