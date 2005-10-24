#!/usr/bin/env python
#
# Read iso-codes data file and output a .tab file
# 
# Copyright (C) 2004,2005 Alastair McKinstry <mckinstry@debian.org>
# Released under the GPL.
# $Id$

from xml.sax import make_parser, SAXException, SAXParseException
from xml.sax.handler import feature_namespaces, ContentHandler
import sys, os, getopt, urllib2

class printLines(ContentHandler):
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
try:
	dh = printLines(ofile)
	p.setContentHandler(dh)
	p.parse(sys.argv[1])
except SAXParseException, e:
	sys.stderr.write('%s:%s:%s: %s\n' % (e.getSystemId(),
		     e.getLineNumber(),
		     e.getColumnNumber(),
		     e.getMessage()))
	sys.exit(1)
except Exception, e:
	sys.stderr.write('<unknown>: %s\n' % str(e))
	sys.exit(1)
ofile.close()
