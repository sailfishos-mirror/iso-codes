xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

localedir = $(datadir)/locale

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	$(DOMAIN).pot

MOSTLYCLEANFILES = \
	$(mofiles)

# Generic target to create binary .mo files from .po files
%.mo: %.po
	$(MSGFMT) $(MSGFMT_FLAGS) -o $@ $<

# Generic target to create .pot files from JSON data files
$(DOMAIN).pot: $(top_srcdir)/data/$(DOMAIN).json
	python3 $(top_srcdir)/bin/pot_from_json.py $(DOMAIN) $(top_srcdir)/data

# Generic target to create deprecated .xml files from JSON data files
$(DOMAIN).xml: $(top_srcdir)/data/$(DOMAIN).json
	python3 $(top_srcdir)/bin/xml_from_json.py $(DOMAIN) $(top_srcdir)/data $@

# Used in the domain subdirectories for checking that
# all .po files contain UTF-8 data
check-local:
	python3 $(top_srcdir)/bin/check_valid_utf8.py $(pofiles)

# This target merges all po files with the current pot file,
# removes obsolete msgids and substitutes the Project-Id-Version
# header with the correct value
#
# NOTE:
# Removing obsolete msgids is not the recommended way to go.
# However, we've decided that in the specific case of iso-codes
# the benefit outweights the loss of information. Having only msgids
# with one (sometimes two or three) words, the fuzzy matching performed
# with obsolete msgids will not ease the translator's work, but
# will lead to confusing entries.
.PHONY: update-po
update-po:
	for pofile in $(pofiles); do \
		$(MSGMERGE) --no-fuzzy-matching $$pofile $(DOMAIN).pot > tmpfile; \
		$(MSGATTRIB) --no-obsolete tmpfile > $$pofile; \
		sed -i -e 's/^\"Project-Id-Version: iso.*/\"Project-Id-Version: $(DOMAIN)\\n\"/' $$pofile; \
	done
	rm -f tmpfile
	if [ -f sr.po ]; then \
		$(RECODE_SR_LATIN) < sr.po > sr@latin.po; \
		sed -i -e 's/^\"Language: sr\\n\"/\"Language: sr@latin\\n\"/' sr@latin.po; \
	fi
	if [ -f tt@iqtelif.po ]; then \
		$(MSGFILTER) --keep-header sed -f $(top_srcdir)/bin/recode-tt-cyrillic.sed < tt@iqtelif.po > tt.po; \
		sed -i -e 's/^\"Language: tt@iqtelif\\n\"/\"Language: tt\\n\"/' tt.po; \
	fi

install-data-hook: $(mofiles)
	$(mkinstalldirs) $(DESTDIR)$(localedir)
	catalogs='$(mofiles)'; \
	for cat in $$catalogs; do \
		cat=`basename $$cat`; \
		lang=`echo $$cat | sed 's/\.mo$$//'`; \
		dir=$(DESTDIR)$(localedir)/$$lang/LC_MESSAGES; \
		$(mkinstalldirs) $$dir; \
		$(INSTALL_DATA) $$cat $$dir/$(DOMAIN).mo; \
	done

uninstall-hook:
	catalogs='$(mofiles)'; \
	for cat in $$catalogs; do \
		cat=`basename $$cat`; \
		lang=`echo $$cat | sed 's/\.mo$$//'`; \
		rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(DOMAIN).mo; \
	done