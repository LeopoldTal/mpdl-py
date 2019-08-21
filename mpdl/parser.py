#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colours import COLOURS
from .mpdl_exception import InvalidColourError, OutOfRangeError, SyntaxError
from .mpdl_instruction import Paint, HorizSplit, VertSplit

def parse(mpdl_source):
	"""parse(mpdl_source) -> list of instructions
	
	Parse an MPDL source string into executable instructions"""
	statements = mpdl_source.split()
	return [ parse_statement(statement) for statement in statements ]

def parse_statement(statement):
	"""parse_statement(statement) -> instruction
	
	Parse a single MPDL statement"""
	command, arg = statement[0].lower(), statement[1:]
	commands = {
		'c': parse_paint,
		'h': parse_horiz_split,
		'v': parse_vert_split
	}
	if command in commands:
		return commands[command](arg)
	else:
		raise SyntaxError('Unknown command: %s' % (statement,))

# Painting

def parse_paint(arg):
	"""parse_paint(colour argument) -> instruction"""
	colour = parse_colour(arg)
	return Paint(colour)

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

def parse_horiz_split(arg):
	"""parse_horiz_split(split percentage argument) -> instruction"""
	split_percentage = parse_split_percentage(arg)
	return HorizSplit(split_percentage)

def parse_vert_split(arg):
	"""parse_vert_split(split percentage argument) -> instruction"""
	split_percentage = parse_split_percentage(arg)
	return VertSplit(split_percentage)

def parse_split_percentage(arg): # TODO: syntax errors, 0-100
	"""parse_split_percentage(string) -> int"""
	try:
		percentage = int(arg)
	except ValueError:
		raise SyntaxError('Not an integer: %s' % (arg,))
	
	if percentage < 0 or percentage > 100:
		raise OutOfRangeError('Out of 0-100 range: %d' % (percentage,))
	
	return percentage
