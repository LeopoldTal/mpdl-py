#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import mpdl_instruction
from mpdl.colours import COLOURS
from mpdl.mpdl_exception import InvalidColourError, OutOfRangeError, SyntaxError
from mpdl.parser import Parser

class TestParse:
	def test_empty_program(self):
		assert Parser('').parse() == []
	
	def test_ignores_case(self):
		instructions = Parser('C1').parse()
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_ignores_space(self):
		instructions = Parser('\n\n\r\t    C1 \n\v').parse()
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_line_number(self):
		source = 'v50\nh40 c1'
		instructions = Parser(source).parse()
		assert len(instructions) == 3
		assert instructions[0].line_number == 1
		assert instructions[1].line_number == 2
		assert instructions[2].line_number == 2
	
	def test_col_number(self):
		source = '  v50\nh40 c1'
		instructions = Parser(source).parse()
		assert len(instructions) == 3
		assert instructions[0].col_number == 3
		assert instructions[1].col_number == 1
		assert instructions[2].col_number == 5
	
	def test_syntax_error_on_unknown(self):
		expected_error_trace = r"""Unknown command: x
at line 1, col 1.*"""
		with pytest.raises(SyntaxError, match = expected_error_trace) as e:
			Parser('x').parse()

class TestPaint:
	def test_paint_single_rectangle(self):
		instructions = Parser('c1').parse()
		assert len(instructions) == 1
		assert isinstance(instructions[0], mpdl_instruction.Paint)
		assert instructions[0].colour == COLOURS.WHITE
	
	def test_paint_multiple_rectangles(self):
		instructions = Parser('c1 c2 c3 c4').parse()
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
			Parser('cc').parse()
	
	def test_colour_out_of_range(self):
		with pytest.raises(InvalidColourError):
			Parser('c5').parse()
	
	def test_cannot_paint_black(self):
		with pytest.raises(InvalidColourError):
			Parser('c0').parse()

class TestSplit:
	def test_split(self):
		instructions = Parser('v50 h25').parse()
		assert len(instructions) == 2
		assert isinstance(instructions[0], mpdl_instruction.VertSplit)
		assert instructions[0].split_percentage == 50
		assert isinstance(instructions[1], mpdl_instruction.HorizSplit)
		assert instructions[1].split_percentage == 25
	
	def test_non_numeric_percentage(self):
		with pytest.raises(SyntaxError):
			Parser('v50%').parse()
	
	def test_negative_percentage(self):
		with pytest.raises(OutOfRangeError):
			Parser('v-1').parse()
	
	def test_too_large_percentage(self):
		with pytest.raises(OutOfRangeError):
			Parser('v101').parse()
