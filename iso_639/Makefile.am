DOMAIN = iso_639

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

tabdir = $(datadir)/iso-codes
tab_DATA = $(DOMAIN).tab

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

%.pot: %.xml
	$(top_srcdir)/iso2pot.py --is-version $(VERSION) --comments iso_639_2T_code \
	                --fields name $< $@

iso_639.tab: iso_639.xml
	$(srcdir)/iso639tab.py $< > iso_639.tab.new
	LC_ALL=C sort < iso_639.tab.new > iso_639.tab
	rm -f iso_639.tab.new

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	$(tab_DATA)

MOSTLYCLEANFILES = \
	$(noinst_DATA)	\
	$(tab_DATA)

include $(top_srcdir)/rules.make
