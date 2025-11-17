#!/bin/sh

# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer <toddy@debian.org>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

set -e

update_linguas() {
    domain=$1
    for filename in $(find "$domain" -iname "*po" | LC_ALL=C sort); do
        basename "$filename" .po
    done > "$domain"/LINGUAS
}

DOMAINS=$(find . -maxdepth 1 -iname "iso_*" -type d | LC_ALL=C sort | xargs -n1 basename)
for domain in $DOMAINS; do
    echo "Processing $domain"
    update_linguas "$domain"
done
