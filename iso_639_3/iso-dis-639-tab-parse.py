#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
# Copyright © 2008,2012,2013 Tobias Quathamer <toddy@debian.org>
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

# We support the common_name attribute, which will get lost
# during the generation of the xml file. Therefore, define
# the codes with their common names here.
common_names = {}
common_names['ben'] = "Bangla"

# The Name_Index file only has the fields
# Id, Print_Name, and Inverted_Name.
# There may be multiple lines with the same Id.
# Extract only the inverted names which differ.
inverted_names = {}
names = open("iso_639_3_Name_Index.tab")
for li in names.readlines():
	# Split the line into parts
	parts = li.split('\t')
	# Reverse the parts, because Python's pop() function is much
	# faster at the end of a list instead of at the start of a list
	parts.reverse()
	# Get the fields
	code = parts.pop()
	print_name = parts.pop()
	inverted_name = parts.pop().strip()
	if inverted_name != print_name:
		inverted_names[print_name] = inverted_name
names.close()

def create_iso_639_3_entry(entry):
	result = '\t<iso_639_3_entry\n'
	result += '\t\tid="%s"\n' % entry['code']
	if entry['part1'] != '':
		result += '\t\tpart1_code="%s"\n' % entry['part1']
	if entry['part2t'] != '':
		result += '\t\tpart2_code="%s"\n' % entry['part2t']
	# Special case for lcq, which is the only id with status "Retired"
	if entry['code'] == "lcq":
		result += '\t\tstatus="Retired"\n'
	else:
		result += '\t\tstatus="Active"\n'
	result += '\t\tscope="%s"\n' % entry['element_scope']
	result += '\t\ttype="%s"\n' % entry['language_type']
	if 'inverted_name' in entry:
		result += '\t\tinverted_name="%s"\n' % entry['inverted_name']
	result += '\t\treference_name="%s"\n' % entry['reference_name']
	if 'common_name' in entry:
		result += '\t\tcommon_name="%s"\n' % entry['common_name']
	# Use the inverted form for the name attribute
	if 'inverted_name' in entry:
		result += '\t\tname="%s" />\n' % entry['inverted_name']
	else:
		result += '\t\tname="%s" />\n' % entry['reference_name']
	return result

tabular_file = open("iso_639_3.tab")
xml_file = open("iso_639_3.xml","w")

xml_file.write("""<?xml version="1.0" encoding="UTF-8" ?>

<!--
This file gives a list of all languages in the ISO 639-3
standard, and is used to provide translations via gettext

Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
Copyright © 2008,2012,2013 Tobias Quathamer <toddy@debian.org>

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
		part1_code	CDATA	#IMPLIED
		part2_code	CDATA	#IMPLIED
		status		CDATA	#REQUIRED
		scope		CDATA   #REQUIRED
		type		CDATA	#REQUIRED
		inverted_name	CDATA	#IMPLIED
		reference_name	CDATA	#REQUIRED
		name		CDATA	#REQUIRED
		common_name	CDATA	#IMPLIED
	>
]>

<iso_639_3_entries>
""")

# The first line only contains a header, so discard it
tabular_file.readline()

for li in tabular_file.readlines():
	# Split the line into parts
	parts = li.split('\t')
	# Reverse the parts, because Python's pop() function is much
	# faster at the end of a list instead of at the start of a list
	parts.reverse()
	# Take away the parts which are always at the same position
	code = parts.pop()
	part2b = parts.pop()
	part2t = parts.pop()
	part1 = parts.pop()
	element_scope = parts.pop()
	language_type = parts.pop()
	reference_name = parts.pop()
	comment = parts.pop()
	# Assemble the iso_639_3_entry
	iso_639_3_entry = {}
	iso_639_3_entry['code'] = code
	iso_639_3_entry['part2b'] = part2b
	iso_639_3_entry['part2t'] = part2t
	iso_639_3_entry['part1'] = part1
	iso_639_3_entry['element_scope'] = element_scope
	iso_639_3_entry['language_type'] = language_type
	iso_639_3_entry['reference_name'] = reference_name
	if reference_name in inverted_names:
		iso_639_3_entry['inverted_name'] = inverted_names[reference_name]
	if code in common_names:
		iso_639_3_entry['common_name'] = common_names[code]
	entry = create_iso_639_3_entry(iso_639_3_entry)
	xml_file.write(entry)

# Finally, close the XML file
xml_file.write('</iso_639_3_entries>\n')
xml_file.close()

tabular_file.close()
