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
SHAREDIR=$(PREFIX)/share/iso-codes

all: ${MO_FILES}

install: all
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//' ` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_3166_3.mo ; \
	done
	$(INSTALL) iso_3166_3.tab $(SHAREDIR)/iso_3166_3.tab

iso_3166_3.h: iso_3166_3.tab
	( cut -f1,5 iso_3166_3.tab | ../../tab2h.pl 1 2  - | grep -v N_\(\"\"\)  > iso_3166_3.h )

${MO_FILES}: iso_3166_3.h

%.pot: %.h
	xgettext --extract-all --output $@ --from-code=UTF-8  \
	  --no-location --add-comments $<

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f  *~ *.mo iso_*.h
