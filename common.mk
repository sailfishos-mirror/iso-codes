xmldir = $(datadir)/xml/iso-codes
nodist_xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

localedir = $(datadir)/locale

EXTRA_DIST = \
	$(pofiles)	\
	$(DOMAIN).pot

MOSTLYCLEANFILES = \
	$(mofiles) \
	$(DOMAIN).xml

# Generic target to create binary .mo files from .po files
%.mo: %.po
	$(MSGFMT) $(MSGFMT_FLAGS) -o $@ $<

# Generic target to create .pot files from JSON data files
$(DOMAIN).pot: $(top_srcdir)/bin/pot_from_json.py $(top_srcdir)/data/$(DOMAIN).json $(top_srcdir)/bin/remove-potcdate.sin
	cp $@ backup.pot
	python3 $(top_srcdir)/bin/pot_from_json.py $(DOMAIN) $(top_srcdir)/data
	sed -f $(top_srcdir)/bin/remove-potcdate.sin < $@ > $(DOMAIN).1po
	sed -f $(top_srcdir)/bin/remove-potcdate.sin < backup.pot > $(DOMAIN).2po
	if cmp $(DOMAIN).1po $(DOMAIN).2po >/dev/null 2>&1; then \
		rm -f $(DOMAIN).1po $(DOMAIN).2po $@ && \
		mv backup.pot $@; \
	else \
		rm -f $(DOMAIN).1po $(DOMAIN).2po backup.pot; \
	fi

# Generic target to create deprecated .xml files from JSON data files
$(DOMAIN).xml: $(top_srcdir)/bin/xml_from_json.py $(top_srcdir)/data/$(DOMAIN).json
	python3 $(top_srcdir)/bin/xml_from_json.py $(DOMAIN) $(top_srcdir)/data $@

# Used in the domain subdirectories for checking that
# all .po files contain UTF-8 data
check-local:
	python3 $(top_srcdir)/bin/check_valid_utf8.py $(pofiles)

# This target merges all po files with the current pot file,
# removes obsolete msgids and substitutes the Project-Id-Version
# header with the PROJECT only, removing the VERSION part.
# This is done to keep the diff between releases small.
#
# NOTE:
# Removing obsolete msgids is not the recommended way to go.
# However, we've decided that in the specific case of iso-codes
# the benefit outweights the loss of information. Having only msgids
# with one (sometimes two or three) words, the fuzzy matching performed
# with obsolete msgids will not ease the translator's work, but
# will lead to confusing entries.
#
# However, if there is only a small change, we include the fuzzy
# entry with the previous msgid to hopefully save some work.
.PHONY: update-po
update-po:
	for pofile in $(pofiles); do \
		$(MSGMERGE) --previous $$pofile $(DOMAIN).pot > tmpfile; \
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
		if [ "$(DOMAIN)" = "iso_639-2" ]; then (cd $$dir && $(LN_S) $(DOMAIN).mo iso_639.mo); fi; \
		if [ "$(DOMAIN)" = "iso_639-3" ]; then (cd $$dir && $(LN_S) $(DOMAIN).mo iso_639_3.mo); fi; \
		if [ "$(DOMAIN)" = "iso_639-5" ]; then (cd $$dir && $(LN_S) $(DOMAIN).mo iso_639_5.mo); fi; \
		if [ "$(DOMAIN)" = "iso_3166-1" ]; then (cd $$dir && $(LN_S) $(DOMAIN).mo iso_3166.mo); fi; \
		if [ "$(DOMAIN)" = "iso_3166-2" ]; then (cd $$dir && $(LN_S) $(DOMAIN).mo iso_3166_2.mo); fi; \
	done
	if [ "$(DOMAIN)" = "iso_639-2" ]; then (cd $(DESTDIR)$(xmldir) && $(LN_S) $(DOMAIN).xml iso_639.xml); fi
	if [ "$(DOMAIN)" = "iso_639-3" ]; then (cd $(DESTDIR)$(xmldir) && $(LN_S) $(DOMAIN).xml iso_639_3.xml); fi
	if [ "$(DOMAIN)" = "iso_639-5" ]; then (cd $(DESTDIR)$(xmldir) && $(LN_S) $(DOMAIN).xml iso_639_5.xml); fi
	if [ "$(DOMAIN)" = "iso_3166-1" ]; then (cd $(DESTDIR)$(xmldir) && $(LN_S) $(DOMAIN).xml iso_3166.xml); fi
	if [ "$(DOMAIN)" = "iso_3166-2" ]; then (cd $(DESTDIR)$(xmldir) && $(LN_S) $(DOMAIN).xml iso_3166_2.xml); fi

uninstall-hook:
	catalogs='$(mofiles)'; \
	for cat in $$catalogs; do \
		cat=`basename $$cat`; \
		lang=`echo $$cat | sed 's/\.mo$$//'`; \
		rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(DOMAIN).mo; \
		if [ "$(DOMAIN)" = "iso_639-2" ]; then rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/iso_639.mo; fi; \
		if [ "$(DOMAIN)" = "iso_639-3" ]; then rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/iso_639_3.mo; fi; \
		if [ "$(DOMAIN)" = "iso_639-5" ]; then rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/iso_639_5.mo; fi; \
		if [ "$(DOMAIN)" = "iso_3166-1" ]; then rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/iso_3166.mo; fi; \
		if [ "$(DOMAIN)" = "iso_3166-1" ]; then rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/iso_3166_2.mo; fi; \
	done
	if [ "$(DOMAIN)" = "iso_639-2" ]; then rm -f $(DESTDIR)$(xmldir)/iso_639.xml; fi
	if [ "$(DOMAIN)" = "iso_639-3" ]; then rm -f $(DESTDIR)$(xmldir)/iso_639_3.xml; fi
	if [ "$(DOMAIN)" = "iso_639-5" ]; then rm -f $(DESTDIR)$(xmldir)/iso_639_5.xml; fi
	if [ "$(DOMAIN)" = "iso_3166-1" ]; then rm -f $(DESTDIR)$(xmldir)/iso_3166.xml; fi
	if [ "$(DOMAIN)" = "iso_3166-2" ]; then rm -f $(DESTDIR)$(xmldir)/iso_3166_2.xml; fi
