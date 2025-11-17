#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2016 Dr. Tobias Quathamer <toddy@debian.org>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

"""
Checks all JSON data files against their schema.
"""

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

# Validate against schema
for standard in standards:
    with open("data/schema-" + standard + ".json", encoding="utf-8") as schema_file:
        schema = json.load(schema_file)
        with open("data/iso_" + standard + ".json", encoding="utf-8") as json_file:
            validate(json.load(json_file), schema)

# Ensure correct sorting order
for standard in standards:
    # Read in the JSON file
    with open("data/iso_" + standard + ".json", encoding="utf-8") as json_file:
        iso = json.load(json_file)
    sort_key = "alpha_3"
    if standard in ["3166-3", "15924"]:
        sort_key = "alpha_4"
    if standard == "3166-2":
        sort_key = "code"
    iso[standard].sort(key=lambda item: item[sort_key])

    # Write the sorted JSON file
    with open("data/iso_" + standard + ".json", "w", encoding="utf-8") as json_file:
        json.dump(iso, json_file, ensure_ascii=False, indent=2, sort_keys=True)
        # Add a final newline
        json_file.write("\n")

    # Check for codes that are assigned more than once
    keys = ["alpha_2", "alpha_3", "alpha_4", "numeric", "code"]
    for key in keys:
        # Skip ISO 3166-3 with data that has been withdrawn,
        # here are multiple keys expected
        if standard == "3166-3":
            continue
        values = []
        for item in iso[standard]:
            if key in item:
                if item[key] not in values:
                    values.append(item[key])
                else:
                    print(
                        "Error in ISO %s: key '%s' has multiple entries for value '%s'."
                        % (standard, key, item[key])
                    )
