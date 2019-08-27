#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .defaults import DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH
from .mpdl import run

def main():
	# TODO: read source file from args
	source = 'v25 h71 v93 h50 c4 c1 c1 c2 h71 c3 h44 c1 c1'
	image = run(source, DEFAULT_CANVAS_SIZE, DEFAULT_BORDER_WIDTH)
	print(image)

if __name__ == '__main__':
	main()
