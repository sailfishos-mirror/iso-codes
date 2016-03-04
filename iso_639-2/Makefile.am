DOMAIN = iso_639-2

include $(top_srcdir)/common.mk

iso_639.pot: iso_639.xml
	$(top_srcdir)/iso2pot.py --is-version $(VERSION) \
		--comments iso_639_2T_code \
		--comments iso_639_1_code \
	        --fields name,common_name --outfile $@ iso_639.xml
