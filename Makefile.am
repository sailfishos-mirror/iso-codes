SUBDIRS = iso_639 iso_3166 iso_4217 notes

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

EXTRA_DIST = \
	$(pkgconfig_DATA)	\
	README			\
	TODO			\
	rules.make		\
	iso2pot.py		\
	iso2tab.py		\
	tab2h.pl		\
	debian/changelog       \
	debian/control         \
	debian/copyright       \
	debian/rules           \
	debian/watch

DISTCLEANFILES = $(pkgconfig_DATA)
