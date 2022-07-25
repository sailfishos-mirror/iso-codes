#!/usr/bin/python3
#
# Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
# Copyright © 2008,2012,2013,2022 Dr. Tobias Quathamer <toddy@debian.org>
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
a JSON file for our own use.
"""

import json

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
with open("iso_639_3_Name_Index.tab") as names:
    for line in names:
        # Split the line into parts
        parts = line.split('\t')
        # Reverse the parts, because Python's pop() function is much
        # faster at the end of a list instead of at the start of a list
        parts.reverse()
        # Get the fields
        code = parts.pop()
        print_name = parts.pop()
        inverted_name = parts.pop().strip()
        if inverted_name != print_name:
            inverted_names[print_name] = inverted_name

iso_639_3_entries = []
first_line = True
with open("iso_639_3.tab") as tabular_file:
    for line in tabular_file.readlines():
        if first_line:
            # The first line only contains a header, so discard it
            first_line = False
            continue
        # Split the line into parts
        parts = line.split('\t')
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
        # Assemble the ISO 639-3 entry with required fields
        entry = {}
        entry['alpha_3'] = code
        entry['name'] = reference_name
        entry['scope'] = element_scope
        entry['type'] = language_type
        # Add optional fields
        if part1:
            entry['alpha_2'] = part1
        if part2b and part2b != part2t:
            entry['bibliographic'] = part2b
        if reference_name in inverted_names:
            entry['inverted_name'] = inverted_names[reference_name]
        if code in common_names:
            entry['common_name'] = common_names[code]
        iso_639_3_entries.append(entry)

print(json.dumps({'639-3': iso_639_3_entries}, indent=2))
