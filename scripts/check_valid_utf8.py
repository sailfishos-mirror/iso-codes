#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2016 Dr. Tobias Quathamer <toddy@debian.org>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

"""
Takes a directory on the command line and checks for valid
UTF-8 data in the .po files therein.
"""

import pathlib
import re
import sys

# Get the directory to check
if len(sys.argv) != 2:
    print("Error: Provide the directory to check.", file=sys.stderr)
    sys.exit(1)
directory = sys.argv[1]

# Assume that every file is valid
exit_status = 0

po_files = [f for f in pathlib.Path().glob(directory + "*po")]

# Cycle through all .po files to check for valid UTF-8 encoding
for filename in po_files:
    # Open the file for reading in binary mode
    with open(filename, "rb") as pofile:
        # The "Content-Type" header has not been seen yet
        charset_utf8_seen = False
        # Read all lines to check for Content-Type header
        for line in pofile:
            # Try to decode binary data to UTF-8
            try:
                utf8 = line.decode(encoding="utf-8", errors="strict")
            except UnicodeError as error:
                print(
                    f"UTF-8 encoding error in file {filename}: {error.reason} (position {error.start})",
                    file=sys.stderr,
                )
                print(f"Binary data: {line}", file=sys.stderr)
                exit_status = 1
                break
            if re.search(r"Content-Type: text/plain; charset=UTF-8", utf8):
                charset_utf8_seen = True
        # The whole file has been read, the content type should have
        # been detected now. Otherwise, it's an error.
        if not charset_utf8_seen:
            print(
                f"Error in file {filename}: could not detect UTF-8 Content-Type header",
                file=sys.stderr,
            )
            exit_status = 1
            break

sys.exit(exit_status)
