# Makefile to build ISO-639 translation files
# 
#  Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#  Released under the GNU License; see file COPYING for details
#
#  $ Id: $

# The following are expected to be overruled by top-level makefile
PREFIX=/usr
VERSION=CVS


XMLDIR=${PREFIX}/share/xml/iso-codes
SHAREDIR=${PREFIX}/share/iso-codes
MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
MKDIR_P=mkdir -p
INSTALL=/usr/bin/install -m 644

destdir=${PREFIX}/share/locale

all: iso_639.pot ${MO_FILES}

install: iso_639.xml ${MO_FILES}
	${MKDIR_P} ${XMLDIR}
	${MKDIR_P} ${SHAREDIR}
	${INSTALL} iso_639.xml ${XMLDIR}/iso_639.xml
	${INSTALL} iso_639.tab ${SHAREDIR}/iso_639.tab
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//'` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_639.mo ; \
	done

iso_639.pot: iso_639.xml
	../iso2pot.py --is-version ${VERSION} --comments iso_639_2T_code \
		--fields name $< $@

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f *~ *.mo 
