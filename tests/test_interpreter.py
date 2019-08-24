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

def compare_rectangle_collections(actual, expected):
	case = unittest.TestCase()
	case.assertCountEqual(map(str, actual), map(str, expected))
