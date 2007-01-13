#!/usr/bin/env python
"""
Parse the SIL.org iso-fdis-639-3_20061114.tab file and create
an XML file for our own use.

(Originally iso-dis-639-3_20050910.tab)
"""

f=open("iso-fdis-639-3_20061114.tab")

ot=open("iso_639_3.xml","w")

ot.write("""<?xml version="1.0" encoding="UTF-8" ?>

<!-- iso_639_3.xml							-->
<!-- 									-->
<!-- DRAFT DRAFT DRAFT							-->
<!-- iso-639-3 draft standard						-->
<!-- WARNING: The contents of this DRAFT standard will not be shipped   -->
<!-- in iso_639_3.xml in production releases of iso-codes; when the     -->
<!-- standard is released, the data will probably be folded into        -->
<!-- iso_639.xml. Please contact mckinstry@debian.org if you have any   -->
<!-- comments on the format of this data.			        -->

<!DOCTYPE iso_639_3_entries [
	<!ELEMENT iso_639_3_entries (iso_639_3_entry+)>
	<!ELEMENT iso_639_3_entry EMPTY>
	<!ATTLIST iso_639_3_entry
		id		CDATA	#REQUIRED
		name		CDATA	#REQUIRED
		type		CDATA	#REQUIRED
		scope 		CDATA   #REQUIRED
		iso_639_1_code	CDATA	#IMPLIED
		iso_639_2B_code	CDATA	#IMPLIED
		iso_639_2T_code	CDATA	#IMPLIED
	>
]>

<iso_639_3_entries>
""")

f.readline()		# throw away the header
for li in f.readlines():
	(id,part2b,part2t,part1,scope,type,name) = li.split('\t')
	name  = name.strip()
	ot.write('\t<iso_639_3_entry\n')
	ot.write('\t\tid="%s"\n' % id)
	if part1 != '':
		ot.write('\t\tiso_639_1_code="%s"\n' % part1)
	if part2b != '':
		ot.write('\t\tiso_639_2B_code="%s"\n' % part2b)
	if part2t != '':
		ot.write('\t\tiso_639_2T_code="%s"\n' % part2t)
	ot.write('\t\tscope="%s"\n' % scope)
	ot.write('\t\ttype="%s"\n' % type)
	ot.write('\t\tname="%s" />\n' % name)

ot.write('</iso_639_3_entries>')
ot.close()
f.close()
	
	

