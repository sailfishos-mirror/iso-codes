# Makefile to build ISOi_3166 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU Public License; see file COPYING for details
#   
#   $ Id: $

# Expect these to be overriden by top-level Makefile
PREFIX=/usr
VERSION=CVS

MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
INSTALL=install -m 644
MKDIR_P=mkdir -p
destdir=${PREFIX}/share/locale
XMLDIR=${PREFIX}/xml/iso-codes


all: ${MO_FILES}

install: all
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//' ` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_3166_2.mo ; \
	done
	${MKDIR_P} ${XMLDIR}
	$(INSTALL) iso_3166_2.xml $(XMLDIR)/iso_3166_2.xml


${MO_FILES}: iso_3166_2.pot

iso_3166_2.pot: iso_3166_2.xml
	../../iso2pot.py --is-version ${VERSION} --comment name \
		--fields name $< $@

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f  *~ *.mo iso_*.h
