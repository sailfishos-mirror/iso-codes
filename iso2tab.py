#!/usr/bin/env pythonenv python
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
    def __init__(self,element, nameslist, ofile):
         """ 
	 nameslist is the elements to be printed in  strings,
	 """
         self.attrnames = nameslist
	 self.element = element
	 self.ofile = ofile

    def startElement(self, name, attrs):
        # Get the name attributes
	if name != self.element:
	    return
	s = ""
	for aname in self.attrnames:
		n = attrs.get(aname, None)
		if n != None:
			if type(n) == unicode:
			    n = n.encode('UTF-8')
			if s == "":
			    s = n
			else:
			    s = s + '\t' + n
	ofile.write(s + "\n")


## 
## MAIN
##

try:
    (opts,trail)=getopt.getopt(sys.argv[1:],"e:f:", ["element=", "fields="])
    assert trail, "No argument provided"
except Exception,e:
    print "ERROR: %s" % e
    print
    print "Usage: iso2pot filename [outfilename]"
    print " filename: xml data file from iso-codes package"
    print " outfilename: Write to this file"
    sys.exit(1)

fields = ["name","official_name"]

for opt, arg in opts:
    if opt in ('--element'):
        element = arg
    elif opt in ('-f', '--fields'):
    	fields = arg.split(',')

if len(trail)==2:
    ofile = open(trail[1], 'w')
else:
    ofile = sys.stdout

p = make_parser()

try:
    dh = printLines(element, fields, ofile)
    p.setContentHandler(dh)
    p.parse(trail[0])
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

    
