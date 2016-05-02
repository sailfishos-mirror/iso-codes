#!/usr/bin/env python3
#
# Create deprecated iso-codes XML from JSON
#
# Copyright © 2016 Dr. Tobias Quathamer <toddy@debian.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import json
import sys

# Get the current ISO code domain, the path to the JSON data dir, and the XML output file
if len(sys.argv) != 4:
    sys.exit("Please provide the domain, the path to the JSON data dir, and the XML output file.")
domain = sys.argv[1]
datapath = sys.argv[2]
xml_file = sys.argv[3]

#
# Define the headers of the XML files
#
headers = {
    "639": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all languages in the ISO 639
standard, and is used to provide translations via gettext

Copyright (C) 2004-2006 Alastair McKinstry <mckinstry@computer.org>
Copyright (C) 2004-2012 Christian Perrier <bubulle@debian.org>
Copyright (C) 2005-2008 Tobias Quathamer <toddy@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.loc.gov/standards/iso639-2/>
-->

<!DOCTYPE iso_639_entries [
	<!ELEMENT iso_639_entries (iso_639_entry+)>
	<!ELEMENT iso_639_entry EMPTY>
	<!ATTLIST iso_639_entry
		iso_639_2B_code		CDATA	#REQUIRED
		iso_639_2T_code		CDATA	#REQUIRED
		iso_639_1_code		CDATA	#IMPLIED
		name			CDATA	#REQUIRED
		common_name		CDATA	#IMPLIED
	>
]>
""",
    "639-3": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all languages in the ISO 639-3
standard, and is used to provide translations via gettext

Copyright © 2005 Alastair McKinstry <mckinstry@computer.org>
Copyright © 2008,2012,2013 Tobias Quathamer <toddy@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.sil.org/iso639-3/>
-->

<!DOCTYPE iso_639_3_entries [
	<!ELEMENT iso_639_3_entries (iso_639_3_entry+)>
	<!ELEMENT iso_639_3_entry EMPTY>
	<!ATTLIST iso_639_3_entry
		id		CDATA	#REQUIRED
		part1_code	CDATA	#IMPLIED
		part2_code	CDATA	#IMPLIED
		status		CDATA	#REQUIRED
		scope		CDATA   #REQUIRED
		type		CDATA	#REQUIRED
		inverted_name	CDATA	#IMPLIED
		reference_name	CDATA	#REQUIRED
		name		CDATA	#REQUIRED
		common_name	CDATA	#IMPLIED
	>
]>
""",
    "639-5": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all languages in the ISO 639-5
standard, and is used to provide translations via gettext

Copyright © 2014 Pander <pander@opentaal.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.loc.gov/standards/iso639-5/>
-->

<!DOCTYPE iso_639_5_entries [
	<!ELEMENT iso_639_5_entries (iso_639_5_entry+)>
	<!ELEMENT iso_639_5_entry EMPTY>
	<!ATTLIST iso_639_5_entry
		id		CDATA	#REQUIRED
		parents		CDATA	#IMPLIED
		name		CDATA	#REQUIRED
	>
]>
""",
    "3166": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all countries in the ISO 3166
standard, and is used to provide translations via gettext

Copyright (C) 2002, 2004, 2006 Alastair McKinstry <mckinstry@computer.org>
Copyright (C) 2004 Andreas Jochens <aj@andaco.de>
Copyright (C) 2004, 2007 Christian Perrier <bubulle@debian.org>
Copyright (C) 2005, 2006, 2007 Tobias Quathamer <toddy@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.iso.org/iso/country_codes>
-->

<!DOCTYPE iso_3166_entries [
	<!ELEMENT iso_3166_entries (iso_3166_entry+, iso_3166_3_entry*)>
	<!ELEMENT iso_3166_entry EMPTY>
	<!ATTLIST iso_3166_entry
		alpha_2_code		CDATA	#REQUIRED
		alpha_3_code		CDATA	#REQUIRED
		numeric_code		CDATA	#REQUIRED
		common_name		CDATA	#IMPLIED
		name			CDATA	#REQUIRED
		official_name		CDATA	#IMPLIED
	>
	<!ELEMENT iso_3166_3_entry EMPTY>
	<!ATTLIST iso_3166_3_entry
		alpha_4_code		CDATA	#REQUIRED
		alpha_3_code		CDATA	#REQUIRED
		numeric_code		CDATA	#IMPLIED
		date_withdrawn		CDATA	#IMPLIED
		names			CDATA	#REQUIRED
		comment			CDATA	#IMPLIED
	>
]>
""",
    "3166-2": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all country subdivisions in the ISO 3166-2
standard, and is used to provide translations via gettext

The following conventions are used in this file:
If the standard lists a subdivision name in more than one language
and/or romanization system, only the first listed name is shown.

For some countries the standard also lists a second level of
regional divisions (e.g. for BE, FR, GB, IT, etc.). The codes
for these regional divisions are shown as 'XX YYYY', i.e. with a
space character instead of the '-'.

Copyright (C) 2004-2006 Alastair McKinstry <mckinstry@computer.org>
Copyright (C) 2004, 2007 Christian Perrier <bubulle@debian.org>
Copyright (C) 2005-2007 Tobias Quathamer <toddy@debian.org>
Copyright (C) 2007, 2009 LI Daobing <lidaobing@gmail.com>
Copyright (C) 2007-2010 Alexis Darrasse <alexis@ortsa.com>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.iso.org/iso/country_codes/background_on_iso_3166/iso_3166-2.htm>
-->


<!DOCTYPE iso_3166_2_entries [
	<!ELEMENT iso_3166_2_entries (iso_3166_country+)>
  <!ELEMENT iso_3166_country (iso_3166_subset*)>
	<!ATTLIST iso_3166_country
		code			CDATA	#REQUIRED
	>
	<!ELEMENT iso_3166_subset (iso_3166_2_entry+)>
	<!ATTLIST iso_3166_subset
		type			CDATA	#REQUIRED
	>
	<!ELEMENT iso_3166_2_entry EMPTY>
	<!ATTLIST iso_3166_2_entry
		code			CDATA	#REQUIRED
		name			CDATA	#REQUIRED
		parent			CDATA	#IMPLIED
	>
]>
""",
    "15924": """<?xml version="1.0" encoding="UTF-8" ?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all script names in the ISO 15924
standard, and is used to provide translations via gettext

Copyright (C) 2007 Ivan Masar <helix84@centrum.sk>
Copyright (C) 2007-2011 Christian Perrier <bubulle@debian.org>
Copyright (C) 2007 Tobias Quathamer <toddy@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://unicode.org/iso15924/>
Source for changes: <http://unicode.org/iso15924/codechanges.html>
-->

<!DOCTYPE iso_15924_entries [
	<!ELEMENT iso_15924_entries (iso_15924_entry+)>
	<!ELEMENT iso_15924_entry EMPTY>
	<!ATTLIST iso_15924_entry
		alpha_4_code		CDATA	#REQUIRED
		numeric_code  		CDATA	#REQUIRED
		name			CDATA	#REQUIRED
	>
]>
""",
    "4217": """<?xml version="1.0" encoding="UTF-8"?>

<!--

WARNING: THIS FILE IS DEPRECATED.

PLEASE USE THE JSON DATA INSTEAD.

Usually, this data can be found in /usr/share/iso-codes/json.

This file gives a list of all currencies in the ISO 4217
standard, and is used to provide translations via gettext

Copyright (C) 2004-2006 Alastair McKinstry <mckinstry@computer.org>
Copyright (C) 2005-2009 Tobias Quathamer <toddy@debian.org>
Copyright (C) 2007 Christian Perrier <bubulle@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.bsi-global.com/en/Standards-and-Publications/Industry-Sectors/Services/BSI-Currency-Code-Service/>
-->

<!DOCTYPE iso_4217_entries [
	<!ELEMENT iso_4217_entries (iso_4217_entry+, historic_iso_4217_entry*)>
	<!ELEMENT iso_4217_entry EMPTY>
	<!ATTLIST iso_4217_entry
		letter_code		CDATA	#REQUIRED
		numeric_code		CDATA	#IMPLIED
		currency_name		CDATA	#REQUIRED
	>
	<!ELEMENT historic_iso_4217_entry EMPTY>
	<!ATTLIST historic_iso_4217_entry
		letter_code		CDATA	#REQUIRED
		numeric_code		CDATA	#IMPLIED
		currency_name		CDATA	#REQUIRED
		date_withdrawn		CDATA	#REQUIRED
	>
]>
""",
}

def get_iso_entries(standard):
    """ Return all entries from the given standard
    """
    with open(datapath + "/iso_" + standard + ".json", encoding="utf-8") as input_file:
        iso = json.load(input_file)
        return iso[standard]

# Create the output file
with open(xml_file, "w", encoding="utf-8") as outfile:
    #
    # Handle ISO 639-2
    #
    if domain == "iso_639-2":
        outfile.write(headers["639"])
        outfile.write("\n")
        outfile.write("<iso_639_entries>\n")
        for entry in get_iso_entries("639-2"):
            outfile.write("\t<iso_639_entry\n")
            if "bibliographic" in entry:
                outfile.write("\t\tiso_639_2B_code=\"" + entry["bibliographic"] + "\"\n")
            else:
                outfile.write("\t\tiso_639_2B_code=\"" + entry["alpha_3"] + "\"\n")
            outfile.write("\t\tiso_639_2T_code=\"" + entry["alpha_3"] + "\"\n")
            if "alpha_2" in entry:
                outfile.write("\t\tiso_639_1_code=\"" + entry["alpha_2"] + "\"\n")
            outfile.write("\t\tname=\"" + entry["name"] + "\"")
            if "common_name" in entry:
                outfile.write("\n\t\tcommon_name=\"" + entry["common_name"] + "\"")
            outfile.write(" />\n")
        outfile.write("</iso_639_entries>\n")
    #
    # Handle ISO 639-3
    #
    elif domain == "iso_639-3":
        outfile.write(headers["639-3"])
        outfile.write("\n")
        outfile.write("<iso_639_3_entries>\n")
        for entry in get_iso_entries("639-3"):
            outfile.write("\t<iso_639_3_entry\n")
            outfile.write("\t\tid=\"" + entry["alpha_3"] + "\"\n")
            if "alpha_2" in entry:
                outfile.write("\t\tpart1_code=\"" + entry["alpha_2"] + "\"\n")
            if "bibliographic" in entry:
                outfile.write("\t\tpart2_code=\"" + entry["bibliographic"] + "\"\n")
            # Special case for lcq, which is the only entry with status "Retired"
            if entry["alpha_3"] == "lcq":
                outfile.write("\t\tstatus=\"Retired\"\n")
            else:
                outfile.write("\t\tstatus=\"Active\"\n")
            outfile.write("\t\tscope=\"" + entry["scope"] + "\"\n")
            outfile.write("\t\ttype=\"" + entry["type"] + "\"\n")
            if "inverted_name" in entry:
                outfile.write("\t\tinverted_name=\"" + entry["inverted_name"] + "\"\n")
            outfile.write("\t\treference_name=\"" + entry["name"] + "\"\n")
            if "common_name" in entry:
                outfile.write("\t\tcommon_name=\"" + entry["common_name"] + "\"\n")
            if "inverted_name" in entry:
                outfile.write("\t\tname=\"" + entry["inverted_name"] + "\"")
            else:
                outfile.write("\t\tname=\"" + entry["name"] + "\"")
            outfile.write(" />\n")
        outfile.write("</iso_639_3_entries>\n")
    #
    # Handle ISO 639-5
    #
    elif domain == "iso_639-5":
        outfile.write(headers["639-5"])
        outfile.write("\n")
        outfile.write("<iso_639_5_entries>\n")
        for entry in get_iso_entries("639-5"):
            outfile.write("\t<iso_639_5_entry\n")
            outfile.write("\t\tid=\"" + entry["alpha_3"] + "\"\n")
            outfile.write("\t\tname=\"" + entry["name"] + "\"")
            outfile.write(" />\n")
        outfile.write("</iso_639_5_entries>\n")
    #
    # Handle ISO 3166
    #
    elif domain == "iso_3166-1":
        outfile.write(headers["3166"])
        outfile.write("\n")
        outfile.write("<iso_3166_entries>\n")
        for entry in get_iso_entries("3166-1"):
            outfile.write("\t<iso_3166_entry\n")
            outfile.write("\t\talpha_2_code=\"" + entry["alpha_2"] + "\"\n")
            outfile.write("\t\talpha_3_code=\"" + entry["alpha_3"] + "\"\n")
            outfile.write("\t\tnumeric_code=\"" + entry["numeric"] + "\"\n")
            if "common_name" in entry:
                outfile.write("\t\tcommon_name=\"" + entry["common_name"] + "\"\n")
            outfile.write("\t\tname=\"" + entry["name"] + "\"")
            if "official_name" in entry:
                outfile.write("\n\t\tofficial_name=\"" + entry["official_name"] + "\"")
            outfile.write(" />\n")
        for entry in get_iso_entries("3166-3"):
            outfile.write("\t<iso_3166_3_entry\n")
            outfile.write("\t\talpha_4_code=\"" + entry["alpha_4"] + "\"\n")
            outfile.write("\t\talpha_3_code=\"" + entry["alpha_3"] + "\"\n")
            if "numeric" in entry:
                outfile.write("\t\tnumeric_code=\"" + entry["numeric"] + "\"\n")
            if "withdrawal_date" in entry:
                outfile.write("\t\tdate_withdrawn=\"" + entry["withdrawal_date"] + "\"\n")
            outfile.write("\t\tnames=\"" + entry["name"] + "\"")
            if "comment" in entry:
                outfile.write("\n\t\tcomment=\"" + entry["comment"] + "\"")
            outfile.write(" />\n")
        outfile.write("</iso_3166_entries>\n")
    #
    # Handle ISO 3166-2
    #
    elif domain == "iso_3166-2":
        outfile.write(headers["3166-2"])
        outfile.write("\n")
        outfile.write("<iso_3166_2_entries>\n")
        last_country_code = ""
        subsets = {}
        for entry in get_iso_entries("3166-2"):
            country_code = entry["code"].split("-")[0]
            # Initialize for every new country
            if last_country_code != country_code:
                # Write out if subsets are filled
                if len(subsets) > 0:
                    outfile.write("<iso_3166_country code=\"" + last_country_code + "\">\n")
                    for subset in sorted(subsets):
                        outfile.write("<iso_3166_subset type=\"" + subset + "\">\n")
                        for item in subsets[subset]:
                            outfile.write("\t<iso_3166_2_entry\n")
                            outfile.write("\t\tcode=\"" + item["code"] + "\"\tname=\"" + item["name"] + "\"")
                            if "parent" in item:
                                outfile.write("\tparent=\"" + item["parent"] + "\"")
                            outfile.write(" />\n")
                        outfile.write("</iso_3166_subset>\n")
                    outfile.write("</iso_3166_country>\n")
                last_country_code = country_code
                subsets = {}
            # Group by subset types
            if entry["type"] not in subsets:
                subsets[entry["type"]] = [entry]
            else:
                subsets[entry["type"]].append(entry)
        outfile.write("</iso_3166_2_entries>\n")
    #
    # Handle ISO 15924
    #
    elif domain == "iso_15924":
        outfile.write(headers["15924"])
        outfile.write("\n")
        outfile.write("<iso_15924_entries>\n")
        for entry in get_iso_entries("15924"):
            outfile.write("\t<iso_15924_entry\n")
            outfile.write("\t\talpha_4_code=\"" + entry["alpha_4"] + "\"\n")
            outfile.write("\t\tnumeric_code=\"" + entry["numeric"] + "\"\n")
            outfile.write("\t\tname=\"" + entry["name"] + "\"")
            outfile.write(" />\n")
        outfile.write("</iso_15924_entries>\n")
    #
    # Handle ISO 4217
    #
    elif domain == "iso_4217":
        outfile.write(headers["4217"])
        outfile.write("\n")
        outfile.write("<iso_4217_entries>\n")
        for entry in get_iso_entries("4217"):
            outfile.write("\t<iso_4217_entry\n")
            outfile.write("\t\tletter_code=\"" + entry["alpha_3"] + "\"\n")
            if "numeric" in entry:
                outfile.write("\t\tnumeric_code=\"" + entry["numeric"] + "\"\n")
            outfile.write("\t\tcurrency_name=\"" + entry["name"] + "\"")
            outfile.write(" />\n")
        # Insert the obsolete historic entries, which are no
        # longer included in the JSON data files.
        outfile.write("""	<historic_iso_4217_entry
		letter_code="ADP"
		numeric_code="020"
		currency_name="Andorran Peseta"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="ADF"
		currency_name="Andorran Franc"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="AFA"
		numeric_code="004"
		currency_name="Afghani"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="ALK"
		currency_name="Albanian Old Lek"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="AOK"
		currency_name="Angolan Kwanza"
		date_withdrawn="1991-03" />
	<historic_iso_4217_entry
		letter_code="AON"
		numeric_code="024"
		currency_name="Angolan New Kwanza"
		date_withdrawn="2000-02" />
	<historic_iso_4217_entry
		letter_code="AOR"
		numeric_code="982"
		currency_name="Angola Kwanza Reajustado"
		date_withdrawn="2000-02" />
	<historic_iso_4217_entry
		letter_code="ARA"
		currency_name="Argentine Austral"
		date_withdrawn="1992-01" />
	<historic_iso_4217_entry
		letter_code="ARM"
		currency_name="Argentine peso moneda nacional"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="ARL"
		currency_name="Argentine peso ley"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="ARP"
		currency_name="Peso Argentino"
		date_withdrawn="1985-07" />
	<historic_iso_4217_entry
		letter_code="ATS"
		numeric_code="040"
		currency_name="Austrian Schilling"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="AZM"
		numeric_code="031"
		currency_name="Azerbaijanian Manat"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="BAD"
		numeric_code="070"
		currency_name="Bosnia and Herzegovina Dinar"
		date_withdrawn="1997-07" />
	<historic_iso_4217_entry
		letter_code="BEC"
		numeric_code="993"
		currency_name="Belgian Franc Convertible"
		date_withdrawn="1990-03" />
	<historic_iso_4217_entry
		letter_code="BEF"
		numeric_code="056"
		currency_name="Belgian Franc"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="BEL"
		numeric_code="992"
		currency_name="Belgian Franc Financial"
		date_withdrawn="1990-03" />
	<historic_iso_4217_entry
		letter_code="BGJ"
		currency_name="Bulgarian Lev A/52"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="BGK"
		currency_name="Bulgarian Lev A/62"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="BGL"
		numeric_code="100"
		currency_name="Bulgarian Lev A/99"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="BOP"
		currency_name="Bolivian Peso"
		date_withdrawn="1987-02" />
	<historic_iso_4217_entry
		letter_code="BRB"
		currency_name="Brazilian Cruzeiro"
		date_withdrawn="1986-03" />
	<historic_iso_4217_entry
		letter_code="BRC"
		currency_name="Brazilian Cruzado"
		date_withdrawn="1989-02" />
	<historic_iso_4217_entry
		letter_code="BRE"
		numeric_code="076"
		currency_name="Brazilian Cruzeiro"
		date_withdrawn="1993-03" />
	<historic_iso_4217_entry
		letter_code="BRN"
		currency_name="Brazilian New Cruzado"
		date_withdrawn="1990-03" />
	<historic_iso_4217_entry
		letter_code="BRR"
		numeric_code="987"
		currency_name="Brazilian Cruzeiro Real"
		date_withdrawn="1994-07" />
	<historic_iso_4217_entry
		letter_code="BUK"
		currency_name="Kyat"
		date_withdrawn="1990-02" />
	<historic_iso_4217_entry
		letter_code="BYB"
		currency_name="Belarussian Rouble"
		date_withdrawn="1999" />
	<historic_iso_4217_entry
		letter_code="CNX"
		currency_name="Chinese Peoples Bank Dollar"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="CSD"
		numeric_code="891"
		currency_name="Serbian Dinar"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="CSJ"
		currency_name="Czechoslovak Krona A/53"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="CSK"
		numeric_code="200"
		currency_name="Czechoslovak Koruna"
		date_withdrawn="1993-03" />
	<historic_iso_4217_entry
		letter_code="DDM"
		numeric_code="278"
		currency_name="East German Mark of the GDR"
		date_withdrawn="1990-09" />
	<historic_iso_4217_entry
		letter_code="DEM"
		numeric_code="276"
		currency_name="Deutsche Mark"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="ECS"
		numeric_code="218"
		currency_name="Ecuador Sucre"
		date_withdrawn="2000-09-15" />
	<historic_iso_4217_entry
		letter_code="ECV"
		numeric_code="983"
		currency_name="Ecuador Unidad de Valor Constante UVC"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="ESA"
		numeric_code="996"
		currency_name="Spanish Peseta ('A' Account)"
		date_withdrawn="1981" />
	<historic_iso_4217_entry
		letter_code="ESB"
		numeric_code="995"
		currency_name="Spanish Peseta (convertible)"
		date_withdrawn="1994-12" />
	<historic_iso_4217_entry
		letter_code="ESP"
		numeric_code="724"
		currency_name="Spanish Peseta"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="FIM"
		numeric_code="246"
		currency_name="Finnish Markka"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="FRF"
		numeric_code="250"
		currency_name="French Franc"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="GEK"
		numeric_code="268"
		currency_name="Georgian Coupon"
		date_withdrawn="1995-10" />
	<historic_iso_4217_entry
		letter_code="GNE"
		currency_name="Guinea Syli"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="GNS"
		currency_name="Guinea Syli"
		date_withdrawn="1986-02" />
	<historic_iso_4217_entry
		letter_code="GQE"
		numeric_code="226"
		currency_name="Equatorial Guinea Ekwele"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="GHC"
		numeric_code="288"
		currency_name="Cedi"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="GRD"
		numeric_code="300"
		currency_name="Greek Drachma"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="GWE"
		currency_name="Guinea Escudo"
		date_withdrawn="1981" />
	<historic_iso_4217_entry
		letter_code="GWP"
		numeric_code="624"
		currency_name="Guinea-Bissau Peso"
		date_withdrawn="1997-04" />
	<historic_iso_4217_entry
		letter_code="HRD"
		currency_name="Croatian Dinar"
		date_withdrawn="1995-01" />
	<historic_iso_4217_entry
		letter_code="IEP"
		numeric_code="372"
		currency_name="Irish Pound"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="ILP"
		currency_name="Israeli Pound"
		date_withdrawn="1981" />
	<historic_iso_4217_entry
		letter_code="ILR"
		currency_name="Israeli Old Shekel"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="ISJ"
		currency_name="Iceland Old Krona"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="ITL"
		numeric_code="380"
		currency_name="Italian Lira"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="LAJ"
		currency_name="Lao kip"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="LSM"
		currency_name="Lesotho Maloti"
		date_withdrawn="1985-05" />
	<historic_iso_4217_entry
		letter_code="LTT"
		currency_name="Lithuanian Talonas"
		date_withdrawn="1993-07" />
	<historic_iso_4217_entry
		letter_code="LUC"
		numeric_code="989"
		currency_name="Luxembourg Convertible Franc"
		date_withdrawn="1990-03" />
	<historic_iso_4217_entry
		letter_code="LUF"
		numeric_code="442"
		currency_name="Luxembourg Franc"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="LUL"
		numeric_code="988"
		currency_name="Luxembourg Financial Franc"
		date_withdrawn="1990-03" />
	<historic_iso_4217_entry
		letter_code="LVR"
		currency_name="Latvian Ruble"
		date_withdrawn="1994-12" />
	<historic_iso_4217_entry
		letter_code="MAF"
		currency_name="Mali Franc"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="MGF"
		numeric_code="450"
		currency_name="Malagasy Franc"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="MLF"
		numeric_code="446"
		currency_name="Mali Franc"
		date_withdrawn="1984-11" />
	<historic_iso_4217_entry
		letter_code="MTP"
		currency_name="Maltese Pound"
		date_withdrawn="1983-06" />
	<historic_iso_4217_entry
		letter_code="MVQ"
		currency_name="Maldive Rupee"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="MXP"
		currency_name="Mexican Peso"
		date_withdrawn="1993-01" />
	<historic_iso_4217_entry
		letter_code="MZE"
		currency_name="Mozambique Escudo"
		date_withdrawn="1981" />
	<historic_iso_4217_entry
		letter_code="MZM"
		numeric_code="508"
		currency_name="Mozambique Metical"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="NIC"
		currency_name="Nicaraguan Cordoba"
		date_withdrawn="1990-10" />
	<historic_iso_4217_entry
		letter_code="NLG"
		numeric_code="528"
		currency_name="Netherlands Guilder"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="PEH"
		currency_name="Peruvian Sol"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="PEI"
		currency_name="Peruvian Inti"
		date_withdrawn="1991-07" />
	<historic_iso_4217_entry
		letter_code="PES"
		currency_name="Peruvian Sol"
		date_withdrawn="1986-02" />
	<historic_iso_4217_entry
		letter_code="PLZ"
		numeric_code="616"
		currency_name="Polish Złoty"
		date_withdrawn="1997-01" />
	<historic_iso_4217_entry
		letter_code="PTE"
		numeric_code="620"
		currency_name="Portuguese Escudo"
		date_withdrawn="2002-03" />
	<historic_iso_4217_entry
		letter_code="RHD"
		currency_name="Rhodesian Dollar"
		date_withdrawn="1981" />
	<historic_iso_4217_entry
		letter_code="ROK"
		currency_name="Romanian Leu A/52"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="ROL"
		numeric_code="642"
		currency_name="Romanian Old Leu"
		date_withdrawn="2005-06" />
	<historic_iso_4217_entry
		letter_code="RUR"
		numeric_code="810"
		currency_name="Russian Rouble"
		date_withdrawn="1997" />
	<historic_iso_4217_entry
		letter_code="SDD"
		numeric_code="736"
		currency_name="Sudanese Pound"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="SDP"
		currency_name="Sudanese Pound"
		date_withdrawn="1998-06" />
	<historic_iso_4217_entry
		letter_code="SIT"
		numeric_code="705"
		currency_name="Slovenian Tolar"
		date_withdrawn="2006-12-31" />
	<historic_iso_4217_entry
		letter_code="SKK"
		numeric_code="703"
		currency_name="Slovak Koruna"
		date_withdrawn="2009-01-01" />
	<historic_iso_4217_entry
		letter_code="SRG"
		numeric_code="740"
		currency_name="Suriname Guilder"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="SUR"
		currency_name="USSR Rouble"
		date_withdrawn="1990-12" />
	<historic_iso_4217_entry
		letter_code="TJR"
		numeric_code="762"
		currency_name="Tajik Rouble"
		date_withdrawn="2000" />
	<historic_iso_4217_entry
		letter_code="TLE"
		numeric_code="626"
		currency_name="Timor Escudo"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="TRL"
		numeric_code="792"
		currency_name="Turkish Lira"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="UAK"
		numeric_code="804"
		currency_name="Ukrainian Karbovanet"
		date_withdrawn="1996-09" />
	<historic_iso_4217_entry
		letter_code="UGS"
		currency_name="Uganda Schilling"
		date_withdrawn="1987-05" />
	<historic_iso_4217_entry
		letter_code="UGW"
		currency_name="Uganda Old Schilling"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="UYN"
		currency_name="Old Uruguayan Peso"
		date_withdrawn="1989-12" />
	<historic_iso_4217_entry
		letter_code="UYP"
		currency_name="Uruguayan Peso"
		date_withdrawn="1993-03" />
	<historic_iso_4217_entry
		letter_code="VEB"
		numeric_code="862"
		currency_name="Venezuela Bolívar"
		date_withdrawn="2008-01-01" />
	<historic_iso_4217_entry
		letter_code="VNC"
		currency_name="Viet Nam Old Dong"
		date_withdrawn="1990" />
	<historic_iso_4217_entry
		letter_code="XEU"
		numeric_code="954"
		currency_name="European Currency Unit ECU"
		date_withdrawn="1999-01" />
	<historic_iso_4217_entry
		letter_code="XRE"
		currency_name="RINET Funds Code"
		date_withdrawn="1999-11" />
	<historic_iso_4217_entry
		letter_code="YDD"
		numeric_code="720"
		currency_name="Yemeni Dinar"
		date_withdrawn="1991-09" />
    <historic_iso_4217_entry
		letter_code="YUD"
		numeric_code="891"
		currency_name="Yugoslavian Dinar"
		date_withdrawn="unknown" />
	<historic_iso_4217_entry
		letter_code="YUN"
		numeric_code="890"
		currency_name="Yugoslavian Dinar"
		date_withdrawn="1995-11" />
	<historic_iso_4217_entry
		letter_code="ZAL"
		numeric_code="991"
		currency_name="South African Financial Rand"
		date_withdrawn="1995-03" />
	<historic_iso_4217_entry
		letter_code="ZRN"
		currency_name="New Zaire"
		date_withdrawn="1999-06" />
	<historic_iso_4217_entry
		letter_code="ZRZ"
		numeric_code="180"
		currency_name="Zaire"
		date_withdrawn="1994-02" />
""")
        outfile.write("</iso_4217_entries>\n")
