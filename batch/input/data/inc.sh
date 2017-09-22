#!/bin/sh
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Bac/index.html > urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Tyb/index.html >>  urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Ksa/index.html >>  urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Kka/index.html >>  urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Kyg/index.html >>  urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Ukc/index.html >>  urls.txt
./extract-html-alink.pl a http://www2.jrdb.com/member/data/Zec/index.html >>  urls.txt

cat urls.txt | xargs wget 
for file in *.lzh; do
    lha xq "${file}"
    rm "${file}"
done

