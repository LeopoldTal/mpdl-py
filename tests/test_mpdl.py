#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import mpdl

class TestMpdl:
	def test_stupid(self):
		assert mpdl.COLOURS.RED.value == 2
