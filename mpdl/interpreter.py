#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def exec_mpdl(instructions):
	"""exec_mpdl(instructions) -> list of rectangles
	
	Execute MPDL instructions and return the list of resulting rectangles"""
	return []

class PaintingRectangle:
	"""PaintingRectangle(left, top, right, bottom, colour)
	
	Rectangle
	- from (left, top) inclusive
	- to (right, bottom) exclusive
	- with colour fill"""
	def __init__(self, left, top, right, bottom, colour):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		self.colour = colour
