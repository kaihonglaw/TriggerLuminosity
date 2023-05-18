import FWCore.ParameterSet.Config as cms

unpackedPatTrigger = cms.EDProducer(
    "PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag('slimmedPatTrigger'),
    triggerResults              = cms.InputTag('TriggerResults::HLT'),
    unpackFilterLabels = cms.bool(True)
)

# Order is important !!!
seeds = [
    'L1_SingleMu6er1p5',
    'L1_SingleMu7er1p5',
    'L1_SingleMu8er1p5',
    'L1_SingleMu9er1p5',
    'L1_SingleMu10er1p5',
    'L1_SingleMu12er1p5',
    'L1_SingleMu14er1p5',
    'L1_SingleMu16er1p5',
    'L1_SingleMu18er1p5',
    'L1_SingleMu22',
]

# Order is important !!!
paths=[
    'HLT_Mu7_IP4_part0',
    'HLT_Mu7_IP4_part1',
    'HLT_Mu7_IP4_part2',
    'HLT_Mu7_IP4_part3',
    'HLT_Mu7_IP4_part4',
    'HLT_Mu7_IP4_part5',
    'HLT_Mu8_IP3_part0',
    'HLT_Mu8_IP3_part1',
    'HLT_Mu8_IP3_part2',
    'HLT_Mu8_IP3_part3',
    'HLT_Mu8_IP3_part4',
    'HLT_Mu8_IP3_part5',
    'HLT_Mu8_IP5_part0',
    'HLT_Mu8_IP5_part1',
    'HLT_Mu8_IP5_part2',
    'HLT_Mu8_IP5_part3',
    'HLT_Mu8_IP5_part4',
    'HLT_Mu8_IP5_part5',
    'HLT_Mu8_IP6_part0',
    'HLT_Mu8_IP6_part1',
    'HLT_Mu8_IP6_part2',
    'HLT_Mu8_IP6_part3',
    'HLT_Mu8_IP6_part4',
    'HLT_Mu8_IP6_part5',
    'HLT_Mu8p5_IP3p5_part0',
    'HLT_Mu8p5_IP3p5_part1',
    'HLT_Mu8p5_IP3p5_part2',
    'HLT_Mu8p5_IP3p5_part3',
    'HLT_Mu8p5_IP3p5_part4',
    'HLT_Mu8p5_IP3p5_part5',
    'HLT_Mu9_IP4_part0',
    'HLT_Mu9_IP4_part1',
    'HLT_Mu9_IP4_part2',
    'HLT_Mu9_IP4_part3',
    'HLT_Mu9_IP4_part4',
    'HLT_Mu9_IP4_part5',
    'HLT_Mu9_IP5_part0',
    'HLT_Mu9_IP5_part1',
    'HLT_Mu9_IP5_part2',
    'HLT_Mu9_IP5_part3',
    'HLT_Mu9_IP5_part4',
    'HLT_Mu9_IP5_part5',   
    'HLT_Mu9_IP6_part0',
    'HLT_Mu9_IP6_part1',
    'HLT_Mu9_IP6_part2',
    'HLT_Mu9_IP6_part3',
    'HLT_Mu9_IP6_part4',
    'HLT_Mu9_IP6_part5',
    'HLT_Mu10p5_IP3p5_part0',
    'HLT_Mu10p5_IP3p5_part1',
    'HLT_Mu10p5_IP3p5_part2',
    'HLT_Mu10p5_IP3p5_part3',
    'HLT_Mu10p5_IP3p5_part4',
    'HLT_Mu10p5_IP3p5_part5',
    'HLT_Mu12_IP6_part0',
    'HLT_Mu12_IP6_part1',
    'HLT_Mu12_IP6_part2',
    'HLT_Mu12_IP6_part3',
    'HLT_Mu12_IP6_part4',
    'HLT_Mu12_IP6_part5',  
]

miniAODTriggerAnalyzer = cms.EDAnalyzer(
    "MiniAODTriggerAnalyzer",
    HLTProcess = cms.string('HLT'),
    HLTPaths = cms.vstring(paths),
    L1Seeds = cms.vstring(seeds),
    cfg = cms.PSet(
        stageL1Trigger = cms.uint32(2),
        l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
        l1tExtBlkInputTag = cms.InputTag('gtStage2Digis')
    ),
    bits = cms.InputTag("TriggerResults","","HLT"),
    prescales = cms.InputTag("patTrigger"),
    objects = cms.InputTag("unpackedPatTrigger"),
    Verbose = cms.int32(1),
    OnlyLowestUnprescaledHltPath = cms.bool(True),
    ModuloPrescale = cms.int32(100), # Only analyse 1/N events (for speed) if trigger rate permits
)

miniAODTriggerSequence = cms.Sequence(
    unpackedPatTrigger+
    miniAODTriggerAnalyzer
)
