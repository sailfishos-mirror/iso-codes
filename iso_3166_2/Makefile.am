DOMAIN = iso_3166_2
VERSION = @PACKAGE_VERSION@

include $(top_srcdir)/common.mk

iso_3166_2.pot: iso_3166_2.xml
	../iso2pot.py --is-version ${VERSION} --comment code \
		--fields name --outfile $@ $< 
