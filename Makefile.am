SUBDIRS = iso_639 iso_3166 iso_4217 notes

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

EXTRA_DIST = \
	$(pkgconfig_DATA)	\
	LGPL-2.1		\
	rules.make		\
	iso2pot.py

DISTCLEANFILES = $(pkgconfig_DATA)


.PHONY: release
release: check distcheck
	rm -f iso-codes-$(VERSION).tar.gz.sig
	rm -f iso-codes-$(VERSION).tar.bz2.sig
	gpg --detach-sign iso-codes-$(VERSION).tar.gz
	gpg --detach-sign iso-codes-$(VERSION).tar.bz2

.PHONY: upload
upload:
	@if [[ "$(ALIOTH_USERNAME)" == "" ]]; then \
		echo "Please set your Alioth username. Example command line:"; \
		echo "  ALIOTH_USERNAME=toddy-guest make upload"; \
	fi
	@if [[ -f "iso-codes-$(VERSION).tar.gz" ]] \
	&& [[ -f "iso-codes-$(VERSION).tar.bz2" ]] \
	&& [[ -f "iso-codes-$(VERSION).tar.gz.sig" ]] \
	&& [[ -f "iso-codes-$(VERSION).tar.bz2.sig" ]] \
	&& [[ -n "$(ALIOTH_USERNAME)" ]]; then \
		scp iso-codes-$(VERSION).tar.* \
		$(ALIOTH_USERNAME)@alioth.debian.org:/var/lib/gforge/chroot/ftproot/pub/pkg-isocodes; \
	fi
