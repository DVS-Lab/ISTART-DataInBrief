# ISTART Data
This repository contains the final code for managing and processing all of the data in our ISTART project. The data live on OpenNeuro (https://openneuro.org/datasets/ds004920), and a preprint of a data paper has been posted to PsyArxiv (https://osf.io/preprints/psyarxiv/vqpnx) and is under consideration at Data in Brief.

## A few prerequisites and recommendations
- Understand BIDS and be comfortable navigating Linux
- Install [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation)
- Install [miniconda or anaconda](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda)
- Install PyDeface: `pip install pydeface`
- Make singularity containers for heudiconv (version: 0.9.0), mriqc (version: 0.16.1), and fmriprep (version: 20.2.3).


## Notes on repository organization and files
- Raw DICOMS (an input to heudiconv) are only accessible locally
- Some of the contents of this repository are not tracked (.gitignore) because the files are large and we do not yet have a nice workflow for datalad. Note that we only track key text files in `bids`.
- Tracked folders and their contents:
  - `code`: analysis code
  - `bids`: contains the standardized "raw" in BIDS format (output of heudiconv)
  - `stimuli`: psychopy scripts and matlab scripts for delivering stimuli and organizing output. This directory also contains the sourcedata for the raw behavioral data.


## Downloading Data
```
# get data via datalad
git clone https://github.com/DVS-Lab/ISTART-DataInBrief
cd ISTART-DataInBrief
datalad clone https://github.com/OpenNeuroDatasets/ds004920.git bids
# you can get all of the data with the commands below:
cd bids
datalad get sub-*

```


## Acknowledgments
This work was supported in part by grants from the National Institute of Mental Health (R15-MH122927 to DSF), the Eunice Kennedy Shriver National Institute of Child Health and Human Development (R21-HD093912 to JMJ), the National Institute on Aging (RF1-AG067011 to DVS), and the National Institute on Drug Abuse (R03-DA046733 to DVS), and a fellowship from the Temple Public Policy Lab (to JMJ). We thank Caleb Haynes, Jeffrey Dennison, Athena Vafiadis, and Makayla Collins for assistance with data collection.

[openneuro]: https://openneuro.org/
