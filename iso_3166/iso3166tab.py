#!/usr/bin/python
#
# Read iso-codes data file and output a .tab file
# 
# Copyright (C) 2004 Alastair McKinstry <mckinstry@debian.org>
# Released under the GPL.
# $Id$

from xml.sax import saxutils, make_parser, saxlib, saxexts, ContentHandler
from xml.sax.handler import feature_namespaces
import sys, os, getopt, urllib2

class printLines(saxutils.DefaultHandler):
	def __init__(self, ofile):
		self.ofile = ofile

	def startElement(self, name, attrs):
		if name != 'iso_3166_entry':
			return
		code = attrs.get('alpha_2_code', None)
		if code == None:
			raise RunTimeError, "Bad file"	
		if type(code) == unicode:
			code = code.encode('UTF-8')
		name = attrs.get('name', None)
		if name == None:
			raise RunTimeError, " BadFile"
		if type(name) == unicode:
			name = name.encode('UTF-8')
		common_name = attrs.get('common_name', None)
		if common_name != None:
			if type(common_name) == unicode:
				name = common_name.encode('UTF-8')
			else:
				name = common_name
		self.ofile.write (code + '\t' + name + '\n')


## 
## MAIN
##


ofile = sys.stdout
p = make_parser()
p.setErrorHandler(saxutils.ErrorPrinter())
try:
	dh = printLines(ofile)
	p.setContentHandler(dh)
	p.parse('iso_3166.xml')
except IOError,e:
	print in_sysID+": "+str(e)
except saxlib.SAXException,e:
	print str(e)

ofile.close()
