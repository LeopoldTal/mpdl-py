#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MpdlInstruction:
	"""Abstract MPDL instruction"""
	pass # TODO: add tracing info

class VertSplit(MpdlInstruction):
	"""VertSplit(split_percentage) -> MPDL instruction
	Split a rectangle vertically:
	split_percentage% on the left, 100-split_percentage% on the right"""
	def __init__(self, split_percentage):
		self.split_percentage = split_percentage

class HorizSplit(MpdlInstruction):
	"""HorizSplit(split_percentage) -> MPDL instruction
	Split a rectangle horizontally:
	split_percentage% on top, 100-split_percentage% on bottom"""
	def __init__(self, split_percentage):
		self.split_percentage = split_percentage

class Paint(MpdlInstruction):
	"""Paint(colour) -> MPDL instruction
	Pop and paint a rectangle one of the preset non-black colours"""
	def __init__(self, colour):
		self.colour = colour
