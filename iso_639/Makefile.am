DOMAIN = iso_639
VERSION=@PACKAGE_VERSION@

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

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	$(tab_DATA)

MOSTLYCLEANFILES = \
	$(noinst_DATA)

include $(top_srcdir)/rules.make
