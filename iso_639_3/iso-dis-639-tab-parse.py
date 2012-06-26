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

# The Name_Index file has the same fields as the normal
# tab file. Extract the additional entries and save them
# for later.
alternative_names = {}
last_code = ''
last_name = ''
names = open("iso_639_3_Name_Index.tab")
for li in names.readlines():
	# Split the line into parts
	parts = li.split('\t')
	# Reverse the parts, because Python's pop() function is much
	# faster at the end of a list instead of at the start of a list
	parts.reverse()
	# Get the code
	code = parts.pop()
	# Take away unneeded parts
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
	# If we have already seen the code, we store the name
	# for later use, else skip the rest
	if code == last_code:
		if code in alternative_names:
			# If there is already an entry, just append the current name
			alternative_names[code].append(reference_name)
		else:
			# The is no entry yet, so save the previous name, too
			alternative_names[code] = [last_name, reference_name]
	# Store code and reference_name for comparison
	last_code = code
	last_name = reference_name
names.close()

# Set up a dictionary for the one letter abbreviations
status_codes = {'A': 'Active', 'R': 'Retired'}

def create_iso_639_3_entry(entry):
	result = '\t<iso_639_3_entry\n'
	result += '\t\tid="%s"\n' % entry['code']
	if entry['iso_639_1'] != '':
		result += '\t\tpart1_code="%s"\n' % entry['iso_639_1']
	if entry['iso_639_2'] != '':
		result += '\t\tpart2_code="%s"\n' % entry['iso_639_2']
	result += '\t\tstatus="%s"\n' % entry['status']
	result += '\t\tscope="%s"\n' % entry['element_scope']
	result += '\t\ttype="%s"\n' % entry['language_type']
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
		part1_code	CDATA	#IMPLIED
		part2_code	CDATA	#IMPLIED
		status		CDATA	#REQUIRED
		scope		CDATA   #REQUIRED
		type		CDATA	#REQUIRED
		name		CDATA	#REQUIRED
	>
]>

<iso_639_3_entries>
""")

# The first line only contains a header, so discard it
tabular_file.readline()

# Set up a dictionary for XML element 'iso_639_3_entry'
iso_639_3_entry = {}

for li in tabular_file.readlines():
	# Split the line into parts
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
	# Write the last entry, before starting a new one
	if iso_639_3_entry.has_key('code'):
		entry = create_iso_639_3_entry(iso_639_3_entry)
		xml_file.write(entry)
		iso_639_3_entry = {}
	# Assemble the iso_639_3_entry
	iso_639_3_entry['code'] = code
	iso_639_3_entry['status'] = status_codes[status]
	iso_639_3_entry['iso_639_1'] = iso_639_1
	iso_639_3_entry['iso_639_2'] = iso_639_2
	iso_639_3_entry['element_scope'] = element_scope
	iso_639_3_entry['language_type'] = language_type
	iso_639_3_entry['reference_name'] = reference_name
	# If there are alternative names, try to find the one
	# with a comma, which is treated as the inverted name.
	if code in alternative_names:
		for other_name in alternative_names[code]:
			# Skip the reference_name
			if other_name == reference_name:
				continue
			# If there is a comma, use this as the inverted form
			if ',' in other_name:
				iso_639_3_entry['inverted_name'] = other_name

# Finally, write the last entry and close the XML file
entry = create_iso_639_3_entry(iso_639_3_entry)
xml_file.write(entry)
xml_file.write('</iso_639_3_entries>\n')
xml_file.close()

tabular_file.close()
