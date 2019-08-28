#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colours import COLOURS
from .mpdl_exception import InvalidColourError, OutOfRangeError, SyntaxError
from .mpdl_instruction import Paint, HorizSplit, VertSplit, TracingContext

# TODO: Messy! make this a class
def parse(mpdl_source):
	"""parse(mpdl_source) -> list of instructions
	
	Parse an MPDL source string into executable instructions"""
	lines = mpdl_source.splitlines()
	instructions = []
	line_number = 1 # humans use 1-indexed line/col numbers
	for line in lines:
		col_number = 1
		statement_start_col_number = 1
		statement = ''
		for char in line:
			print(line_number, col_number, statement_start_col_number, char, statement)
			if char.isspace():
				if statement:
					context = TracingContext(
						line_number = line_number,
						col_number = statement_start_col_number
					)
					instructions.append(parse_statement(statement, context))
					statement = ''
				statement_start_col_number = col_number + 1
			else:
				statement += char
			col_number += 1
		if statement:
			context = TracingContext(
				line_number = line_number,
				col_number = statement_start_col_number
			)
			instructions.append(parse_statement(statement, context))
			statement = ''
		line_number += 1
	return instructions

# TODO: this wants to be a class, to maintain context
def parse_statement(statement, context):
	"""parse_statement(statement) -> instruction
	
	Parse a single MPDL statement"""
	command, arg = statement[0].lower(), statement[1:]
	commands = {
		'c': parse_paint,
		'h': parse_horiz_split,
		'v': parse_vert_split
	}
	if command in commands:
		return commands[command](arg, context)
	else:
		raise SyntaxError('Unknown command: %s' % (statement,))

# Painting

def parse_paint(arg, context):
	"""parse_paint(colour argument) -> instruction"""
	colour = parse_colour(arg)
	return Paint(colour, context)

def parse_colour(arg):
	"""parse_colour(string) -> colour"""
	try:
		colour_code = int(arg)
	except ValueError:
		raise SyntaxError('Not a colour code: %s' % (arg,))
	
	try:
		colour = COLOURS(colour_code)
	except ValueError:
		raise InvalidColourError('Invalid colour: %d' % (colour_code,))
	if colour == COLOURS.BLACK:
		raise InvalidColourError('Invalid colour: %d' % (colour_code,))
	
	return colour

# Splitting

def parse_horiz_split(arg, context):
	"""parse_horiz_split(split percentage argument) -> instruction"""
	split_percentage = parse_split_percentage(arg)
	return HorizSplit(split_percentage, context)

def parse_vert_split(arg, context):
	"""parse_vert_split(split percentage argument) -> instruction"""
	split_percentage = parse_split_percentage(arg)
	return VertSplit(split_percentage, context)

def parse_split_percentage(arg):
	"""parse_split_percentage(string) -> int"""
	try:
		percentage = int(arg)
	except ValueError:
		raise SyntaxError('Not an integer: %s' % (arg,))
	
	if percentage < 0 or percentage > 100:
		raise OutOfRangeError('Out of 0-100 range: %d' % (percentage,))
	
	return percentage
