#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
basedir="$(dirname "$scriptdir")"

task=mid

for sub in `cat ${scriptdir}/newsubs.txt`; do
	if [ "${task}" == "socialdoors" ]; then	
		cp -r /ZPOOL/data/projects/istart/social_reward_c/data/${sub}/ /ZPOOL/data/projects/istart-datapaper-test05/bids/sourcedata/sub-${sub} 
	elif [ "${task}" == "mid" ]; then	
		cp -r /ZPOOL/data/projects/istart/Monetary_Incentive/data/sub-${sub}/* /ZPOOL/data/projects/istart-datapaper-test05/bids/sourcedata/sub-${sub} 
	fi
done