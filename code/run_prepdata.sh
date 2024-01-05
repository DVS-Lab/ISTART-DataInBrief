#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
maindir="$(dirname "$scriptdir")"

for sub in 1001 1002 1003 1004 3218 3220 1006 1007 1009 1010 1011 1012 1013 1015 1016 1018 1019 1021 1240 1242 1243 1244 1245 1247 1248 1249 1251 1253 1255 1276 1282 1286 1294 1300 1301 1302 1303 3101 3116 3122 3125 3140 3143 3146 3152 3164 3166 3167 3170 3173 3175 3176 3178 3186 3189 3190 3199 3200 3206 3210 3212 3223; do

	script=${scriptdir}/prepdata.sh
	NCORES=16
	while [ $(ps -ef | grep -v grep | grep $script | wc -l) -ge $NCORES ]; do
		sleep 5s
	done
   bash $script $sub &
	sleep 5s

done
