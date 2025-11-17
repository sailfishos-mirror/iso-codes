#!/bin/sh

# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer <toddy@debian.org>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

set -e

update_pot_file() {
    domain=$1
    pot_file="$domain/$domain.pot"

    backup=$(mktemp)
    cp "$pot_file" "$backup"

    python3 ./scripts/pot_from_json.py "$domain" .

    sed -f ./scripts/remove-potcdate.sin < "$pot_file" > "$domain".1po
    sed -f ./scripts/remove-potcdate.sin < "$backup" > "$domain".2po

    if cmp "$domain".1po "$domain".2po > /dev/null 2>&1; then
        rm -f "$domain".1po "$domain".2po "$pot_file"
        mv "$backup" "$pot_file"
    else
        rm -f "$domain".1po "$domain".2po "$backup"
    fi
}

DOMAINS=$(find . -maxdepth 1 -iname "iso_*" -type d | LC_ALL=C sort | xargs -n1 basename)
for domain in $DOMAINS; do
    echo "Processing $domain"
    update_pot_file "$domain"
done
