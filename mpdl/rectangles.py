#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BlankRectangle:
	""""BlankRectangle(left, top, right, bottom)
	
	Splittable, unpainted rectangle"""
	def __init__(self, left, top, right, bottom):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom

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
	
	def __eq__(self, other):
		return all([
			self.left == other.left,
			self.top == other.top,
			self.right == other.right,
			self.bottom == other.bottom,
			self.colour == other.colour
		])
	
	def __str__(self):
		return 'Rectangle %d, %d to %d, %d painted %s' % (
			self.left,
			self.top,
			self.right,
			self.bottom,
			self.colour.name
		)
