SUBDIRS = $(DOMAINS)

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

# For this release, just install the JSON files.
jsondir = $(pkgdatadir)/json
dist_json_DATA = $(wildcard $(srcdir)/data/*.json)

EXTRA_DIST = \
	LICENSE			\
	common.mk		\
	iso2pot.py		\
	check_valid_utf8.py

DISTCLEANFILES = $(pkgconfig_DATA)


.PHONY: release
release: update-po check distcheck

.PHONY: update-po
update-po:
	for domain in $(DOMAINS); do \
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
