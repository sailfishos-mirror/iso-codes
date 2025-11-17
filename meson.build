# SPDX-FileCopyrightText: 2025 Dr. Tobias Quathamer
#
# SPDX-License-Identifier: LGPL-2.1-or-later

project(
    'iso-codes',
    version: '4.20.0',
    meson_version: '>= 0.61.0',
    license: 'LGPL-2.1-or-later',
)

# Needed for the "meson test" command
check_utf8 = find_program(
    meson.project_source_root() / 'scripts' / 'check_valid_utf8.py',
)

# Needed for the custom targets to create and install the
# deprecated XML files
xml_from_json = find_program(
    meson.project_source_root() / 'scripts' / 'xml_from_json.py',
)

# Handle domains of iso-codes
domains = [
    'iso_15924',
    'iso_3166-1',
    'iso_3166-2',
    'iso_3166-3',
    'iso_4217',
    'iso_639-2',
    'iso_639-3',
    'iso_639-5',
]

foreach domain : domains
    subdir(domain)
endforeach

# Install JSON data and schema files
json_files = [
    'data/iso_15924.json',
    'data/iso_3166-1.json',
    'data/iso_3166-2.json',
    'data/iso_3166-3.json',
    'data/iso_4217.json',
    'data/iso_639-2.json',
    'data/iso_639-3.json',
    'data/iso_639-5.json',
    'data/schema-15924.json',
    'data/schema-3166-1.json',
    'data/schema-3166-2.json',
    'data/schema-3166-3.json',
    'data/schema-4217.json',
    'data/schema-639-2.json',
    'data/schema-639-3.json',
    'data/schema-639-5.json',
]

install_data(
    json_files,
    install_dir: get_option('datadir') / meson.project_name() / 'json',
)

# Create iso-codes.pc
pkg_conf = configuration_data()
pkg_conf.set('VERSION', meson.project_version())
pkg_conf.set('DOMAINS', ' '.join(domains))
pkg_conf.set('PREFIX', get_option('prefix'))
configure_file(
    input: 'iso-codes.pc.in',
    output: 'iso-codes.pc',
    configuration: pkg_conf,
    install: true,
    install_dir: get_option('datadir') / 'pkgconfig',
)

# Custom targets to create deprecated .xml files from JSON data files
foreach domain : domains
    mytarget = custom_target(
        domain + '-xml',
        output: domain + '.xml',
        command: [
            xml_from_json,
            domain,
            meson.project_source_root() / 'data',
            '@OUTPUT@',
        ],
        install: true,
        install_dir: get_option('datadir') / 'xml' / meson.project_name(),
    )
endforeach

# Install symlinks for obsolete filenames
symlinks = {
    'iso_639.xml': 'iso_639-2.xml',
    'iso_639_3.xml': 'iso_639-3.xml',
    'iso_639_5.xml': 'iso_639-5.xml',
    'iso_3166_2.xml': 'iso_3166-2.xml',
    'iso_3166.xml': 'iso_3166-1.xml',
}

foreach linkname, original : symlinks
    install_symlink(
        linkname,
        pointing_to: original,
        install_dir: get_option('datadir') / 'xml' / meson.project_name(),
    )
endforeach
