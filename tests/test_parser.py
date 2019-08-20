#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import parser

class TestParse:
	def test_empty_program(self):
		assert parser.parse('') == []
	
	def test_paint(self):
		assert len(parser.parse('c1')) == 1
