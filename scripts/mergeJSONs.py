########################
# Run with python3 !!! #
########################

print("########## MERGE THE INDIVIDUAL JSON FILES PRODUCED BY ALL CRAB JOBS INTO A SINGLE JSON PER TRIGGER ##########")

import os
import glob
import json
import sys
base = os.environ.get('CMSSW_RELEASE_BASE')
arch = os.environ.get('SCRAM_ARCH')
path = base+'/bin/'+arch
print("Retrieving mergeJSON.py from",path)
sys.path.append(path)
from mergeJSON import *

#inputs.append(base+'TriggerLuminosity_2022Sep30/ParkingDoubleElectronLowMass*/crab_Run2022C*_part*/220930_*/000*/output_*.json') # Era C
#inputs.append(base+'TriggerLuminosity_2022Sep30/ParkingDoubleElectronLowMass*/crab_Run2022Dv2_part*/220930_*/000*/output_*.json') # Era Dv2

#base='/eos/user/k/klaw/TriggerLuminosity/20230112new/'
#base2='/eos/user/k/klaw/TriggerLuminosity/20230114/'
#base3='/eos/user/k/klaw/TriggerLuminosity/20230118/'

base = '/eos/user/k/klaw/TriggerLuminosity/20230514/'

inputs = []
#inputs.append(base+'triggerluminositynew_2023Jan12/ParkingBPH3/crab_ParkingBPH3/230112_*/000*/output_*.json')
#inputs.append(base2+'triggerluminosity_2023Jan14/ParkingBPH*/crab_ParkingBPH_*/230114_*/000*/output_*.json')
#inputs.append(base3+'triggerluminosity_2023Jan18/ParkingBPH*/crab_ParkingBPHPrompt_*/230118_*/000*/output_*.json') 

inputs.append(base+'triggerluminosity_2023May14/ParkingBPH*/crab_ParkingBPH_*/*/*/output_*.json')
inputs.append(base+'triggerluminosity_2023May14/ParkingBPH*/crab_ParkingBPHPrompt_*/*/*/output_*.json')

#inputs.append(base+'TriggerLuminosity_2022Dec08/ParkingDoubleElectronLowMass*/crab_Run2022C_part*/221208_*/000*/output_*.json') # Era C
#inputs.append(base+'TriggerLuminosity_2022Dec08/ParkingDoubleElectronLowMass*/crab_Run2022Dv1_part*/221208_*/000*/output_*.json') # Era Dv1
#inputs.append(base+'TriggerLuminosity_2022Dec08/ParkingDoubleElectronLowMass*/crab_Run2022Dv2_part*/221208_*/000*/output_*.json') # Era Dv2
#inputs.append(base+'TriggerLuminosity_2022Dec08/ParkingDoubleElectronLowMass*/crab_Run2022E_part*/221208_*/000*/output_*.json') # Era E
#inputs.append(base+'TriggerLuminosity_2022Dec08/ParkingDoubleElectronLowMass*/crab_Run2022F_part*/221208_*/000*/output_*.json') # Era F

files = [ name for input in inputs for name in glob.glob(input) ]
print("len(files)",len(files))
#for filename in files: print(file)

dct = {}
for ifilename,filename in enumerate(files):
    if ifilename % 1000 == 0:
        print("Merging file \""+filename+"\" (number "+str(ifilename)+" out of "+str(len(files))+") ...")
    jsonFile = open(filename,'r')
    jsonDict = json.load(jsonFile)
    for (trigger,runs_lumis) in jsonDict.items():
        #if trigger != "": continue #@@
        lumi_list = LumiList(compactList=runs_lumis)
        #if "357900" not in lumi_list.getRuns(): continue #@@
        if trigger not in dct.keys(): dct[str(trigger)]  = lumi_list
        else:                         dct[str(trigger)] |= lumi_list
    jsonFile.close()
    del(jsonFile)

print()
print("FINAL MERGED JSON:")
print()

for idx,(trigger,lumiList) in enumerate(dct.items()): 
    print(trigger+":")
    print(str(lumiList))
    with open('jsons/currentdralltriggers/{:s}_Excl.json'.format(trigger), 'w') as output: json.dump(lumiList.getCompactList(), output)

################################################################################
################################################################################
################################################################################

# Build list of trigger paths
#triggers = []
#for filename in files:
#    #print("filename:",filename)
#    jsonFile = open(filename,'r')
#    jsonDict = json.load(jsonFile)
#    #print("keys:",jsonDict.keys())
#    for entry in jsonDict.keys() :
#        if str(entry) not in triggers : triggers.append(str(entry))
#print("triggers:",triggers)
#print()

        #if trigger not in dct.keys(): dct[str(trigger)] = LumiList()
        #print("trigger:",trigger," runs_lumis:",runs_lumis)
        #runs_lumis_unpacked = {}
        #for run,lumis in runs_lumis.items(): runs_lumis_unpacked[str(run)] = [int(y) for x in lumis for y in range(x[0],x[1]+1)]

        #runs_lumis_unpacked = {}
        #for run,lumis in runs_lumis.items(): runs_lumis_unpacked[run] = [y for x in lumis for y in range(x[0],x[1]+1)]
        #localList = LumiList(runsAndLumis=runs_lumis_unpacked)


            #localList = LumiList(runsAndLumis=runs_lumis_unpacked)
            #print("localList:",localList)
            #print("dct[trigger] before:",dct[str(trigger)])
            #finalList = dct[str(trigger)]
            #finalList = finalList | lumi_list
            

#            localList = LumiList(runsAndLumis=runs_lumis_unpacked)
#            #print("localList:",localList)
#            #print("dct[trigger] before:",dct[str(trigger)])
#            finalList = dct[str(trigger)]
#            finalList = finalList | localList
#            dct[str(trigger)] = finalList
#
#            runs_lumis_unpacked = {}
#            for run,lumis in runs_lumis.items(): runs_lumis_unpacked[run] = [y for x in lumis for y in range(x[0],x[1]+1)]
#            localList = LumiList(runsAndLumis=runs_lumis_unpacked)
#            #print("localList:",localList)
#            #print("dct[trigger] before:",dct[str(trigger)])
#            finalList = dct[str(trigger)]
#            finalList = finalList | localList
#            dct[str(trigger)] = finalList

            #print("dct[trigger] after:",dct[str(trigger)])

#        for (run,lumis) in run_lumis.items():
#            if run not in dct[trigger].keys(): dct[str(trigger)][str(run)] = LumiList()
#            print("dct[trigger][run] before:",dct[str(trigger)][str(run)])
#            #filterRuns(localList, minRun, maxRun)
#            dct[str(trigger)][str(run)] |= localList
#            #print("dct[trigger] after:",dct[trigger])

#        if trigger not in dct.keys(): dct[str(trigger)] = {}
#        for (run,lumis) in run_lumis.items():
#            if run not in dct[trigger].keys(): dct[str(trigger)][str(run)] = LumiList()
#            print("dct[trigger][run] before:",dct[str(trigger)][str(run)])
#            localList = LumiList(runsAndLumis=lumis)
#            #filterRuns(localList, minRun, maxRun)
#            dct[str(trigger)][str(run)] |= localList
#            #print("dct[trigger] after:",dct[trigger])
