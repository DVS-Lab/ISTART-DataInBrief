# Task scan and event availability for ds004920

The historical counts below describe the public files in [OpenNeuro 1.1.0](https://openneuro.org/datasets/ds004920/versions/1.1.0) and [1.1.1](https://openneuro.org/datasets/ds004920/versions/1.1.1), which accompany the [Data in Brief paper](https://doi.org/10.1016/j.dib.2024.110197).

## Changes in OpenNeuro 1.1.2

[Version 1.1.2](https://doi.org/10.18112/openneuro.ds004920.v1.1.2) restores ten run 1 event tables from the original scanner-task logs and replaces the mixed Social Doors record for `sub-1282` with its scan-day file. Fourteen of 415 BOLD runs still have zero event rows (Doors 1, Social Doors 1, MID 5, Shared Reward 3, UGDG 4). The short Social Doors recordings for `sub-3152` and `sub-3199` contain 6 and 34 outcomes, respectively.

The release also aligns questionnaire and participant codes with their existing dictionaries, corrects the Buss–Perry sidecar filename, and updates citation guidance for the data paper and task-specific publications.

## Coverage in snapshots 1.1.0 and 1.1.1

The paper describes the 59-participant cohort and the four experimental paradigms. The two conditions of the Social Doors paradigm are released under separate task labels, `doors` and `socialdoors`. In snapshots 1.1.0 (cited in the paper) and 1.1.1, 50 participants have at least one BOLD run under all five task labels. The task BOLD and event files are identical in those two snapshots.

| Task label | Participants with BOLD | BOLD runs | BOLD runs with zero event rows |
| --- | ---: | ---: | ---: |
| `doors` | 59 | 59 | 6 |
| `socialdoors` | 58 | 58 | 6 |
| `mid` | 56 | 80 | 5 |
| `sharedreward` | 52 | 102 | 3 |
| `ugdg` | 58 | 116 | 4 |
| Total | 59 unique | 415 | 24 |

Every released BOLD run has a corresponding event TSV by filename. A table with zero event rows cannot supply task timing. Event columns differ by task. For example, the populated Doors tables use `onset`, `duration`, `trial_type`, `rt`, `resp`, and `gender`, while MID uses `onset`, `duration`, and `trial_type`. A trial can produce more than one event row.

Three additional TSVs have event rows without a corresponding BOLD file in these snapshots. They are `1240` Social Doors run 1 (24 recorded outcomes), `1253` Shared Reward run 2, and `3186` MID run 1. These are outside the 415-run denominator.

## Known event file exceptions

| Task and run | Participants | Source status |
| --- | --- | --- |
| `doors` and `socialdoors`, run 1 | `1011`, `1012`, `1013`, `1015`, `1016` | These ten placeholders have original scan-session TSVs. Each archived file is byte-identical to the version committed with that participant’s scan data and contains 60 decision periods and 60 outcomes (30 wins and 30 losses). Trial labels, onsets, and durations agree with the older lab BIDS tables. The older and released scan sidecars match on acquisition time, series number, task description, and repetition time. The [collection script](https://github.com/DVS-Lab/istart/blob/065f86c020a98d2d7386a008f393cca69eb8f0b6/social_reward_c/social_reward_c.py#L120-L134) starts the event clock after the scanner trigger. The [recovery manifest](https://github.com/DVS-Lab/istart-ds004920/blob/11220dd3519ce6d22bfc0102be65134a3ccc5e93/config/istart_event_sources.json) links the original `imageA` (monetary Doors) and `faceA` (Social Doors) logs by exact revision and records their Git blob hashes. |
| `doors`, run 1 | `1282` | Zero event rows. The [archived Doors files](https://github.com/DVS-Lab/istart/tree/7a6cffe9f03e36ef91699f7d2a355ea155b6527c/social_reward_c/data/1282) contain practice timing only. No usable in-scanner Doors timing was located. |
| `socialdoors`, run 1 | `1253` | Zero event rows. No usable Social Doors encoding log was located in the [task archive](https://github.com/DVS-Lab/istart/tree/7a6cffe9f03e36ef91699f7d2a355ea155b6527c/social_reward_c/data/1253). |
| `socialdoors`, run 1 | `1282` | The released table combines a 60-outcome run with a three-outcome attempt and invalid timing rows. The [scan-day encoding file](https://github.com/DVS-Lab/istart/blob/e798552ad8143cc10024b3076e1385d391deedf8/social_reward_c/data/1282/sub-1282_ses-1_task-socialReward_facesB_events.tsv) contains 120 rows ending at 506.51 s within the 512.75 s scan. The 60 decisions and 60 outcomes match the first complete sequence in the release. The [later archive revision](https://github.com/DVS-Lab/istart/blob/d9ed388cb8c9ac06131ca35d80b66a1a9277a259/social_reward_c/data/1282/sub-1282_ses-1_task-socialReward_facesB_events.tsv) shows where a merge conflict appended the short attempt. |
| `socialdoors`, run 1 | `3152`, `3199` | The original logs and the release agree on 6 and 34 outcomes, respectively. These are partial records relative to the 60 outcomes in the planned run. [3152 source](https://github.com/OpenNeuroDatasets/ds004920/tree/1.1.1/sourcedata/sub-3152) · [3199 source](https://github.com/OpenNeuroDatasets/ds004920/tree/1.1.1/sourcedata/sub-3199) |
| `mid`, run 1 | `1253`, `3101`, `3122` | Zero event rows. The original MATLAB logs have 50, 75, and 75 trial onsets, with 49, 74, and 74 outcomes, respectively. The [converter](https://github.com/DVS-Lab/ISTART-DataInBrief/blob/0cf05a6bd68c88d81fae475b1f8db649f395aa78/code/convert2bids_mid.py#L54-L87) skips logs with unequal field lengths. The missing outcome cannot be assigned to a trial from the array lengths alone. |
| `mid`, run 1 | `1282` | Zero event rows. The older timing matches 75 trials and outcomes in the original log. Verify synchronization to the released scan before substituting it. [Older timing and raw log](https://github.com/DVS-Lab/istart-data/tree/3d08efcbe12a7328969ffdce3ec010c9f0c0d97a/bids/sub-1282/func) · [Original MATLAB log](https://github.com/DVS-Lab/istart/tree/7a6cffe9f03e36ef91699f7d2a355ea155b6527c/Monetary_Incentive/data/sub-1282) |
| `mid`, run 2 | `1286` | Zero event rows. The [archived MID source](https://github.com/DVS-Lab/istart/tree/7a6cffe9f03e36ef91699f7d2a355ea155b6527c/Monetary_Incentive/data/sub-1286) contains a run 1 log. A run 2 log was not located. |
| `sharedreward`, run 2 | `1002` | Zero event rows. The source CSV labeled run 1 uses zero-based numbering and has seven recorded outcomes. The [converter](https://github.com/DVS-Lab/ISTART-DataInBrief/blob/0cf05a6bd68c88d81fae475b1f8db649f395aa78/code/convertSharedReward2BIDSevents.m#L27-L57) requires at least 72 trial records after its response-field check. [Source log directory](https://github.com/OpenNeuroDatasets/ds004920/tree/1.1.1/sourcedata/sub-1002) |
| `sharedreward`, runs 1 and 2 | `1282` | Zero event rows in both tables. Two 72-trial logs match the older timing tables, and a separate short attempt is also archived. Verify the mapping to the two scans before substituting the older tables. [Older timing](https://github.com/DVS-Lab/istart-data/tree/3d08efcbe12a7328969ffdce3ec010c9f0c0d97a/bids/sub-1282/func) · [Original CSVs](https://github.com/DVS-Lab/istart/tree/7a6cffe9f03e36ef91699f7d2a355ea155b6527c/Shared_Reward/logs/1282) |
| `ugdg`, runs 1 and 2 | `1240`, `1282` | Zero event rows in all four tables. The two non-practice logs per participant contain 36 trials each. The column order for 1240 differs from the fixed positions in the [converter](https://github.com/DVS-Lab/ISTART-DataInBrief/blob/0cf05a6bd68c88d81fae475b1f8db649f395aa78/code/convert2bids_ugdg.m#L98-L139), which also notes an imaging issue for 1240. The cause of the empty tables for 1282 is undetermined. Verify timing and scan suitability before reuse. [Original CSVs](https://github.com/OpenNeuroDatasets/ds004920/tree/1.1.1/sourcedata/UGDG/logs) |

## Counting runs for analysis

Use the participant, task, and run together to match BOLD and event files. Check the recorded trial counts by condition and whether the event timing matches the scan. The counts above describe file availability. Imaging quality and the inclusion criteria for a particular analysis require their own assessment.

The coverage counts come from the released BOLD and event file trees for [1.1.0](https://github.com/OpenNeuroDatasets/ds004920/tree/1.1.0) and [1.1.1](https://github.com/OpenNeuroDatasets/ds004920/tree/2913a29de224f5364629cc39ac26045c06817b4f). For the affected runs, the notes distinguish what can be recovered from the reviewed logs from timing that still needs to be matched to the scans.
