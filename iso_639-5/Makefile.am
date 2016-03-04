DOMAIN = iso_639_5

include $(top_srcdir)/common.mk

iso_639_5.pot: iso_639_5.xml
	../iso2pot.py --is-version ${VERSION} --comment id \
		--fields name --outfile $@ $< 
