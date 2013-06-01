# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sys, os

__version__ = '0.1'

setup(name='haproxy',
	version=__version__,
	description="The haproxy client communicates with the haproxy stats socket.",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Operating System :: POSIX",
		"Environment :: Console",
		"Programming Language :: Python",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries :: Python Modules",
	], 
	keywords='haproxy',
	author='Remco Verhoef',
	author_email='remco@red5.nl',
	url='http://github.com/nl5887/python-haproxy',
	license='MIT',
	packages=['haproxy'],
)

