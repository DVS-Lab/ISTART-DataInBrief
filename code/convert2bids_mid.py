#Import the Libraries
import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd
import os
from natsort import natsorted
import re

#Make a list of the files
#Mat_Beh_dir='/ZPOOL/data/projects/istart-datapaper-test05/bids/sourcedata'
Mat_Beh_dir='/Users/jameswyngaarden/Documents/Github/istart-datapaper-test05/bids/sourcedata'
ML_EvFiles_list=natsorted([os.path.join(root,f) for root,dirs,files in os.walk(
    Mat_Beh_dir) for f in files if 'output.mat' in f])

print("The number of Subjects are: %s"%(len([x for x in os.listdir(Mat_Beh_dir) if x.startswith('sub')])))
print("The number of files are: %s"%(len(ML_EvFiles_list)))
print("----------------------------------------")

#Load the .mat convert to dataframe add trial_type and detect bad data
for ML_EvFile in ML_EvFiles_list:
    print(ML_EvFile)
    sub='sub-'+re.search('sub-(.*)/',ML_EvFile).group(1)
    # Make conditions for Run 1 and Run 2
    run_cond=loadmat('%s/timing/run1.mat'%(Mat_Beh_dir))
    run1=run_cond['run']['cond'][0,0]
    run1 = np.where(run1==[1], 'Large_gain', run1)
    run1 = np.where(run1==['2'], 'Large_loss', run1)
    run1 = np.where(run1==['3'], 'Small_gain', run1)
    run1 = np.where(run1==['4'], 'Small_loss', run1)
    run1 = np.where(run1==['5'], 'Neutral', run1)
    run1=np.concatenate(run1)

    run_cond=loadmat('%s/timing/run2.mat'%(Mat_Beh_dir))
    run2=run_cond['run']['cond'][0,0]
    run2 = np.where(run2==[1], 'Large_gain', run2)
    run2 = np.where(run2==['2'], 'Large_loss', run2)
    run2 = np.where(run2==['3'], 'Small_gain', run2)
    run2 = np.where(run2==['4'], 'Small_loss', run2)
    run2 = np.where(run2==['5'], 'Neutral', run2)
    run2=np.concatenate(run2)

    run=re.search('run-(.*)_out',ML_EvFile).group(1)
    print(sub,run)
    mat = loadmat(ML_EvFile)  # load mat-file
    mdata = mat['output']  # variable in mat file
    mdtype = mdata.dtype  # dtypes of structures are "unsized objects"
    # * SciiencPy reads in structures as structured NumPy arrays of dtype object
    # * The size of the array is the size of the structure array, not the number
    #   elements in any particular field. The shape defaults to 2-dimensional.
    # * For convene make a dictionary of the data using the names from dtypes
    # * Since the structure has only one element, but is 2-D, index it at [0, 0]
    ndata = {n: mdata[n][0, 0] for n in mdtype.names}
    # Reconstruct the columns of the data table from just the time series
    # Use the number of intervals to test if a field is a column or metadata
    columns = [n for n in ndata]
    #Check fo frame
    # now make a data frame, setting the time stamps as the index
    lens=[len(x[0]) for x in ndata.values()]
    if lens.count(lens[0]) == len(lens):
        df = pd.DataFrame(np.transpose(np.concatenate([ndata[c] for c in columns])),
                  columns=columns)
        if run=='1':
            if len(df)==50:
                df['trial_type']=run1[0:50]
            elif len(df)==75:
                df['trial_type']=run1
        if run=='2':
            df['trial_type']=run2
        #print(df)
        tmp1=df[['target_starts','trial_starts','trial_type']]
        tmp1['duration']=tmp1['target_starts']-tmp1['trial_starts']
        tmp1['onset']=tmp1['trial_starts']
        tmp1=tmp1[['onset','duration','trial_type']]
        tmp2=df[['target_starts','outcome']]
        tmp2['onset']=tmp2['target_starts']+1.0
        tmp2['duration']=1.0
        map_dict = {1: "ConHit", 0 : "ConMiss"}
        tmp2["trial_type"] = tmp2["outcome"].map(map_dict)
        tmp2=tmp2[['onset','duration','trial_type']]
        df=pd.concat([tmp1,tmp2])
        if not os.path.isdir('../../istart-datapaper-test05/bids/%s/func'%(sub)):
            os.makedirs('../../istart-datapaper-test05/bids/%s/func'%(sub)) 
        df.to_csv('../../istart-datapaper-test05/bids/%s/func/%s_task-mid_run-%s_events.tsv'%(sub,sub,run),sep = '\t', index=False)
    else:
        print("Problem with %s run-%s"%(sub,run))
