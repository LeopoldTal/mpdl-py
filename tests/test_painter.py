#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import painter
from mpdl.colours import COLOURS
from mpdl.rectangles import PaintingRectangle

x, K, R, Y, B = None, COLOURS.BLACK, COLOURS.RED, COLOURS.YELLOW, COLOURS.BLUE

class TestPaintRectangles:
	def test_paint_nothing(self):
		expected = [
			[x] * 256
		] * 256
		assert painter.paint_rectangles([], 256, 42) == expected
	
	def test_canvas_size(self):
		expected = [[x]]
		assert painter.paint_rectangles([], 1, 3) == expected
	
	def test_paint_rectangle_no_border(self):
		expected = [
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, R, R, R, R, R, x, x ],
			[ x, R, R, R, R, R, x, x ],
			[ x, R, R, R, R, R, x, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ]
		]
		rectangles = [
			PaintingRectangle(1, 2, 6, 5, R)
		]
		assert painter.paint_rectangles(rectangles, 8, 0) == expected
	
	def test_paint_rectangle_border_1px(self):
		expected = [
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, K, K, K, K, K, K, x ],
			[ x, K, R, R, R, R, K, x ],
			[ x, K, R, R, R, R, K, x ],
			[ x, K, K, K, K, K, K, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ]
		]
		rectangles = [
			PaintingRectangle(1, 2, 6, 5, R)
		]
		assert painter.paint_rectangles(rectangles, 8, 1) == expected
	
	def test_paint_rectangle_border_2px(self):
		expected = [
			[ x, x, x, x, x, x, x, x ],
			[ K, K, K, K, K, K, K, x ],
			[ K, K, K, K, K, K, K, x ],
			[ K, K, R, R, R, K, K, x ],
			[ K, K, K, K, K, K, K, x ],
			[ K, K, K, K, K, K, K, x ],
			[ x, x, x, x, x, x, x, x ],
			[ x, x, x, x, x, x, x, x ]
		]
		rectangles = [
			PaintingRectangle(1, 2, 6, 5, R)
		]
		assert painter.paint_rectangles(rectangles, 8, 2) == expected
	
	def test_paint_full(self):
		expected = [
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, R, R, R, K, K, K, Y, Y, Y, Y, K, K, K],
			[K, K, K, R, R, R, K, K, K, Y, Y, Y, Y, K, K, K],
			[K, K, K, R, R, R, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, R, R, R, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, R, R, R, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, R, R, R, K, K, K, B, B, B, B, K, K, K],
			[K, K, K, R, R, R, K, K, K, B, B, B, B, K, K, K],
			[K, K, K, R, R, R, K, K, K, B, B, B, B, K, K, K],
			[K, K, K, R, R, R, K, K, K, B, B, B, B, K, K, K],
			[K, K, K, R, R, R, K, K, K, B, B, B, B, K, K, K],
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K],
			[K, K, K, K, K, K, K, K, K, K, K, K, K, K, K, K]
		]
		rectangles = [
			PaintingRectangle(1, 1, 7, 14, R),
			PaintingRectangle(7, 1, 14, 6, Y),
			PaintingRectangle(7, 6, 14, 14, B)
		]
		assert painter.paint_rectangles(rectangles, 16, 3) == expected
