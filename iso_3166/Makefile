# mAKEFILE to build ISO_3166 translation files
# 
#   Copyright (C) 2003,2004 Alastair McKinstry   <mckinstry@computer.org> 
#   Released under the GNU Public License; see file COPYING for details

PREFIX=/usr
VERSION=CVS

MO_FILES = $(patsubst %.po,%.mo, $(wildcard *.po))
TARGETS=$(patsubst %,${INSTALL_DIR}/%, ${MO_FILES})
INSTALL=install -m 644
MKDIR_P=mkdir -p
destdir=${PREFIX}/share/locale
SHAREDIR=${PREFIX}/share/iso-codes
XMLDIR=${PREFIX}/share/xml/iso-codes
SUBDIRS=iso_3166_2 

all: iso_3166.pot ${MO_FILES}
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d all ; done

install: all iso_3166.tab
	${MKDIR_P} ${SHAREDIR}
	${MKDIR_P} ${XMLDIR}
	${INSTALL} iso_3166.tab ${SHAREDIR}
	${INSTALL} iso_3166.xml ${XMLDIR}
	for d in ${MO_FILES} ; do \
		lang=`basename $$d | sed 's/.mo$$//' ` ; \
		dir=${destdir}/$$lang/LC_MESSAGES ; \
		${MKDIR_P} $$dir ; \
		${INSTALL} $$d $$dir/iso_3166.mo ; \
	done
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d install ; done

iso_3166.tab: iso_3166.xml
	./iso3166tab.py iso_3166.xml | sort > iso_3166.tab

iso_3166.pot: iso_3166.xml
	../iso2pot.py --is-version $(VERSION) --comments alpha_3_code \
		--fields name,official_name,common_name $< $@

%.mo: %.po
	msgfmt --verbose --check $< -o $@

clean: 
	rm -f *~ *.mo iso_3166.tab
	for d in ${SUBDIRS}; do ${MAKE} -C $$d clean ; done
