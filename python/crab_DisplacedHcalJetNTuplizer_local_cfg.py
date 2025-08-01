# -----------------------------------------------------------------------------------------------------------------------------
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial  #**Up-to-date**
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile #
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3CheatSheet        #
#
# Environment setup:
#    cmsenv
#    source /cvmfs/cms.cern.ch/crab3/crab.sh
# To submit:
#    crab submit -c MyCrabConfig_Splash.py
# To check status:
#    crab status -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# To kill jobs:
#    crab kill -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# To retrieve output:
#    crab getoutput -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# -----------------------------------------------------------------------------------------------------------------------------
from CRABClient.UserUtilities import config
#from CRABClient.UserUtilities import getUsernameFromSiteDB

# Select dataset to crab over
number = 0 # starting at 0 -> refers to datasetnames # number wrapper

# List of possible datasets
datasetnames = ['/JetMET1/Run2025C-v1/RAW']# dataset wrapper

datasetblock = [
#'/DisplacedJet/Run2023C-EXOLLPJetHCAL-PromptReco-v4/AOD#0882cc9a-f2ab-4626-992e-c787a9d5017c' # in 2023C v4
]

# runrange = '362085,362087' # Nov2022 Phase Scan
#runrange = '392175,392194,392196'

# JSON files for lumiMask are available at: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/
lumimask = ''#'/eos/user/e/ethazelt/projects/LLPNTupler_timeFocused/CMSSW_15_0_6/src/cms_lpc_llp/Run3-HCAL-LLP-NTupler-TimeFocused/python/lumimask_PhaseScan2025.json'

# Storage path for output files - EOS specific
#storagepath = '/store/user/'+getUsernameFromSiteDB()+'/HCALnoise2016'

# cmsRun file
psetname = 'DisplacedHcalJetNTuplizer.py'

# Output filename
#OutputFilename = '/eos/home-k/kikenned/HCALtupleMaker/CrabOutput_Run'+runrange+'.root'

# Storage site of output files
storageSite = 'T2_US_Wisconsin' # no write access to: 'T2_CH_CERN'

# White list sites
whiteList = ['T2_US_Caltech','T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin', 'T1_US_FNAL','T2_US_MIT','T1_FR_CCIN2P3']
# ['T2_US_UCSD']

# Black list sites
blackList = ['']

# -----------------------------------------------------------------------------------------------------------------------------
# No modifications below this line are necessary

import datetime
timestamp = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S")
date = datetime.datetime.now().strftime("_%Y%m%d")

dataset = filter(None, datasetnames[number].split('/'))
dataset = list(dataset)

config = config()

# General
config.General.workArea        = 'crab_LLPNtupler_JetMET1_Run2025C-v1_RAW_392175_94_96' # workArea wrapper
config.General.instance        = 'prod'
config.General.requestName     = 'LLPNtupler'+'_'+dataset[0]+'_'+dataset[1]+'_'+dataset[2]+timestamp  # requestName wrapper
config.General.transferOutputs = True
config.General.transferLogs    = True

# JobType
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = psetname
#config.JobType.outputFiles = [OutputFilename]
#config.JobType.pyCfgParams = ['outputFile='+OutputFilename]
config.JobType.maxMemoryMB = 3500
config.JobType.maxJobRuntimeMin = 1980

# Data
# four below lines for standard dataset input
config.Data.inputDataset     = ''
config.Data.userInputFiles   = open('/eos/user/e/ethazelt/projects/LLPNTupler_timeFocused/CMSSW_15_0_6/src/cms_lpc_llp/Run3-HCAL-LLP-NTupler-TimeFocused/python/local_JetMET1_PS2025.txt').readlines()
config.Data.inputDBS         = 'global'
config.Data.splitting        = 'FileBased'
config.Data.unitsPerJob      = 1
config.Data.ignoreLocality   = True
config.Data.publication      = False
config.Data.outputDatasetTag = 'LLPNtupler'+'_'+dataset[1]+'_'+dataset[2]+timestamp # outputDatasetTag wrapper
config.Data.outputPrimaryDataset = 'JetMET1'

#config.Data.runRange        =  '1'
if lumimask != '':
  config.Data.lumiMask        = lumimask

config.Site.storageSite = storageSite

config.Site.whitelist = whiteList

if not blackList:
    config.Site.blacklist = blackList
