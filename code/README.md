All custom code goes into this directory. All scripts should be written such
that they can be executed from the root of the dataset, and are only using
relative paths for portability.

convert2bids_mid.py: To generate tsv files in the BIDS directory for MID, use convert2bids_mid.py
This code extracts the information needed to generate three column  files for MID. 
Use the convert2bids_mid.py command from the code directory.

convert2bids_socialdoors.m: To generate tsv files in the BIDS directory for socialdoors, use convert2bids_socialdoors.m
This code extracts the information needed to generate three column  files for socialdoors. 
Open Matlab and hit run to make the TSV files.

convert2bids_ugdg.m: To generate tsv files in the BIDS directory for UGDG, use convert2bids_ugdg.m
This code extracts the information needed to generate three column  files for UGDG. 
Open Matlab and hit run to make the TSV files.

run_convertSharedReward2BIDSevents.m: To generate tsv files in the BIDS directory for SharedReward task, open run_convertSharedReward2BIDSevents.m in MATLAB from the code directory.
Once in MATLAB, hit run to make the TSV files.
This code is a wrapper to execute the convertSharedReward2BIDSevents.m base script for all subjects with behavioral data from the 59 included in this data set.
The script extracts the information needed to generate three column  files for Shared Reward.

gen_phentoypes.py: To generate phenotype files in the BIDS directory for all measures, run gen_phenotypes.py in the code directory. 
This code converts the .txt files within sourcedata/redcap/ to BIDS compliant phenotype files. Subjects of interest can be defined withtin the usable_subs.txt file, which comes standard with the 59 subjects who have brain data. 
Command: python gen_phenotypes.py

heuristics.py: Sets the heuristics for heudiconv

run_prepdata.sh: Is a wrapper for prepdata.sh; runs heudiconv to convert to BIDS, defaces structural scans with pydeface, and runs mriqc. 

sublist-all.txt and newsubs.txt: Contains a list of all subjects with brain imaging data, used in analyses in conversion scripts. TODO: Remove newsubs.txt since it has been made redundant. May need to replace it with sublist-all.txt in some scripts. 