# Changelog

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.8.0] – 2021-11-03

### Added

- ISO 3166-1: Add flag emoji to countries. Thanks to Pander
  for the suggestion. Fixes #19
- ISO 639-5: New translation for Chinese (Simplified)

### Changed

- ISO 3166-2: Major update of data.
  Thanks to the script of Kevin Kaiser, which enables
  the download of ISO pages and parses the data.
  Fixes #15, #16, #27
- Rename ChangeLog.md to CHANGELOG.md and follow the suggestions
  from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- Move all CHANGELOG entries from versions before 4.0 to an
  archive file (CHANGELOG-PRE-4.0.md) in order to reduce the
  massive size of this CHANGELOG.
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 15924


## 4.7.0 – 2021-08-25

### Added
- ISO 3166-1: Add common names for South and North Korea. Fixes #25

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 3166-3
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Fixed
- ISO 3166-1: Rename ku.po to kmr.po.
- ISO 3166-2: Updates for Indonesia. Fixes #20
- ISO 3166-3: Rename ku.po to kmr.po.
- Fix weblate check: Remove double spaces


## 4.6.0 – 2021-03-08

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 3166-3
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924


## 4.5.0 – 2020-05-19

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 3166-3
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Fixed
- ISO 3166-2: Update codes for Norway. Fixes #19
- ISO 3166-2: Update subdivision names for Belarus. Fixes #22


## 4.4 – 2019-10-03

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 3166-3
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Fixed
- ISO 3166-2: Fix code for Eastern Equatoria. Fixes #12
- ISO 3166-2: Remove MA- prefix from parent codes. Fixes #13
- ISO 3166-2: Update codes for Kenya. Fixes #15


## 4.3 – 2019-07-11

### Changed
- Translation updates for ISO 3166-1
  - Turkish by Atila KOÇ. Closes: #910350
- Translation updates for ISO 3166-2
- Translation updates for ISO 3166-3
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Fixed
- ISO 3166-1: Update names for GM (Gambia) and SZ (Eswatini).
  Fixes #10
- ISO 3166-1: Update names for MK (North Macedonia). Fixes #5
- ISO 3166-2: Update names and codes for CN (China) from iso.org.
  Closes: #910632
- ISO 3166-2: Update MA (Morocco) from iso.org. Fixes #9


## 4.2 – 2019-01-25

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Fixed

- ISO 3166-2: Update codes for MX (Mexico). Fixes #7


## 4.1 – 2018-09-18

**If you're maintaining a program which uses XML files,
please switch to the JSON data files.**

### Added
- The XML files have been re-added, because too many
  other programs still rely on those files.
- ISO 3166-2: Update codes for ZA-GT (Gauteng) and
  ZA-NL (Kwazulu-Natal). Fixes #6
- Translation updates for ISO 3166-3
- Translation updates for ISO 15924


## 4.0 – 2018-08-25

### Changed
- Translation updates for ISO 3166-1
- Translation updates for ISO 3166-2
- Translation updates for ISO 639-2
- Translation updates for ISO 639-3
- Translation updates for ISO 639-5
- Translation updates for ISO 4217
- Translation updates for ISO 15924

### Removed
- The XML files have been removed after having been deprecated for
  two and a half years. Please use the JSON data files instead.
