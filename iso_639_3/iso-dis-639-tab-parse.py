#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
# Copyright © 2008,2012 Tobias Quathamer <toddy@debian.org>
#
# This file is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this file; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""
Parse the SIL.org iso_639_3.tab file and create
an XML file for our own use.
"""

inverted_names = {}
names=open("iso_639_3_Name_Index.tab")
for li in names.readlines():
	(code, name, inverted_name) = li.split('\t')
	inverted_name = inverted_name.strip()
	if inverted_name != name:
		inverted_names[code] = inverted_name
names.close()


f=open("iso_639_3.tab")

ot=open("iso_639_3.xml","w")

ot.write("""<?xml version="1.0" encoding="UTF-8" ?>

<!--
This file gives a list of all languages in the ISO 639-3
standard, and is used to provide translations via gettext

Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
Copyright © 2008,2012 Tobias Quathamer <toddy@debian.org>

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

Source: <http://www.sil.org/iso639-3/>
-->

<!DOCTYPE iso_639_3_entries [
	<!ELEMENT iso_639_3_entries (iso_639_3_entry+)>
	<!ELEMENT iso_639_3_entry EMPTY>
	<!ATTLIST iso_639_3_entry
		id		CDATA	#REQUIRED
		name		CDATA	#REQUIRED
		type		CDATA	#REQUIRED
		scope 		CDATA   #REQUIRED
		part1_code	CDATA	#IMPLIED
		part2_code	CDATA	#IMPLIED
	>
]>

<iso_639_3_entries>
""")

f.readline()		# throw away the header
for li in f.readlines():
	# Split the line into parts and look for quotes
	parts = li.split('\t')
	# Reverse the parts, because Python's pop() function is much
	# faster at the end of a list instead of at the start of a list
	parts.reverse()
	# Take away the parts which are always at the same position
	code = parts.pop()
	status = parts.pop()
	partner_agency = parts.pop()
	iso_639_3 = parts.pop()
	iso_639_2 = parts.pop()
	b_code = parts.pop()
	bt_equiv = parts.pop()
	iso_639_1 = parts.pop()
	# At this point, we are at 'reference_name'. This field may
	# contain a quote sign, so we have to look for it and append
	# the next field, completing the field.
	reference_name = parts.pop()
	if reference_name.startswith('"'):
		reference_name = reference_name + parts.pop()
		# Now strip the quote signs
		reference_name = reference_name.strip('"')
	element_scope = parts.pop()
	language_type = parts.pop()
	documentation = parts.pop()
	ot.write('\t<iso_639_3_entry\n')
	ot.write('\t\tid="%s"\n' % code)
	if iso_639_1 != '':
		ot.write('\t\tpart1_code="%s"\n' % iso_639_1)
	if iso_639_2 != '':
		ot.write('\t\tpart2_code="%s"\n' % iso_639_2)
	ot.write('\t\tscope="%s"\n' % element_scope)
	ot.write('\t\ttype="%s"\n' % language_type)
	if inverted_names.has_key(code):
		reference_name = inverted_names[code]
	ot.write('\t\tname="%s" />\n' % reference_name)

ot.write('</iso_639_3_entries>\n')
ot.close()
f.close()
