#!/usr/bin/env python3
#
# Takes a list of files on the command line and checks for valid
# UTF-8 data. Used for checking .po files.
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

import re
import sys

# Remove the script name from the files to check
sys.argv.pop(0)

# Assume that every file is valid
exit_status = 0

# Cycle through all files and check for valid UTF-8 encoding
for filename in sys.argv:
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
                print("UTF-8 encoding error in file %s: %s (position %d)" % (filename, error.reason, error.start))
                print("Binary data: %s" % line)
                exit_status = 1
                break
            if re.search(r'Content-Type: text/plain; charset=UTF-8', utf8):
                charset_utf8_seen = True
        # The whole file has been read, the content type should have
        # been detected now. Otherwise, it's an error.
        if not charset_utf8_seen:
            print("Error in file %s: could not detect Content-Type header" % filename)
            exit_status = 1
            break

sys.exit(exit_status)
