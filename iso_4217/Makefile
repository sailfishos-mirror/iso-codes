# Makefile to build ISO_4217 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU License; see file COPYING for details


XMLDIR=${PREFIX}/share/xml/iso-codes
TAB_FILE=iso_4217.tab
MO_FILES=$(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
MKDIR_P=mkdir -p
INSTALL=/usr/bin/install -m 644 
destdir=${PREFIX}/share/locale
VERSION=CVS

all: ${MO_FILES}

install:  ${MO_FILES}
	${MKDIR_P} ${XMLDIR}
	${INSTALL} iso_4217.xml ${XMLDIR}/iso_4217.xml
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//'` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_4217.mo ; \
	done


iso_4217.pot: iso_4217.xml
	../iso2pot.py --is-version ${VERSION}  --comments letter_code \
		--fields currency_name  $< $@

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f *~ *.mo 

