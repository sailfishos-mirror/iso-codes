# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer
#
# SPDX-License-Identifier: LGPL-2.1-or-later

i18n = import('i18n')

domain = 'iso_15924'
i18n.gettext(domain)

test(
    'Check all .po files in ' + domain + ' are valid UTF-8',
    check_utf8,
    args: domain,
)
