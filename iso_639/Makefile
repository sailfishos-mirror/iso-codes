# Makefile to build ISO-639 translation files
# 
#   Copyright (C) Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU License; see file COPYING for details

PREFIX=/usr

MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
MKDIR_P=mkdir -p
INSTALL=/usr/bin/install -m 644
SHAREDIR=${PREFIX}/share/iso-codes

includedir=${PREFIX}/include
destdir=${PREFIX}/share/locale

all: iso_639.pot ${MO_FILES}

install: ${HEADER_FILES} ${MO_FILES}
	${MKDIR_P} ${SHAREDIR}
	${INSTALL} iso_639.tab ${SHAREDIR}/iso_639.tab
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//'` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_639.mo ; \
	done

	

iso_639.h: iso_639.tab
	../tab2h.pl 1 4 iso_639.tab > iso_639.h

iso_639.pot: iso_639.h
	xgettext --extract-all --from-code=UTF-8 --no-location \
	 --output $@ --add-comments $<

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f *.pot *~ *.mo *.h
