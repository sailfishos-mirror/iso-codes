DOMAIN = iso_3166

include $(top_srcdir)/common.mk

iso_3166.pot: iso_3166.xml
	../iso2pot.py --is-version $(VERSION) --comments alpha_3_code \
		--fields name,names,official_name,common_name --outfile $@ $<
