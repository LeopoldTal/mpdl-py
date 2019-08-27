#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import mpdl_instruction, parser
from mpdl.colours import COLOURS
from mpdl.mpdl_exception import InvalidColourError, OutOfRangeError, SyntaxError

class TestParse:
	def test_empty_program(self):
		assert parser.parse('') == []
	
	def test_ignores_case(self):
		instructions = parser.parse('C1')
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_ignores_space(self):
		instructions = parser.parse('\n\n\r\t    C1 \n\v')
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_syntax_error_on_unknown(self):
		with pytest.raises(SyntaxError):
			parser.parse('x')

class TestPaint:
	def test_paint_single_rectangle(self):
		instructions = parser.parse('c1')
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_paint_multiple_rectangles(self):
		instructions = parser.parse('c1 c2 c3 c4')
		assert len(instructions) == 4
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
		assert isinstance(instructions[1], mpdl_instruction.Paint)
		assert instructions[1].colour == COLOURS.RED
		assert isinstance(instructions[2], mpdl_instruction.Paint)
		assert instructions[2].colour == COLOURS.BLUE
		assert isinstance(instructions[3], mpdl_instruction.Paint)
		assert instructions[3].colour == COLOURS.YELLOW
	
	def test_non_numeric_colour(self):
		with pytest.raises(SyntaxError):
			parser.parse('cc')
	
	def test_colour_out_of_range(self):
		with pytest.raises(InvalidColourError):
			parser.parse('c5')
	
	def test_cannot_paint_black(self):
		with pytest.raises(InvalidColourError):
			parser.parse('c0')

class TestSplit:
	def test_split(self):
		instructions = parser.parse('v50 h25')
		assert len(instructions) == 2
		assert isinstance(instructions[0], mpdl_instruction.VertSplit)
		assert instructions[0].split_percentage == 50
		assert isinstance(instructions[1], mpdl_instruction.HorizSplit)
		assert instructions[1].split_percentage == 25
	
	def test_non_numeric_percentage(self):
		with pytest.raises(SyntaxError):
			parser.parse('v50%')
	
	def test_negative_percentage(self):
		with pytest.raises(OutOfRangeError):
			parser.parse('v-1')
	
	def test_too_large_percentage(self):
		with pytest.raises(OutOfRangeError):
			parser.parse('v101')
