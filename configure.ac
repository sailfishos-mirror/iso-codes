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

AC_INIT([iso-codes],[3.79])

AM_INIT_AUTOMAKE([dist-xz no-dist-gzip foreign])
AM_MAINTAINER_MODE

AC_PROG_INSTALL
AC_PROG_LN_S

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

DOMAINS="iso_639-2 iso_639-3 iso_639-5 iso_3166-1 iso_3166-2 iso_3166-3 iso_4217 iso_15924"
AC_SUBST([DOMAINS])

AC_CONFIG_FILES([
  Makefile
  iso-codes.pc
  iso_639-2/Makefile
  iso_639-3/Makefile
  iso_639-5/Makefile
  iso_3166-1/Makefile
  iso_3166-2/Makefile
  iso_3166-3/Makefile
  iso_4217/Makefile
  iso_15924/Makefile
])

AC_OUTPUT
