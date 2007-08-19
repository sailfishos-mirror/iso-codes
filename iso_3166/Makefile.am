SUBDIRS = iso_3166_2
DOMAIN = iso_3166
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

tabdir = $(datadir)/iso-codes
tab_DATA = $(DOMAIN).tab

iso_3166.tab: iso_3166.xml
	$(srcdir)/iso3166tab.py $< > iso_3166.tab.new
	LC_ALL=C sort < iso_3166.tab.new > iso_3166.tab
	rm -f iso_3166.tab.new

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

iso_3166.pot: iso_3166.xml
	../iso2pot.py --is-version $(VERSION) --comments alpha_3_code \
		--fields name,names,official_name,common_name --outfile $@ $<

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_3166.pot 	\
	iso3166tab.py

MOSTLYCLEANFILES = \
	$(mofiles) \
	$(tab_DATA)

check-local: check-content

include $(top_srcdir)/rules.make
