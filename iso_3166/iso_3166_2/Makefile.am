DOMAIN = iso_3166_2

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml


pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot) 

iso_3166_2.pot: iso_3166_2.xml
	../../iso2pot.py --is-version ${VERSION} --comment code \
		--fields name $< $@

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	

MOSTLYCLEANFILES = \
	$(noinst_DATA)

include $(top_srcdir)/rules.make
