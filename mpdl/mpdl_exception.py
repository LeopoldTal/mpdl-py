#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MpdlException(Exception):
	def __init__(self, value, context = ''):
		Exception.__init__(self, '%s\n%s' % (value, context))

class ParseError(MpdlException):
	pass

class SyntaxError(ParseError):
	pass

class InvalidColourError(ParseError):
	pass

class OutOfRangeError(ParseError):
	pass

class RuntimeError(MpdlException):
	pass

class IncompletePaintingError(RuntimeError):
	pass

class NoRectangleError(RuntimeError):
	pass
