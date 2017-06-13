#!/bin/bash
DATE=`date +%Y-%m-%d`
if [ "$1" == "" ]; then
    NAME="$DATE"_DevTools_80X_v1
else
    NAME="$1"
fi

SITE=T2_DE_DESY

submit_job.py crabSubmit --sampleList DevTools/Ntuplizer/data/datasetList_Data.txt --applyLumiMask "Collisions16" "$NAME" --site=$SITE DevTools/Ntuplizer/test/MiniTree_cfg.py isMC=0 crab=1 
submit_job.py crabSubmit --sampleList DevTools/Ntuplizer/data/datasetList_MC.txt --site=$SITE "$NAME" DevTools/Ntuplizer/test/MiniTree_cfg.py isMC=1 crab=1 
#submit_job.py crabSubmit --sampleList DevTools/Ntuplizer/data/datasetList_MC_nonvalid.txt --allowNonValid "$NAME" DevTools/Ntuplizer/test/MiniTree_cfg.py isMC=1 crab=1
submit_job.py crabSubmit --sampleList DevTools/Ntuplizer/data/datasetList_phys03.txt--site=$SITE --inputDBS phys03 "$NAME" DevTools/Ntuplizer/test/MiniTree_cfg.py isMC=1 crab=1
