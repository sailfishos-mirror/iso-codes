# Process this file with autoconf to produce a configure script.
#
# Copyright © 2003-2004 Christian Persch
# Copyright © 2006-2016 Dr. Tobias Quathamer
#
# This file is part of iso-codes.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA

AC_INIT([iso-codes],[3.65])

AM_INIT_AUTOMAKE([dist-xz no-dist-gzip foreign])
AM_MAINTAINER_MODE

AC_SUBST([ACLOCAL_AMFLAGS], ["\${ACLOCAL_FLAGS}"])

AC_PROG_INSTALL
AC_PROG_MAKE_SET

AC_PATH_PROG([MSGMERGE],[msgmerge])
AC_PATH_PROG([MSGFMT],[msgfmt])
AC_PATH_PROG([MSGFILTER],[msgfilter])
AC_PATH_PROG([MSGATTRIB],[msgattrib])
AC_PATH_PROG([RECODE_SR_LATIN],[recode-sr-latin])
AC_MSG_CHECKING([if $MSGFMT is GNU msgfmt])
gnu_msgfmt=no
MSGFMT_FLAGS=
if $MSGFMT --version 2>&1 | grep GNU > /dev/null; then
  gnu_msgfmt=yes
  MSGFMT_FLAGS="--verbose --check"
fi
AC_MSG_RESULT($gnu_msgfmt)
AC_SUBST(MSGFMT_FLAGS)

DOMAINS="iso_15924 iso_3166 iso_4217 iso_639 iso_3166_2 iso_639_3 iso_639_5"
AC_SUBST([DOMAINS])

AC_CONFIG_FILES([
  Makefile
  iso-codes.pc
  iso_15924/Makefile
  iso_3166/Makefile
  iso_3166_2/Makefile
  iso_4217/Makefile
  iso_639/Makefile
  iso_639_3/Makefile
  iso_639_5/Makefile
])

AC_OUTPUT
