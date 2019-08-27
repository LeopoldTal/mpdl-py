#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
	readme = readme_file.read()

requirements = ["argparse"]

test_requirements = ["pytest"]

setup(
	name="mpdl",
	version="0.1.0",
	description="Mondrian Painting Description Language interpreter",
	long_description=readme,
	url="https://github.com/LeopoldTal/mpdl-py",
	author="Leopold de Gaillande",
	author_email="leopold.tal.dg@gmail.com",
	license="MIT",
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3",
		"Topic :: Software Development :: Interpreters"
	],
	keywords="mpdl interpreter esoteric esolang",
	packages=["mpdl"],
	install_requires=requirements,
	entry_points={
		"console_scripts": [
			"mpdl = mpdl.mpdl_console:main"
		]
	},
	test_suite="tests",
	setup_requires=["pytest-runner"],
	tests_require=test_requirements,
)
