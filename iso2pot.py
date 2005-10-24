#!/usr/bin/env python
#
# Read iso-codes data file and output a .pot file
# 
# Copyright (C) 2004,2005 Alastair McKinstry <mckinstry@debian.org>
# Released under the GPL.
# $Id$

from xml.sax import make_parser, SAXException, SAXParseException
from xml.sax.handler import feature_namespaces, ContentHandler
import sys, os, getopt, urllib2, locale, time

class printPot(ContentHandler):
    def __init__(self, nameslist,comment, ofile):
         """ 
	 nameslist is the elements to be printed in msgid strings,
	 comment is the atrribute to be used in the comment line
	 """
         self.attrnames = nameslist
	 self.comment = comment
	 self.ofile = ofile
	 self.done = {}


    def startElement(self, name, attrs):
        # Get the name attributes
	for aname in self.attrnames:
		n = attrs.get(aname, None)
		c = attrs.get(self.comment, None)
		if type(n) == unicode:
		    n = n.encode('UTF-8')
		if type(c) == unicode:
		    c = c.encode('UTF-8')
		if n != None and not self.done.has_key(n):
			self.ofile.write("\n")
                	if c != None:
				self.ofile.write("#. " + aname + " for " + c +  "\n")
			self.ofile.write ("msgid \"" + n + "\"\n")
			self.ofile.write ("msgstr \"\"\n")
			self.done[n] = 'True'

def printHeader(ofile, report_bugs_to, version):
    """Print the file header
    """
    # FIXME Derive these
    ofile.write ("# SOME DESCRIPTIVE TITLE.\n")
    ofile.write ("# Copyright (C) " + time.strftime('%Y') + "\n")
    ofile.write ("# This file is distributed under the same license as the iso-codes package.\n")
    ofile.write ("# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.\n")
    ofile.write ("# \n")
    ofile.write ("msgid \"\"\n")
    ofile.write ("msgstr \"\"\n")
    ofile.write ("\"Project-Id-Version: iso-codes " + version + "\\n\"\n")
    ofile.write ("\"Report-Msgid-Bugs-To: " + report_bugs_to + "\\n\"\n")
    ofile.write ("\"POT-Creation-Date: " + time.strftime('%F %H:%M%z') + "\\n\"\n")
    ofile.write ("\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n\"\n")
    ofile.write ("\"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n\"\n")
    ofile.write ("\"Language-Team: LANGUAGE <LL@li.org>\\n\"\n")
    ofile.write ("\"MIME-Version: 1.0\\n\"\n")
    ofile.write ("\"Content-Type: text/plain; charset=UTF-8\\n\"\n")
    ofile.write ("\"Content-Transfer-Encoding: 8bit\\n\"\n")


## 
## MAIN
##

locale.setlocale(locale.LC_ALL, 'C')

try:
    (opts,trail)=getopt.getopt(sys.argv[1:],"f:c:v:",
                               ["fields=", "comments=", "is-version="])
    assert trail, "No argument provided"
except Exception,e:
    print "ERROR: %s" % e
    print
    print "Usage: iso2pot filename [outfilename]"
    print " filename: xml data file from iso-codes package"
    print " outfilename: Write to this file"
    sys.exit(1)

version = "VERSION"
report_bugs_to = "Alastair McKinstry <mckinstry@debian.org>"
fields = ["name","official_name"]
comment = "code"

for opt, arg in opts:
    if opt in ('-v', '--is-version'):
        version = arg
    elif opt in ('-f', '--fields'):
    	fields = arg.split(',')
    elif opt in ('-c','--comments'):
        comment = arg

if len(trail)==2:
    ofile = open(trail[1], 'w')
else:
    ofile = sys.stdout

printHeader(ofile, report_bugs_to, version)

p = make_parser()

try:
    dh = printPot(fields, comment, ofile)
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

    
