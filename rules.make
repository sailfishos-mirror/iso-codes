
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

.PHONY: update-po
update-po:
	for pofile in $(pofiles); do \
		$(MSGMERGE) $$pofile $(DOMAIN).pot > tmpfile; \
		mv tmpfile $$pofile; \
	done

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
