#!/usr/bin/make -f
#
# Top-level Makefile for iso-codes

# These may be overridden by values from debian/rules, etc.
PREFIX=/usr
PREFIX_QUOTED=\/usr
VERSION=0.35

DOMAINS=iso_3166 iso_639 iso_4217 iso_3166_2 

SUBDIRS=iso_3166 iso_639 iso_4217

all: iso-codes.pc
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d all; done

clean:
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d clean ; done
	rm -f iso-codes.pc

install: iso-codes.pc
	for d in ${SUBDIRS} ; do ${MAKE} -C $$d install ; done
	mkdir -p ${PREFIX}/lib/pkgconfig
	cp iso-codes.pc ${PREFIX}/lib/pkgconfig/iso-codes.pc


iso-codes.pc: iso-codes.pc.in
	sed     -e 's/@VERSION@/${VERSION}/' \
		-e 's/@DOMAINS@/${DOMAINS}/' \
		-e 's/@PREFIX@/${PREFIX_QUOTED}/' <  $< > $@

