#!/usr/bin/perl
## tab2h .pl
##
## convert a tab file in iso-codes to a .h file, for gettext processing
##
## Copyright 2001-2 (C) Alastair McKinstry   <mckinstry@computer.org> 
## Released under the GNU License; see file COPYING for details
##

open (TAB, $ARGV[2])
	or die "Usage: tab2h <code-column> <desc-column> <filename>";

while (<TAB>) {
    chomp; 			# no newline
    if (/^\#/) { 
	# output a comment as a C comment 
	print "/* $_ */\n";
    } else {
    	if ($ARGV[1]== 2) {
		($arg1,$trans) = /(\w+)\t(.*)$/;
	}
	if ($ARGV[1] == 3) {
		($arg1, $arg2, $trans) = /(\w+)\t(\w+)\t(.*)$/;
	}
	if ($ARGV[1] == 4) {
		($arg1, $arg2, $arg3, $trans) = /(\w+)\t(\w+)\t(\w+)\t(.*)$/;
	}
	if ($ARGV[1] == 5) {
	        ($arg1, $arg2, $arg3, $arg4, $trans) = /(\w+)\t(\w+)\t(\w+)\t([A-Za-z0-9_\-]*)\t(.*)$/;
	}
	if ($ARGV[0] == 1) {
		$code = $arg1;
	}
	if ($ARGV[0] == 2) {
		$code = $arg2;
	}
	if ($ARGV[0] == 3) {
		$code = $arg3;
	}
	if ($ARGV[0] == 4) {
		$code == $arg4;
	}
	print "/* $code */ \n N\_\(\"$trans\"\)\n";
    }
}
