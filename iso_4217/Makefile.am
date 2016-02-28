DOMAIN = iso_4217

include $(top_srcdir)/common.mk

iso_4217.pot: iso_4217.xml
	../iso2pot.py --is-version ${VERSION}  --comments letter_code \
		--fields currency_name  --outfile $@ $< 
