#!/usr/bin/env python3
#
# Checks all JSON data files against their schema.
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
from jsonschema import validate

standards = [
	"639-2",
	"639-3",
	"639-5",
	"3166-1",
	"3166-2",
	"3166-3",
	"4217",
	"15924",
]

for standard in standards:
	with open("data/schema-" + standard + ".json") as schema_file:
		schema = json.load(schema_file)
		with open("data/iso_" + standard + ".json") as json_file:
			validate(json.load(json_file), schema)
