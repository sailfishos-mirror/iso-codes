SUBDIRS = iso_3166_2

DOMAIN = iso_3166
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

tabdir = $(datadir)/iso-codes
tab_DATA = $(DOMAIN).tab

%.tab: %.xml
	$(srcdir)/iso3166tab.py $< | sort > $@

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

iso_3166.pot: iso_3166.xml
	../iso2pot.py --is-version $(VERSION) --comments alpha_3_code \
		--fields name,official_name,common_name $< $@

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso3166tab.py

MOSTLYCLEANFILES = \
	$(noinst_DATA)	\
	$(tab_DATA)

include $(top_srcdir)/rules.make
