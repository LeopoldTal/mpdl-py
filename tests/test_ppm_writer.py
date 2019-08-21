#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import ppm_writer
from mpdl.colours import COLOURS

class TestToPpm:
	def test_empty_image(self):
		ppm = """P3
0 0 1

"""
		assert ppm_writer.to_ppm([]) == ppm
	
	def test_single_pixel(self):
		pixels = [
			[ COLOURS.RED ]
		]
		ppm = """P3
1 1 1
1 0 0
"""
		assert ppm_writer.to_ppm(pixels) == ppm
	
	def test_all_colours(self):
		pixels = [
			[ COLOURS.BLACK, COLOURS.RED, COLOURS.BLUE ],
			[ COLOURS.YELLOW, COLOURS.WHITE, COLOURS.WHITE ]
		]
		ppm = """P3
3 2 1
0 0 0  1 0 0  0 0 1
1 1 0  1 1 1  1 1 1
"""
		assert ppm_writer.to_ppm(pixels) == ppm
	
	def test_line_wrap(self):
		pixels = [
			[ COLOURS.WHITE ] * 16
		] * 3
		ppm = """P3
16 3 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
1 1 1  1 1 1  1 1 1  1 1 1  1 1 1  1 1 1
"""
		assert ppm_writer.to_ppm(pixels) == ppm
