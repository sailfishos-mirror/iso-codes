# Makefile to build ISO_3166 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU Public License; see file COPYING for details

PREFIX=/usr

MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
INSTALL=install -m 644
MKDIR_P=mkdir -p
destdir=${PREFIX}/share/locale
SHAREDIR=${PREFIX}/share/iso-codes
SUBDIRS=iso_3166_1 iso_3166_2 iso_3166_3

all: iso_3166.pot ${MO_FILES}
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d all ; done

install: all
	${MKDIR_P} ${SHAREDIR}
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//' ` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_3166.mo ; \
	done
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d install ; done

iso_3166.h: iso_3166.tab
	../tab2h.pl 1 2 iso_3166.tab > iso_3166.h

%.pot: %.h
	xgettext --extract-all --output $@  --from-code=UTF-8 \
	  --no-location --add-comments $<

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f iso_3166.pot *~ *.mo 
	for d in ${SUBDIRS}; do ${MAKE} -C $$d clean ; done
