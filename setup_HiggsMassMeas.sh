#!/bin/bash

export PYTHONPATH=${PYTHONPATH}:${PWD}
export PYTHONPATH=$PYTHONPATH:${PWD}/leptonPtErrorCorrector/doCorrection/
export PATH=${PATH}:${PWD}/bin
export BASE_PATH=${PWD}

cd /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_32/src/
eval `scramv1 runtime -sh`
cd -
