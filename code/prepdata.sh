#/usr/bin/env bash

# Example code for heudiconv and pydeface. This will get your data ready for analyses.
# This code will convert DICOMS to BIDS (PART 1). Will also deface (PART 2) and run MRIQC (PART 3).

# usage: bash prepdata.sh sub nruns
# example: bash prepdata.sh 104 3

# Notes:
# 1) containers live under /data/tools on local computer. should these relative paths and shared? YODA principles would suggest so.
# 2) other projects should use Jeff's python script for fixing the IntendedFor
# 3) aside from containers, only absolute path in whole workflow (transparent to folks who aren't allowed to access to raw data)
sourcedata=/ZPOOL/data/sourcedata/sourcedata/istart


sub=$1


# ensure paths are correct irrespective from where user runs the script
codedir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dsroot="$(dirname "$codedir")"



# make bids folder if it doesn't exist
if [ ! -d $dsroot/bids ]; then
	mkdir -p $dsroot/bids
fi

# overwrite existing
rm -rf $dsroot/bids/sub-${sub}


# PART 1: running heudiconv and fixing fieldmaps
singularity run --cleanenv \
-B $dsroot:/out \
-B $sourcedata:/sourcedata \
/ZPOOL/data/tools/heudiconv_1.0.0.sif \
-d /sourcedata/dicoms/Smith-ISTART-{subject}/scans/*/resources/DICOM/files/*.dcm \
-s $sub \
-f /out/code/heuristics.py \
-c dcm2niix -b --minmeta -o /out/bids --overwrite


# PART 2: Defacing anatomicals and date shifting to ensure compatibility with data sharing.

# note that you may need to install pydeface via pip or conda
bidsroot=$dsroot/bids
pydeface ${bidsroot}/sub-${sub}/anat/sub-${sub}_T1w.nii.gz
mv -f ${bidsroot}/sub-${sub}/anat/sub-${sub}_T1w_defaced.nii.gz ${bidsroot}/sub-${sub}/anat/sub-${sub}_T1w.nii.gz

