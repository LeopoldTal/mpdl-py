#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
	readme = readme_file.read()

requirements = []

test_requirements = ["pytest"]

setup(
	name="mpdl",
	version="0.1.0",
	description="Mondrian Painting Description Language interpreter",
	long_description=readme,
	author="Leopold de Gaillande",
	author_email="leopold.tal.dg@gmail.com",
	license="MIT",
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Topic :: Software Development :: Interpreters"
	],
	keywords="mpdl interpreter esoteric esolang",
	packages=["mpdl"],
	install_requires=requirements,
	entry_points={
		"console_scripts": [
			# TODO: "mpdl = mpdl_console:main"
		]
	},
	test_suite="tests",
	tests_require=test_requirements,
)
