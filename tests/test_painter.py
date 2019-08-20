#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import painter

class TestPaintRectangles:
	def test_noop(self):
		assert painter.paint_rectangles([]) == []
