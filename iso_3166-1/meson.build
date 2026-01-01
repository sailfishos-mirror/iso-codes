# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer
#
# SPDX-License-Identifier: LGPL-2.1-or-later

i18n = import('i18n')
fs = import('fs')

domain = 'iso_3166-1'
i18n.gettext(domain)

# Install symlinks for obsolete filenames
linguas = fs.read('LINGUAS').split('\n')
foreach lingua : linguas
    if lingua.startswith('#') or lingua == ''
        continue
    endif
    install_symlink(
        'iso_3166.mo',
        pointing_to: domain + '.mo',
        install_dir: get_option('localedir') / lingua / 'LC_MESSAGES',
    )
endforeach

test(
    'Check all .po files in ' + domain + ' are valid UTF-8',
    check_utf8,
    args: domain,
)
