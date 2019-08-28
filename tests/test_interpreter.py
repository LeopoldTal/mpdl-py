#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import unittest
from mpdl import mpdl_instruction
from mpdl.colours import COLOURS
from mpdl.interpreter import MpdlInterpreter
from mpdl.mpdl_exception import IncompletePaintingError, NoRectangleError
from mpdl.rectangles import PaintingRectangle

class TestMpdlInterpreter:
	def test_empty_program(self):
		with pytest.raises(IncompletePaintingError):
			MpdlInterpreter([], 256, 3).run()
	
	def test_single_rectangle_no_border(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE)
		]
		expected_rectangles = [
			PaintingRectangle(0, 0, 10, 10, COLOURS.BLUE)
		]
		actual_rectangles = MpdlInterpreter(instructions, 10, 0).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)
	
	def test_single_rectangle_even_border(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE)
		]
		expected_rectangles = [
			PaintingRectangle(1, 1, 9, 9, COLOURS.BLUE)
		]
		actual_rectangles = MpdlInterpreter(instructions, 10, 2).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)
	
	def test_single_rectangle_odd_border(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE)
		]
		expected_rectangles = [
			PaintingRectangle(1, 1, 8, 8, COLOURS.BLUE)
		]
		actual_rectangles = MpdlInterpreter(instructions, 10, 3).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)
	
	def test_no_rectangle(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.Paint(COLOURS.RED)
		]
		with pytest.raises(NoRectangleError):
			MpdlInterpreter(instructions, 10, 0).run()
	
	def test_vert_split(self):
		instructions = [
			mpdl_instruction.VertSplit(40),
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.Paint(COLOURS.RED)
		]
		expected_rectangles = [
			PaintingRectangle(0, 0, 4, 10, COLOURS.RED),
			PaintingRectangle(4, 0, 10, 10, COLOURS.BLUE)
		]
		actual_rectangles = MpdlInterpreter(instructions, 10, 0).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)
	
	def test_horiz_split(self):
		instructions = [
			mpdl_instruction.HorizSplit(70),
			mpdl_instruction.Paint(COLOURS.YELLOW),
			mpdl_instruction.Paint(COLOURS.WHITE)
		]
		expected_rectangles = [
			PaintingRectangle(0, 0, 50, 35, COLOURS.WHITE),
			PaintingRectangle(0, 35, 50, 50, COLOURS.YELLOW)
		]
		actual_rectangles = MpdlInterpreter(instructions, 50, 0).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)
	
	def test_rounding(self):
		instructions = [
			mpdl_instruction.VertSplit(40),
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.Paint(COLOURS.RED)
		]
		expected_rectangles = [
			PaintingRectangle(0, 0, 3, 9, COLOURS.RED),
			PaintingRectangle(3, 0, 9, 9, COLOURS.BLUE)
		]
		actual_rectangles = MpdlInterpreter(instructions, 9, 0).run()
		compare_rectangle_collections(actual_rectangles, expected_rectangles)

class TestErrorTraces:
	def test_trace_empty_program(self):
		expected_error_trace = r"""No instructions found.*"""
		with pytest.raises(IncompletePaintingError, match = expected_error_trace):
			MpdlInterpreter([], 256, 3).run()
	
	def test_trace_single_unpainted_rectangle(self):
		context = mpdl_instruction.TracingContext(
			line_number = 17,
			col_number = 42
		)
		instructions = [
			mpdl_instruction.VertSplit(30),
			mpdl_instruction.Paint(COLOURS.BLUE, context)
		]
		expected_error_trace = r"""1 rectangle left unpainted
at line 17, col 42.*"""
		with pytest.raises(IncompletePaintingError, match = expected_error_trace):
			MpdlInterpreter(instructions, 256, 3).run()
	
	def test_trace_multiple_unpainted_rectangles(self):
		context = mpdl_instruction.TracingContext(
			line_number = 17,
			col_number = 42
		)
		instructions = [
			mpdl_instruction.VertSplit(30),
			mpdl_instruction.VertSplit(30, context)
		]
		expected_error_trace = r"""3 rectangles left unpainted
at line 17, col 42.*"""
		with pytest.raises(IncompletePaintingError, match = expected_error_trace):
			MpdlInterpreter(instructions, 256, 3).run()
	
	def test_trace_paint_no_rectangle(self):
		context = mpdl_instruction.TracingContext(
			line_number = 314,
			col_number = 15
		)
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.Paint(COLOURS.RED, context)
		]
		expected_error_trace = r"""No rectangle available for command c2
at line 314, col 15.*"""
		with pytest.raises(NoRectangleError, match = expected_error_trace):
			MpdlInterpreter(instructions, 10, 0).run()
	
	def test_trace_vert_split_no_rectangle(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.VertSplit(50)
		]
		expected_error_trace = r"""No rectangle available for command v50.*"""
		with pytest.raises(NoRectangleError, match = expected_error_trace):
			MpdlInterpreter(instructions, 10, 0).run()
	
	def test_trace_horiz_split_no_rectangle(self):
		instructions = [
			mpdl_instruction.Paint(COLOURS.BLUE),
			mpdl_instruction.HorizSplit(7)
		]
		expected_error_trace = r"""No rectangle available for command h7.*"""
		with pytest.raises(NoRectangleError, match = expected_error_trace):
			MpdlInterpreter(instructions, 10, 0).run()

def compare_rectangle_collections(actual, expected):
	case = unittest.TestCase()
	case.assertCountEqual(map(str, actual), map(str, expected))
