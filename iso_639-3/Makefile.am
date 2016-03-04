DOMAIN = iso_639_3

include $(top_srcdir)/common.mk

iso_639_3.pot: iso_639_3.xml
	../iso2pot.py --is-version ${VERSION} --comment id \
		--fields name,inverted_name,reference_name,common_name --outfile $@ $< 
