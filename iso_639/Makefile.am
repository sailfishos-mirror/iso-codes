DOMAIN = iso_639
VERSION= @PACKAGE_VERSION@
SUBDIRS = iso_639_3

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml iso_639_3.xml

tabdir = $(datadir)/iso-codes
tab_DATA = $(DOMAIN).tab

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) iso_639.pot

iso_639.pot: iso_639.xml
	$(top_srcdir)/iso2pot.py --is-version $(VERSION) --comments iso_639_2T_code \
	                --fields name --outfile $@ iso_639.xml

iso_639_3.xml:
	$(top_srcdir)/iso_639/iso-dis-639-tab-parse.py 

iso_639.tab: iso_639.xml
	LC_ALL=C $(srcdir)/iso639tab.py $< > iso_639.tab

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	$(tab_DATA)	\
	iso_639.pot

MOSTLYCLEANFILES = \
	$(mofiles) \
	$(tab_DATA)

check-local: check-content

include $(top_srcdir)/rules.make
