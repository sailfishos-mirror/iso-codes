%.pot: %.xml
	$(top_srcdir)/iso2pot.py --is-version $(VERSION) --comments iso_639_2T_code \
		--fields name $< $@

%.mo: %.po
	$(MSGFMT) --verbose --check $< -o $@

localedir = $(datadir)/locale

install-data-hook: $(mofiles)
	$(mkinstalldirs) $(DESTDIR)$(datadir)
	$(mkinstalldirs) $(DESTDIR)$(localedir)
	catalogs='$(mofiles)'; \
	for cat in $$catalogs; do \
		cat=`basename $$cat`; \
		lang=`echo $$cat | sed 's/\.mo$$//'`; \
		dir=$(DESTDIR)$(localedir)/$$lang/LC_MESSAGES; \
		$(INSTALL_DATA) -D $$cat $$dir/$(DOMAIN).mo; \
	done

uninstall-hook:
	catalogs='$(mofiles)'; \
	for cat in $$catalogs; do \
		cat=`basename $$cat`; \
		lang=`echo $$cat | sed 's/\.mo$$//'`; \
		rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(DOMAIN).mo; \
	done
