# Name: iso-dis-639_5-download.sh
# Date: 2014-03-22
# Version: 0.3
# Author: Pander <pander@opentaal.org>
#
# Main website for ISO 639-5:
# http://www.loc.gov/standards/iso639-5/
#
# Wikipedia entry for ISO 639-5:
# https://en.wikipedia.org/wiki/ISO_639-5

# This script will download almost 2000 files using almost 40 MB.
# For a clean download remove all .rdf files manually and rerun this script.

if [ ! -e rdf ]
then
    mkdir rdf
fi
cd rdf

if [ ! -e iso639-5.rdf ]
then
    wget http://id.loc.gov/vocabulary/iso639-5.rdf
fi
for i in `grep '<rdf:Description rdf:about' iso639-5.rdf|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
do
    I=`basename $i`
    if [ ! -e $I.rdf ]
    then
        wget $i.rdf
    fi
    for j in `grep -A1 '<skos:narrower ' $I.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
    do
        J=`basename $j`
        if [ ! -e $J.rdf ]
        then
            wget $j.rdf
        fi
        for k in `grep -A1 '<skos:narrower ' $J.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
        do
            K=`basename $k`
            if [ ! -e $K.rdf ]
            then
                wget $k.rdf
            fi
            for l in `grep -A1 '<skos:narrower ' $K.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
            do
                L=`basename $l`
                if [ ! -e $L.rdf ]
                then
                    wget $l.rdf
                fi
                for m in `grep -A1 '<skos:narrower ' $L.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
                do
                    M=`basename $m`
                    if [ ! -e $M.rdf ]
                    then
                        wget $m.rdf
                    fi
                    for n in `grep -A1 '<skos:narrower ' $M.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
                    do
                        N=`basename $n`
                        if [ ! -e $N.rdf ]
                        then
                            wget $n.rdf
                        fi
                        for o in `grep -A1 '<skos:narrower ' $N.rdf|grep '<rdf:Description rdf:about'|awk -F 'about="' '{print $2}'|awk -F '">' '{print $1}'`
                        do
                            O=`basename $o`
                            if [ ! -e $O.rdf ]
                            then
                                wget $o.rdf
                            fi
                        done
                    done
                done
            done
        done
    done
done

cd ..
