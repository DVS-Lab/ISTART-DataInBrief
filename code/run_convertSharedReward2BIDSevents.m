% script to run through all subjects
% also makes a table to summarize key information


% set up paths
scriptname = matlab.desktop.editor.getActiveFilename;
[codedir,~,~] = fileparts(scriptname);
cd(codedir);
addpath(codedir);
cd ..
dsdir = pwd;
cd ..

% this assumes you have the istart-sharedreward directory in the same
% directory as istart-data
projectdir = pwd;
sharedrewarddir = fullfile(projectdir,'istart-datapaper-test05','code');
sublist = load(fullfile(sharedrewarddir,'sublist-all.txt'));


outdata = zeros(length(sublist),5);
for s = 1:length(sublist)
    out = convertSharedReward2BIDSevents(sublist(s));
    
    outdata(s,1) = out.ntrials(1);
    outdata(s,2) = out.ntrials(2);
    outdata(s,3) = out.nmisses(1);
    outdata(s,4) = out.nmisses(2);
    outdata(s,5) = out.nfiles;
    
end
A = [sublist outdata];
T = array2table(A,'VariableNames',{'sub','run1_ntrials','run2_ntrials','run1_nmisses','run2_misses','nfiles'});
outfile = fullfile(dsdir,'derivatives',['DataSummary_' date '.csv']);
writetable(T,outfile,'Delimiter',',') 