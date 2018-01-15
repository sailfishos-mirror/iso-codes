SUBDIRS = $(DOMAINS)

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

# Install the JSON files.
jsondir = $(pkgdatadir)/json
dist_json_DATA = $(wildcard $(srcdir)/data/*.json)

# Include the "bin" directory, the bootstrap script,
# the common Makefile snippet
# and the markdown documentation currently not handled
# by automake
EXTRA_DIST = bin bootstrap common.mk README.md

DISTCLEANFILES = $(pkgconfig_DATA)

# Updates all pot files
.PHONY: pot
pot:
	for domain in $(DOMAINS); do \
		cd $$domain && make $$domain.pot && cd ..; \
	done

# Updates all xml files
.PHONY: xml
xml:
	for domain in $(DOMAINS); do \
		cd $$domain && make $$domain.xml && cd ..; \
	done

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
