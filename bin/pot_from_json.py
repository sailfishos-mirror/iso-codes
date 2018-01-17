#!/usr/bin/env python3
#
# Read the specified JSON file and generate the POT file.
#
# Copyright © 2016 Dr. Tobias Quathamer <toddy@debian.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import json
import sys
import time

# Get the current ISO code domain and the path to the JSON data dir
if len(sys.argv) != 3:
    sys.exit("Please provide the domain and the path to the JSON data dir.")
domain = sys.argv[1]
datapath = sys.argv[2]

# The number starts after "iso_", so always after four characters
iso_number = domain[4:]

# Define the description of the ISO standard
# (only needed for the comment in the POT file header)
description = {
    "iso_639-2": "Codes for the representation of names of languages\n# Part 2: Alpha-3 code",
    "iso_639-3": "Codes for the representation of names of languages\n# Part 3: Alpha-3 code for comprehensive coverage of languages",
    "iso_639-5": "Codes for the representation of names of languages\n# Part 5: Alpha-3 code for language families and groups",
    "iso_3166-1": "Codes for the representation of names of countries and their subdivisions\n# Part 1: Country codes",
    "iso_3166-2": "Codes for the representation of names of countries and their subdivisions\n# Part 2: Country subdivision codes",
    "iso_3166-3": "Codes for the representation of names of countries and their subdivisions\n# Part 3: Code for formerly used names of countries",
    "iso_4217": "Codes for the representation of currencies",
    "iso_15924": "Codes for the representation of names of scripts",
}

# Define which field to use for the msgid comment,
# if different from alpha_3
comment = "alpha_3"
if domain in ["iso_3166-3", "iso_15924"]:
    comment = "alpha_4"
if domain == "iso_3166-2":
    comment = "code"

# Read in the JSON file
with open(datapath + "/" + domain + ".json", encoding="utf-8") as json_file:
    iso = json.load(json_file)

# Helper function for keeping track of msgids and comments
# This is needed to ensure that no msgid is repeated, but
# instead the comments are joined. (ISO 3166-2 is an example.)
def add_msgid(name, comment):
    # Search for a previous definition
    if name in msgids:
        data = sorted_data[msgids[name]]
        data["comment"].append(comment)
        sorted_data[msgids[name]] = data
    else:
        sorted_data.append({'msgid': name, 'comment': [comment]})
        # Store the index of the newly added msgid
        msgids[name] = len(sorted_data) - 1

# Collect all msgids with their comments
msgids = {}
sorted_data = []
for item in iso[iso_number]:
    add_msgid(item["name"], "Name for " + item[comment])
    if "official_name" in item:
        add_msgid(item["official_name"], "Official name for " + item[comment])
    if "common_name" in item:
        add_msgid(item["common_name"], "Common name for " + item[comment])
    if "inverted_name" in item:
        add_msgid(item["inverted_name"], "Inverted name for " + item[comment])

# Write the POT file
with open(domain + ".pot", "w", encoding="utf-8") as pot_file:
    # Write the header
    pot_file.write("# Translation of ISO " + iso_number + " to LANGUAGE\n")
    pot_file.write("# " + description[domain] + "\n")
    pot_file.write("#\n")
    pot_file.write("# This file is distributed under the same license as the iso-codes package.\n")
    pot_file.write("#\n")
    pot_file.write("# Copyright ©\n")
    pot_file.write("# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.\n")
    pot_file.write("#\n")
    pot_file.write("msgid \"\"\n")
    pot_file.write("msgstr \"\"\n")
    pot_file.write("\"Project-Id-Version: " + domain + "\\n\"\n")
    pot_file.write("\"Report-Msgid-Bugs-To: https://salsa.debian.org/iso-codes-team/iso-codes/issues\\n\"\n")
    pot_file.write("\"POT-Creation-Date: " + time.strftime('%F %H:%M%z') + "\\n\"\n")
    pot_file.write("\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n\"\n")
    pot_file.write("\"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n\"\n")
    pot_file.write("\"Language-Team: LANGUAGE <LL@li.org>\\n\"\n")
    pot_file.write("\"MIME-Version: 1.0\\n\"\n")
    pot_file.write("\"Content-Type: text/plain; charset=UTF-8\\n\"\n")
    pot_file.write("\"Content-Transfer-Encoding: 8bit\\n\"")
    # Write the data
    for msgid in sorted_data:
        pot_file.write("\n\n#. " + ", ".join(msgid["comment"]) + "\n")
        pot_file.write("msgid \"" + msgid["msgid"] + "\"\n")
        pot_file.write("msgstr \"\"")
    pot_file.write("\n")
