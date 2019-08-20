#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .parser import parse
from .interpreter import exec_mpdl
from .painter import paint_rectangles
from .ppm_writer import to_ppm

def run(mpdl_source): # TODO: more params
	"""run(mpdl_source) -> string
	
	Interpret and run an MPDL program
	Returns the output as a PPM"""
	instructions = parse(mpdl_source)
	rectangles = exec_mpdl(instructions)
	pixel_array = paint_rectangles(rectangles)
	painting = to_ppm(pixel_array)
	return painting

def main():
	# TODO: read source file from args
	run('v30 c1 c2')

if __name__ == '__main__':
	main()
