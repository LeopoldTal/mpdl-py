#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from mpdl import interpreter

class TestExecMdpl:
	def test_empty_program(self):
		assert interpreter.exec_mpdl([]) == []
