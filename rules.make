
%.mo: %.po
	$(MSGFMT) $(MSGFMT_FLAGS) -o $@ $<

.PHONY: check-content
check-content:
	@grep "Content-Type" *po | grep -v "UTF-8" && touch found-non-utf.stamp || true
	@if [ -e found-non-utf.stamp ]; then \
		echo "*********"; \
		echo "* Error *"; \
		echo "*********"; \
		echo "At least one file is not encoded in UTF-8. Please check."; \
		rm -f found-non-utf.stamp; \
		false; \
	fi

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
		$(MSGMERGE) $$pofile $(DOMAIN).pot > tmpfile; \
		msgattrib --no-obsolete tmpfile > $$pofile; \
		sed -i -e 's/^\"Project-Id-Version: iso.*/\"Project-Id-Version: $(DOMAIN) $(VERSION)\\n\"/' $$pofile; \
	done
	rm -f tmpfile

localedir = $(datadir)/locale

install-data-hook: $(mofiles)
	$(mkinstalldirs) $(DESTDIR)$(datadir)
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
