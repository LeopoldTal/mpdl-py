#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import ppm_writer

class TestToPpm:
	def test_empty_image(self):
		ppm = """P3
0 0 1"""
		assert ppm_writer.to_ppm([]) == ppm
