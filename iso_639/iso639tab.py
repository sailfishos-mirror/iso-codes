#!/usr/bin/python
#
# Read iso-codes iso_639.xml data file and output a .tab file
# 
# Copyright (C) 2005 Alastair McKinstry <mckinstry@debian.org>
# Released under the GPL.
# $Id$

from xml.sax import saxutils, make_parser, saxlib, saxexts, ContentHandler
from xml.sax.handler import feature_namespaces
import sys, os, getopt, urllib2

class printLines(saxutils.DefaultHandler):
	def __init__(self, ofile):
		self.ofile = ofile

	def startElement(self, name, attrs):
		if name != 'iso_639_entry':
			return
		t_code = attrs.get('iso_639_2T_code', None)
		if t_code == None:
			raise RunTimeError, "Bad file"	
		if type(t_code) == unicode:
			t_code = t_code.encode('UTF-8')
		b_code = attrs.get('iso_639_2B_code', None)
		if b_code == None:
			raise RunTimeError, "Bad file"	
		if type(b_code) == unicode:
			b_code = b_code.encode('UTF-8')
		name = attrs.get('name', None)
		if name == None:
			raise RunTimeError, " BadFile"
		short_code=attrs.get('iso_639_1_code','XX')
		short_code=short_code.encode('UTF-8')
		if type(name) == unicode:
			name = name.encode('UTF-8')
		self.ofile.write (t_code + '\t' + b_code + '\t' + short_code + '\t' + name + '\n')


## 
## MAIN
##


ofile = sys.stdout
ofile.write("""
## iso-639.tab
##
## Copyright (C) 2005 Alastair McKinstry   <mckinstry@computer.org> 
## Released under the GNU License; see file COPYING for details
##
## PLEASE NOTE: THIS FILE IS DEPRECATED AND SCHEDULED TO BE REMOVED.
## IT IS FOR BACKWARD-COMPATIBILITY ONLY: PLEASE USE THE ISO-639.XML
## FILE INSTEAD.
##
## This file gives a list of all languages in the ISO-639
## standard, and is used to provide translations (via gettext)
##
## Status: ISO 639-2:1998 + additions and changes until 2003-03-05
## Source: http://lcweb.loc.gov/standards/iso639-2/englangn.html
##
## Columns:
##   iso-639-2 terminology code
##   iso-639-2 bibliography code
##   iso-639-1 code (XX if none exists)
##   Name (English)
##
##
""")
p = make_parser()
p.setErrorHandler(saxutils.ErrorPrinter())
try:
	dh = printLines(ofile)
	p.setContentHandler(dh)
	p.parse(sys.argv[1])
except IOError,e:
	print in_sysID+": "+str(e)
except saxlib.SAXException,e:
	print str(e)

ofile.close()
