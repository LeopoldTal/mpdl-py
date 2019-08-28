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
		self.context = None
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
		if len(self.instructions) == 0:
			raise IncompletePaintingError('No instructions found.')
		
		while len(self.instructions) > 0:
			self.step()
		
		if len(self.stack) > 0:
			nb_rectangles = len(self.stack)
			raise IncompletePaintingError(
				'%d rectangle%s left unpainted' % (
					nb_rectangles,
					'' if nb_rectangles == 1 else 's'
				),
				self.context
			)
		
		return self.painted_rectangles
	
	def step(self):
		"""interpreter.step() -> None
		
		Step through one instruction"""
		instruction = self.instructions.pop(0)
		self.context = instruction.context
		if len(self.stack) == 0:
			raise NoRectangleError(
			'No rectangle available for command %s' % (instruction,),
			self.context
		)
		instruction.apply(self.stack, self.painted_rectangles)
