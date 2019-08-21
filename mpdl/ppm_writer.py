#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colours import COLOURS

PIXEL_COLOURS = {
	COLOURS.BLACK: '0 0 0',
	COLOURS.RED: '1 0 0',
	COLOURS.BLUE: '0 0 1',
	COLOURS.YELLOW: '1 1 0',
	COLOURS.WHITE: '1 1 1'
}

PIXELS_PER_LINE = 10

def to_ppm(pixels):
	"""to_ppm(pixels) -> string
	
	Convert a pixel array to a PPM image"""
	nb_rows = len(pixels)
	nb_cols = len(pixels[0]) if nb_rows > 0 else 0
	
	magic = 'P3'
	meta = '%d %d 1' % (nb_cols, nb_rows)
	
	raster = '\n'.join(
		'\n'.join(
			'  '.join(PIXEL_COLOURS[pixel] for pixel in line)
			for line in chunk(row, PIXELS_PER_LINE)
		)
		for row in pixels
	)
	
	return '%s\n%s\n%s\n' % (magic, meta, raster)

def chunk(l, chunk_size):
	chunk_size = max(chunk_size, 1)
	for chunk_start in range(0, len(l), chunk_size):
		yield l[chunk_start:chunk_start + chunk_size]
