# Makefile to build ISO_4217 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU License; see file COPYING for details



TAB_FILE=iso_4217.tab
MO_FILES=$(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
MKDIR_P=mkdir -p
INSTALL=/usr/bin/install -m 644 
destdir=${PREFIX}/share/locale
sharedir=${PREFIX}/share/iso-codes/

all: ${MO_FILES}

install: ${TAB_FILE} ${MO_FILES}
	${MKDIR_P} ${sharedir}
	${INSTALL} iso_4217.tab ${sharedir}/iso_4217.tab	
	${INSTALL} iso_4217_historic.tab ${sharedir}/iso_4217_historic.tab
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//'` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_4217.mo ; \
	done

iso_4217.h: iso_4217.tab
	../tab2h.pl 1 3 iso_4217.tab > iso_4217.h

iso_4217.pot: iso_4217.h
	xgettext --extract-all --output $@ --add-comments $<

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f *.pot *~ *.mo *.h

