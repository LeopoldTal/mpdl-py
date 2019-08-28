#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colours import COLOURS
from .mpdl_exception import InvalidColourError, OutOfRangeError, SyntaxError
from .mpdl_instruction import Paint, HorizSplit, VertSplit, TracingContext

class Parser:
	"""Parser(mpdl_source) -> MPDL parser"""
	def __init__(self, mpdl_source):
		self.source = mpdl_source
	
	def reset_parser(self):
		"""parser.reset_parser() -> reset all parser state"""
		self.instructions = []
		self.line_number = 1
		self.col_number = 1
		self.statement_start_col_number = 1
		self.current_statement = ''
	
	def start_line(self):
		"""parser.start_line() -> reset column state"""
		self.col_number = 1
		self.statement_start_col_number = 1
		self.current_statement = ''
	
	def finish_statement(self):
		"""parser.finish_statement() -> terminate current statement if any"""
		if self.current_statement:
			context = TracingContext(
				line_number = self.line_number,
			col_number = self.statement_start_col_number
			)
			parser = SingleInstructionParser(context)
			instruction = parser.parse_statement(self.current_statement)
			self.instructions.append(instruction)
			self.current_statement = ''
		self.statement_start_col_number = self.col_number + 1
	
	def parse(self):
		"""parser.parse() -> list of instructions"""
		self.reset_parser()
		lines = self.source.splitlines()
		self.line_number = 1
		for line in lines:
			self.start_line()
			for char in line:
				if char.isspace():
					self.finish_statement()
				else:
					self.current_statement += char
				self.col_number += 1
			self.finish_statement()
			self.line_number += 1
		return self.instructions

class SingleInstructionParser:
	def __init__(self, context):
		self.context = context
	
	def parse_statement(self, statement):
		"""parse_statement(statement) -> instruction
	
		Parse a single MPDL statement"""
		command, arg = statement[0].lower(), statement[1:]
		commands = {
			'c': self.parse_paint,
			'h': self.parse_horiz_split,
			'v': self.parse_vert_split
		}
		if command in commands:
			return commands[command](arg)
		else:
			raise SyntaxError(
				'Unknown command: %s' % (statement,),
				self.context
			)

	# Painting

	def parse_paint(self, arg):
		"""parse_paint(colour argument) -> instruction"""
		colour = self.parse_colour(arg)
		return Paint(colour, self.context)

	def parse_colour(self, arg):
		"""parse_colour(string) -> colour"""
		try:
			colour_code = int(arg)
		except ValueError:
			raise SyntaxError(
				'Not a colour code: %s' % (arg,),
				self.context
			)
	
		try:
			colour = COLOURS(colour_code)
		except ValueError:
			raise InvalidColourError(
				'Invalid colour: %d' % (colour_code,),
				self.context
			)
		if colour == COLOURS.BLACK:
			raise InvalidColourError(
				'Invalid colour: %d' % (colour_code,),
				self.context
			)
	
		return colour

	# Splitting

	def parse_horiz_split(self, arg):
		"""parse_horiz_split(split percentage argument) -> instruction"""
		split_percentage = self.parse_split_percentage(arg)
		return HorizSplit(split_percentage, self.context)

	def parse_vert_split(self, arg):
		"""parse_vert_split(split percentage argument) -> instruction"""
		split_percentage = self.parse_split_percentage(arg)
		return VertSplit(split_percentage, self.context)

	def parse_split_percentage(self, arg):
		"""parse_split_percentage(string) -> int"""
		try:
			percentage = int(arg)
		except ValueError:
			raise SyntaxError(
				'Not an integer: %s' % (arg,),
				self.context
			)
	
		if percentage < 0 or percentage > 100:
			raise OutOfRangeError(
				'Out of 0-100 range: %d' % (percentage,),
				self.context
			)
	
		return percentage
