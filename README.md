# iso-codes

https://salsa.debian.org/iso-codes-team/iso-codes

This project provides lists of various ISO standards (e.g. country,
language, language scripts, and currency names) in one place, rather
than repeated in many programs throughout the system.

Currently there are lists of languages and countries embedded in
several different programs, which leads to dozens of lists of
200 languages, translated into more than 90 languages ... not
very efficient.

With this project, we create a single "gettext domain" for every
supported ISO standard which contains the translations of
that domain. It is easy for a programmer to re-use those
translations instead of maintaining their own translation
infrastructure. Moreover, the programmer does not need to follow
changes in the ISO standard and will not work with outdated
information.

To use this translation infrastructure, the programmer just needs
to call `dgettext()` in their program.

Example:

```
dgettext("iso_639-2", "French")
```

will return the translation for "French", depending on the
current locale.

Furthermore, this project provides the ISO standards as JSON files
to be used by other applications as well. All those JSON files
are stored in the directory "/usr/share/iso-codes/json".

# Status of translations

Below you can see the current translation status, with the two most
important gettext domains listed first (countries and languages).

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-3166-1/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-639-2/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

The other gettext domains are also useful, but probably
not as important as the first two.

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-4217/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-3166-2/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-3166-3/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-639-3/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-639-5/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

[![Translation status](https://hosted.weblate.org/widgets/iso-codes/-/iso-15924/287x66-white.png)](https://hosted.weblate.org/engage/iso-codes/?utm_source=widget)

# NEWS

* A new ISO standard has been included, ISO 3166-3. The gettext
  domain is called `iso_3166-3`. Basically, this is a split of the
  old domain `iso_3166` into `iso_3166-1` and `iso_3166-3`, because
  the old domain `iso_3166` contained both standards. However, the
  standard ISO 3166-3 was more or less inaccessible.
* The standard ISO 4217 (currency names) now includes only the
  currently used currencies. Entries of withdrawn currencies are
  no longer included.
* The standard ISO 639-5 now includes only the language families
  which are part of the official standard. The previously
  included languages were not part of the standard and have been
  removed. This reduced the number of language families from
  about 1900 to about 110.
* The XML files are **deprecated** and should not be used for new
  projects. However, they are kept in sync with the JSON data
  for now.
* The gettext domains have been renamed to better match the
  actual ISO number:
  - ISO 639-2: Renamed from `iso_639` to `iso_639-2`
  - ISO 639-3: Renamed from `iso_639_3` to `iso_639-3`
  - ISO 639-5: Renamed from `iso_639_5` to `iso_639-5`
  - ISO 3166-1: Renamed from `iso_3166` to `iso_3166-1`
  - ISO 3166-2: Renamed from `iso_3166_2` to `iso_3166-2`

  All previously used gettext domains are linked to the new
  domain names, so that this transition should be smooth for
  programs using those domain names.


## ISO 639-2

This lists the 2-letter and 3-letter language codes and language
names. The official ISO 639-2 maintenance agency is the Library of
Congress. The gettext domain is "iso_639-2".

<http://www.loc.gov/standards/iso639-2/>


## ISO 639-3

This is a further development of ISO 639-2, see above. All codes
of ISO 639-2 are included in ISO 639-3. ISO 639-3 attempts to
provide as complete an enumeration of languages as possible,
including living, extinct, ancient, and constructed languages,
whether major or minor, written or unwritten. The gettext
domain is "iso_639-3". The official ISO 639-3 maintenance agency
is SIL International.

<http://www.sil.org/iso639-3/>


## ISO 639-5

This standard is highly incomplete list of alpha-3 codes
for language families and groups. The official ISO 639-5 maintenance
agency is the Library of Congress. The gettext domain is "iso_639-5".

<http://www.loc.gov/standards/iso639-5/>


## ISO 3166-1

This lists the 2-letter country code and "short" country name. The
official ISO 3166-1 maintenance agency is ISO. The gettext domain is
"iso_3166-1".

<http://www.iso.org/iso/country_codes>


## ISO 3166-2

The ISO 3166 standard includes a "Country Subdivision Code",
giving a code for the names of the principal administrative
subdivisions of the countries coded in ISO 3166. The official
ISO 3166-2 maintenance agency is ISO. The gettext domain is
"iso_3166-2".

<http://www.iso.org/iso/country_codes>


## ISO 3166-3

The ISO 3166-3 standard defines codes for country names which
have been removed from ISO 3166-1. The official ISO 3166-3
maintenance agency is ISO. The gettext domain is "iso_3166-3".

<http://www.iso.org/iso/country_codes>


## ISO 4217

This lists the currency codes and names. The official ISO 4217
maintenance agency is the Swiss Association for Standardization.
The gettext domain is "iso_4217".

<http://www.currency-iso.org/en/home.html>


## ISO 15924

This lists the language scripts names. The official ISO 15924
maintenance agency is the Unicode Consortium. The gettext
domain is "iso_15924".

<http://unicode.org/iso15924/>


# Tracking updates to the various ISO standards

Below is a list of websites we use to check for updates to the
standards.

ISO 639-2:
<http://www.loc.gov/standards/iso639-2/php/code_changes.php>

ISO 639-3:
<http://www-01.sil.org/iso639-3/changes.asp>

ISO 639-5:
<http://www.loc.gov/standards/iso639-5/changes.php>

ISO 3166-1, ISO 3166-2, and ISO 3166-3:
<http://www.iso.org/iso/country_codes>

ISO 4217:
<http://www.currency-iso.org/en/home/tables/table-a1.html>

ISO-15924:
<http://unicode.org/iso15924/codechanges.html>


# Adding or updating translations

The iso-codes project uses the Weblate translation service
as the primary way of managing translations.
You can find more information about this on the website:

<https://hosted.weblate.org/projects/iso-codes/>

You can also send your translation as a bug report against the package
iso-codes to the Debian Bug Tracking System. You can either send an email
or use the tool reportbug. More details are on this website:

<https://bugs.debian.org/>


# Reporting a bug

If you find a bug in iso-codes, there are several ways to contact us.

* Salsa issues

  <https://salsa.debian.org/iso-codes-team/iso-codes/issues>

  This system can be accessed via webbrowser.
* Debian Bug Tracking System

  <https://bugs.debian.org/>

  This system can be accessed via e-mail.


# Developing using pkgconfig

A pkgconfig file has been included to aid developing with this
project. You can detect the prefix where the translations have
been placed using

```
$ pkg-config --variable=prefix iso-codes
/usr
```

You can detect which gettext domains have been installed using

```
$ pkg-config --variable=domains iso-codes
iso_639-2 iso_639-3 iso_639-5 iso_3166-1 iso_3166-2 iso_3166-3 iso_4217 iso_15924
```
