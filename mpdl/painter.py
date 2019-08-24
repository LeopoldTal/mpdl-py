#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colours import COLOURS
from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH

def paint_rectangles(rectangles, canvas_size, border_width):
	"""paint_rectangles(rectangles, canvas_size, border_width)
		-> list of list of colours
	
	Draw each rectangle with fill and stroke into a pixel array"""
	pixels = [
		[None] * canvas_size
		for _ in range(canvas_size)
	]
	
	for rectangle in rectangles:
		paint_rectangle(pixels, rectangle, border_width)
	
	return pixels

def paint_rectangle(pixels, rectangle, border_width):
	"""paint_rectangle(pixels, rectangle, border_width) -> None
	
	Draw a single rectangle in place"""
	outer_left = rectangle.left - border_width // 2
	inner_left = outer_left + border_width
	
	inner_right = rectangle.right - border_width // 2
	outer_right = inner_right + border_width
	
	outer_top = rectangle.top - border_width // 2
	inner_top = outer_top + border_width
	
	inner_bottom = rectangle.bottom - border_width // 2
	outer_bottom = inner_bottom + border_width
	
	for row in range(outer_top, outer_bottom):
		for col in range(outer_left, outer_right):
			pixels[row][col] = COLOURS.BLACK
	
	for row in range(inner_top, inner_bottom):
		for col in range(inner_left, inner_right):
			pixels[row][col] = rectangle.colour
