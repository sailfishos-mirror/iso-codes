SUBDIRS = iso_639 iso_3166 iso_4217 notes

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

EXTRA_DIST = \
	$(pkgconfig_DATA)	\
	LGPL-2.1		\
	rules.make		\
	iso2pot.py

DISTCLEANFILES = $(pkgconfig_DATA)
