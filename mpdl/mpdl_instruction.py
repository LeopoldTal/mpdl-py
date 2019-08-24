#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .rectangles import BlankRectangle, PaintingRectangle

class MpdlInstruction:
	"""Abstract MPDL instruction"""
	pass # TODO: add tracing info

class VertSplit(MpdlInstruction):
	"""VertSplit(split_percentage) -> MPDL instruction
	Split a rectangle vertically:
	split_percentage% on the left, 100-split_percentage% on the right"""
	def __init__(self, split_percentage):
		self.split_percentage = split_percentage
	
	def __str__(self):
		return 'v%d' % (self.split_percentage,)
	
	def apply(self, stack, painted_rectangles):
		to_split = stack.pop()
		
		width = to_split.right - to_split.left
		cutoff = to_split.left + width * self.split_percentage // 100
		
		left = BlankRectangle(
			to_split.left, to_split.top,
			cutoff, to_split.bottom
		)
		right = BlankRectangle(
			cutoff, to_split.top,
			to_split.right, to_split.bottom
		)
		stack.extend([left, right])

class HorizSplit(MpdlInstruction):
	"""HorizSplit(split_percentage) -> MPDL instruction
	Split a rectangle horizontally:
	split_percentage% on top, 100-split_percentage% on bottom"""
	def __init__(self, split_percentage):
		self.split_percentage = split_percentage
	
	def __str__(self):
		return 'h%d' % (self.split_percentage,)
	
	def apply(self, stack, painted_rectangles):
		to_split = stack.pop()
		
		height = to_split.bottom - to_split.top
		cutoff = to_split.top + height * self.split_percentage // 100
		
		top = BlankRectangle(
			to_split.left, to_split.top,
			to_split.right, cutoff
		)
		bottom = BlankRectangle(
			to_split.left, cutoff,
			to_split.right, to_split.bottom
		)
		stack.extend([top, bottom])

class Paint(MpdlInstruction):
	"""Paint(colour) -> MPDL instruction
	Pop and paint a rectangle one of the preset non-black colours"""
	def __init__(self, colour):
		self.colour = colour
	
	def __str__(self):
		return 'c%d' % (self.colour.value,)
	
	def apply(self, stack, painted_rectangles):
		to_paint = stack.pop()
		painted_rectangle = PaintingRectangle(
			to_paint.left, to_paint.top, to_paint.right, to_paint.bottom,
			self.colour
		)
		painted_rectangles.append(painted_rectangle)
