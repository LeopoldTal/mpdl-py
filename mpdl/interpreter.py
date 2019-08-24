#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .mpdl_exception import IncompletePaintingError, NoRectangleError
from .rectangles import BlankRectangle

class MpdlInterpreter:
	def __init__(self, instructions, canvas_size, border_width):
		"""MpdlInterpreter(instructions, canvas_size, border_width)
			-> interpreter"""
		self.instructions = instructions
		self.canvas_size = canvas_size
		self.stack = [
			BlankRectangle(
				border_width // 2,
				border_width // 2,
				self.canvas_size - (border_width + 1) // 2,
				self.canvas_size - (border_width + 1) // 2
			)
		]
		self.painted_rectangles = []
	
	def run(self):
		"""interpreter.run() -> list of rectangles
		
		Execute MPDL instructions and return the list of resulting rectangles"""
		while len(self.instructions) > 0:
			self.step()
		
		if len(self.stack) > 0:
			raise IncompletePaintingError(
				'%d rectangles left unpainted' % (len(self.stack),)
			)
		
		return self.painted_rectangles
	
	def step(self):
		"""interpreter.step() -> None
		
		Step through one instruction"""
		instruction = self.instructions.pop(0)
		if len(self.stack) == 0:
			raise NoRectangleError(
			'No rectangle available for command %s' % (instruction,)
		)
		instruction.apply(self.stack, self.painted_rectangles)
