DOMAIN = iso_4217

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot) 

iso_4217.pot: iso_4217.xml
	../iso2pot.py --is-version ${VERSION}  --comments letter_code \
		--fields currency_name  $< $@

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)

MOSTLYCLEANFILES = \
	$(noinst_DATA)

include $(top_srcdir)/rules.make
