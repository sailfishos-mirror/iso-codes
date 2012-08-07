SUBDIRS = iso_15924 iso_3166 iso_3166_2 iso_4217 iso_639 iso_639_3

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

EXTRA_DIST = \
	LICENSE			\
	rules.make		\
	iso2pot.py		\
	check_valid_utf8.pl

DISTCLEANFILES = $(pkgconfig_DATA)


.PHONY: release
release: update-po check distcheck

.PHONY: update-po
update-po:
	for domain in $(SUBDIRS); do \
		cd $$domain && make update-po && cd ..; \
	done

.PHONY: sign-release
sign-release: iso-codes-$(VERSION).tar.xz
	rm -f iso-codes-$(VERSION).tar.xz.sig
	gpg --detach-sign iso-codes-$(VERSION).tar.xz

.PHONY: upload
upload:
	@if [[ -f "iso-codes-$(VERSION).tar.xz" ]] \
	&& [[ -f "iso-codes-$(VERSION).tar.xz.sig" ]]; then \
		scp iso-codes-$(VERSION).tar.* \
		alioth.debian.org:/srv/home/groups/pkg-isocodes/htdocs/downloads; \
	fi
