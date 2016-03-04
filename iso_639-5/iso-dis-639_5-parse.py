#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""A script to generate iso_639_5.xml database for iso-codes.
@see http://www.loc.gov/standards/iso639-5/

@attention: File iso_639_5.xml will be written to the current directory.

@author: Pander
@license: LGPL
@contact: pander@opentaal.org
"""

__author__  = 'Pander <pander@opentaal.org>'
__version__ = '0.3'

import libxml2
import os.path

def parseChild(codes, parent, filename):
    u"""Parses recursivly parses RDF files
 
    @param codes: definitions for codes.
    @type codes: dict
    @param parents: parent codes for definition.
    @type status: str
    param filename: file name of child RDF file.
    @type status: str
    @return: decoded status.
    """
    code = None
    name = None
    if not os.path.isfile('rdf/' + filename):
        print 'WARNING, missing', filename, 'rerun download script, perhaps with increased recursion'
        return
    doc = libxml2.parseFile('rdf/' + filename)
    root = doc.xpathEval('/*')
    for d in root:
        dd = d.children
        while dd is not None:
            if dd.name == 'Language': # ???.rdf top-level children
                code = dd.prop('about')[-3:]
                ddd = dd.children
                while ddd is not None:
                    if ddd.name == 'authoritativeLabel' and ddd.prop('lang') == 'en':
                        name = ddd.content
                        if name and code:
                            if parent:
                                print 'ERROR, unexpected parent', code
                                exit(1)
                            else:
                                codes[code] = {'name':name, }
                    elif ddd.name == 'narrower':
                        dddd = ddd.children
                        while dddd is not None:
                            if dddd.name == 'Description':
                                fname = dddd.prop('about')
                                fname = fname[fname.find('/authorities/subjects/')+22:] + '.rdf'
                                parseChild(codes, code, fname)
                            dddd = dddd.next
                    ddd = ddd.next
            elif dd.name == 'Topic': # sh*.rdf file
                code = dd.prop('about')
                code = code[code.find('/authorities/subjects/')+22:]
                ddd = dd.children
                while ddd is not None:
                    if ddd.name == 'authoritativeLabel' and ddd.prop('lang') == 'en':
                        name = ddd.content
                        if code and name:
                            if code in codes.keys():
                                definition = codes[code] 
                                if definition['name'] == name and parent not in definition['parents']:
                                    definition['parents'] = definition['parents'] + ',' + parent
                                    codes[code] = definition
                            else:
                                codes[code] = {'name':name, 'parents':parent}
                    elif ddd.name == 'narrower':
                        dddd = ddd.children
                        while dddd is not None:
                            if dddd.name == 'Description':
                                fname = dddd.prop('about')
                                fname = fname[fname.find('/authorities/subjects/')+22:] + '.rdf'
                                parseChild(codes, code, fname)
                            dddd = dddd.next
                    ddd = ddd.next
            dd = dd.next

if __name__ == '__main__':
    # parse ISO 639-5 languages
    codes = {}
    doc = libxml2.parseFile('rdf/iso639-5.rdf') # top-level file
    root = doc.xpathEval('/*')
    for d in root:
        dd = d.children
        while dd is not None:
            if dd.name == 'MADSScheme':
                ddd = dd.children
                while ddd is not None:
                    if ddd.name == 'hasTopMemberOfMADSScheme':
                        dddd = ddd.children
                        while dddd is not None:
                            if dddd.name == 'Language':
                                filename = None
                                ddddd = dddd.children
                                while ddddd is not None:
                                    if ddddd.name == 'code':
                                        filename = '%s.rdf' % ddddd.content
                                    ddddd = ddddd.next
                                if filename:
                                    parseChild(codes, None, filename)
                                else:
                                    print 'ERROR, no filename found'
                                    exit(1)
                            dddd = dddd.next
                    ddd = ddd.next
            dd = dd.next
    print 'Found %d languages' % len(codes)

    # write XML file
    outfile = file('iso_639_5.xml', 'w')
    outfile.write("""<?xml version="1.0" encoding="UTF-8" ?>

<!--
This file gives a list of all languages in the ISO 639-5
standard, and is used to provide translations via gettext

Copyright © 2014 Pander <pander@opentaal.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.loc.gov/standards/iso639-5/>
-->

<!DOCTYPE iso_639_5_entries [
	<!ELEMENT iso_639_5_entries (iso_639_5_entry+)>
	<!ELEMENT iso_639_5_entry EMPTY>
	<!ATTLIST iso_639_5_entry
		id		CDATA	#REQUIRED
		parents		CDATA	#IMPLIED
		name		CDATA	#REQUIRED
	>
]>

<iso_639_5_entries>
""")
    for code in sorted(codes.keys()):
        definition = codes[code]
        outfile.write('\t<iso_639_5_entry\n')
        outfile.write('\t\tid="%s"\n' % code)
        if 'parents' in definition.keys():
            outfile.write('\t\tparents="%s"\n' % definition['parents'])
        outfile.write('\t\tname="%s" />\n' % definition['name'])
    outfile.write('</iso_639_5_entries>\n')
