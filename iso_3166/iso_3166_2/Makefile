# Makefile to build ISOi_3166 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU Public License; see file COPYING for details

PREFIX=/usr

MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
INSTALL=install -m 644
MKDIR_P=mkdir -p
destdir=${PREFIX}/share/locale


all: ${MO_FILES}

install: all
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//' ` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_3166_2.mo ; \
	done

iso_3166_2.h: ../iso_3166_2.tab
	../../tab2h.pl 1 2 ../iso_3166_2.tab > iso_3166_2.h

${MO_FILES}: iso_3166_2.h

%.pot: %.h
	xgettext --extract-all --output $@ --from-code=UTF-8 --add-comments $<

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f  *~ *.mo iso_*.h
