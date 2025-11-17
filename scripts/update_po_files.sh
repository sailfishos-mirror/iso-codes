#!/bin/sh

# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer <toddy@debian.org>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

# This script merges all po files with the current pot file,
# removes obsolete msgids and substitutes the Project-Id-Version
# header with the PROJECT only, removing the VERSION part.
# This is done to keep the diff between releases small.

set -e

update_po_files() {
    domain=$1
    cd "$domain"

    po_files=$(find . -iname "*.po" -type f | LC_ALL=C sort)
    tmpfile=$(mktemp)

    for po_file in $po_files; do
        msgmerge --previous --quiet --output-file="$tmpfile" "$po_file" "$domain".pot
        msgattrib --no-obsolete --output-file="$po_file" "$tmpfile"
        sed -i -e "s/^\"Project-Id-Version: iso.*/\"Project-Id-Version: $domain\\\n\"/" "$po_file"
    done

    rm -f "$tmpfile"

    if [ -f sr.po ]; then
        recode-sr-latin < sr.po > sr@latin.po
        sed -i -e 's/^\"Language: sr\\n\"/\"Language: sr@latin\\n\"/' sr@latin.po
    fi

    if [ -f tt@iqtelif.po ]; then
        msgfilter --keep-header sed -f ../scripts/recode-tt-cyrillic.sed < tt@iqtelif.po > tt.po
        sed -i -e 's/^\"Language: tt@iqtelif\\n\"/\"Language: tt\\n\"/' tt.po
    fi

    cd ".."
}

DOMAINS=$(find . -maxdepth 1 -iname "iso_*" -type d | LC_ALL=C sort | xargs -n1 basename)
for domain in $DOMAINS; do
    echo "Processing $domain"
    update_po_files "$domain"
done
