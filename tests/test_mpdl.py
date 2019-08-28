#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import mpdl
from mpdl import InterpreterFailureException

class TestMpdl:
	def test_full_run(self):
		source = 'v25 h71 v93 h50 c4 c1 c1 c2 h71 c3 h44 c1 c1'
		canvas_size = 256
		border_width = 3
		actual = mpdl.run(source, canvas_size, border_width)
		with open('tests/expected.ppm') as h:
			expected = h.read()
			assert actual == expected
	
	def test_failure(self):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('v50', 10, 0)

class TestParamValidation:
	def test_non_numeric_border(self):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 10, 'a')
	
	def test_non_integer_border(size):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 256, 0.5)
	
	def test_negative_border(self):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 10, -1)
	
	def test_non_numeric_size(size):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 'a', 0)
	
	def test_non_integer_size(size):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 10.5, 0)
	
	def test_zero_size(self):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 0, 0)
	
	def test_border_bigger_than_canvas(self):
		with pytest.raises(InterpreterFailureException):
			mpdl.run('c1', 256, 300)
