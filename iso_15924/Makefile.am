DOMAIN = iso_15924

include $(top_srcdir)/common.mk

iso_15924.pot: iso_15924.xml
	../iso2pot.py --is-version ${VERSION}  --comments alpha_4_code \
		--fields name  --outfile $@ $<
