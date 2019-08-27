#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import mpdl

class TestMpdl:
	def test_full_run(self):
		source = 'v25 h71 v93 h50 c4 c1 c1 c2 h71 c3 h44 c1 c1'
		canvas_size = 256
		border_width = 3
		actual = mpdl.run(source, canvas_size, border_width)
		with open('tests/expected.ppm') as h:
			expected = h.read()
			assert actual == expected
