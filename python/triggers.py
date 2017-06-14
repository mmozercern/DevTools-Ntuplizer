triggerMap = {
    # name : {'path': pathString, 'objects': [objects]},
    # single muon
    'Mu8_TrkIsoVVL'                                        : {'path' : 'HLT_Mu8_TrkIsoVVL_v\\[0-9]+',                                     'objects' : ['muon'], }, # prescaled always
    'Mu17_TrkIsoVVL'                                       : {'path' : 'HLT_Mu17_TrkIsoVVL_v\\[0-9]+',                                    'objects' : ['muon'], }, # prescaled always
    #'IsoMu18'                                              : {'path' : 'HLT_IsoMu18_v\\[0-9]+',                                           'objects' : ['muon'], }, # prescaled 
    'IsoMu20'                                              : {'path' : 'HLT_IsoMu20_v\\[0-9]+',                                           'objects' : ['muon'], }, # prescaled # follow ken
    'IsoMu22'                                              : {'path' : 'HLT_IsoMu22_v\\[0-9]+',                                           'objects' : ['muon'], }, # prescaled 1.05e34 # follow ken
    'IsoMu24'                                              : {'path' : 'HLT_IsoMu24_v\\[0-9]+',                                           'objects' : ['muon'], },
    'IsoMu27'                                              : {'path' : 'HLT_IsoMu27_v\\[0-9]+',                                           'objects' : ['muon'], },
    #'IsoMu22_eta2p1'                                       : {'path' : 'HLT_IsoMu22_eta2p1_v\\[0-9]+',                                    'objects' : ['muon'], },
    #'IsoMu24_eta2p1'                                       : {'path' : 'HLT_IsoMu24_eta2p1_v\\[0-9]+',                                    'objects' : ['muon'], },
    #'IsoTkMu18'                                            : {'path' : 'HLT_IsoTkMu18_v\\[0-9]+',                                         'objects' : ['muon'], }, # prescaled
    'IsoTkMu20'                                            : {'path' : 'HLT_IsoTkMu20_v\\[0-9]+',                                         'objects' : ['muon'], }, # prescaled # follow ken
    'IsoTkMu22'                                            : {'path' : 'HLT_IsoTkMu22_v\\[0-9]+',                                         'objects' : ['muon'], }, # prescaled 1.05e34 # follow ken
    'IsoTkMu24'                                            : {'path' : 'HLT_IsoTkMu24_v\\[0-9]+',                                         'objects' : ['muon'], },
    'IsoTkMu27'                                            : {'path' : 'HLT_IsoTkMu27_v\\[0-9]+',                                         'objects' : ['muon'], },
    #'IsoTkMu24_eta2p1'                                     : {'path' : 'HLT_IsoTkMu24_eta2p1_v\\[0-9]+',                                  'objects' : ['muon'], },
    'Mu45_eta2p1'                                          : {'path' : 'HLT_Mu45_eta2p1_v\\[0-9]+',                                       'objects' : ['muon'], }, # prescaled #follow ken
    'Mu50'                                                 : {'path' : 'HLT_Mu50_v\\[0-9]+',                                              'objects' : ['muon'], },
    'Mu55'                                                 : {'path' : 'HLT_Mu55_v\\[0-9]+',                                              'objects' : ['muon'], },
    'TkMu50'                                               : {'path' : 'HLT_TkMu50_v\\[0-9]+',                                            'objects' : ['muon'], },
    # single electron
    'Ele12_CaloIdL_TrackIdL_IsoVL'                         : {'path' : 'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',                      'objects' : ['electron'], }, # prescaled always
    'Ele17_CaloIdL_TrackIdL_IsoVL'                         : {'path' : 'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',                      'objects' : ['electron'], }, # prescaled always
    'Ele23_CaloIdL_TrackIdL_IsoVL'                         : {'path' : 'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',                      'objects' : ['electron'], }, # prescaled always
    #'Ele22_eta2p1_WPLoose_Gsf'                             : {'path' : 'HLT_Ele22_eta2p1_WPLoose_Gsf_v\\[0-9]+',                          'objects' : ['electron'], }, # prescaled
    #'Ele24_eta2p1_WPLoose_Gsf'                             : {'path' : 'HLT_Ele24_eta2p1_WPLoose_Gsf_v\\[0-9]+',                          'objects' : ['electron'], }, # prescaled
    #'Ele25_eta2p1_WPLoose_Gsf'                             : {'path' : 'HLT_Ele25_eta2p1_WPLoose_Gsf_v\\[0-9]+',                          'objects' : ['electron'], }, # prescaled
    'Ele27_eta2p1_WPLoose_Gsf'                             : {'path' : 'HLT_Ele27_eta2p1_WPLoose_Gsf_v\\[0-9]+',                          'objects' : ['electron'], }, # prescaled # follow ken
    'Ele25_eta2p1_WPTight_Gsf'                             : {'path' : 'HLT_Ele25_eta2p1_WPTight_Gsf_v\\[0-9]+',                          'objects' : ['electron'], },
    'Ele27_eta2p1_WPTight_Gsf'                             : {'path' : 'HLT_Ele27_eta2p1_WPTight_Gsf_v\\[0-9]+',                          'objects' : ['electron'], },
    'Ele30_eta2p1_WPTight_Gsf'                             : {'path' : 'HLT_Ele30_eta2p1_WPTight_Gsf_v\\[0-9]+',                          'objects' : ['electron'], },
    'Ele32_eta2p1_WPTight_Gsf'                             : {'path' : 'HLT_Ele32_eta2p1_WPTight_Gsf_v\\[0-9]+',                          'objects' : ['electron'], },
    #'Ele23_WPLoose_Gsf'                                    : {'path' : 'HLT_Ele23_WPLoose_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], }, # prescaled
    #'Ele27_WPLoose_Gsf'                                    : {'path' : 'HLT_Ele27_WPLoose_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], }, # prescaled
    #'Ele35_WPLoose_Gsf'                                    : {'path' : 'HLT_Ele35_WPLoose_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], }, # removed
    #'Ele45_WPLoose_Gsf'                                    : {'path' : 'HLT_Ele45_WPLoose_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], }, # removed
    #'Ele25_WPTight_Gsf'                                    : {'path' : 'HLT_Ele25_WPTight_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], }, # prescaled
    'Ele27_WPTight_Gsf'                                    : {'path' : 'HLT_Ele27_WPTight_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], },
    'Ele30_WPTight_Gsf'                                    : {'path' : 'HLT_Ele30_WPTight_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], },
    'Ele32_WPTight_Gsf'                                    : {'path' : 'HLT_Ele32_WPTight_Gsf_v\\[0-9]+',                                 'objects' : ['electron'], },
    # single photon
    'Photon175'                                            : {'path' : 'HLT_Photon175_v\\[0-9]+',                                         'objects' : ['photon'], },
    'Photon500'                                            : {'path' : 'HLT_Photon500_v\\[0-9]+',                                         'objects' : ['photon'], },
    'Photon600'                                            : {'path' : 'HLT_Photon600_v\\[0-9]+',                                         'objects' : ['photon'], },
    # double muon
    'Mu17_TrkIsoVVL_Mu8_TrkIsoVVL'                         : {'path' : 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v\\[0-9]+',                      'objects' : ['muon'], }, # prescaled # follow Ken
    'Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'                       : {'path' : 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v\\[0-9]+',                    'objects' : ['muon'], }, # prescaled # follow Ken
    'Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'                      : {'path' : 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v\\[0-9]+',                   'objects' : ['muon'], },
    'Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'                    : {'path' : 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v\\[0-9]+',                 'objects' : ['muon'], },
    # double electron
    #'Ele17_Ele12_CaloIdL_TrackIdL_IsoVL'                   : {'path' : 'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',                'objects' : ['electron'], }, # prescaled
    #'Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'                   : {'path' : 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',                'objects' : ['electron'], }, # prescaled
    'Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'                : {'path' : 'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',             'objects' : ['electron'], }, # prescaled # follow Ken
    'Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'                : {'path' : 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',             'objects' : ['electron'], },
    # electron muon
    'Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL'           : {'path' : 'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',        'objects' : ['electron','muon'], }, # prescaled 9.5e33 #follow Ken
    'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL'           : {'path' : 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',        'objects' : ['electron','muon'], }, # good before run 281639
    'Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'          : {'path' : 'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',       'objects' : ['electron','muon'], }, # prescaled 9.5e33 #follow Ken
    'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL'           : {'path' : 'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',        'objects' : ['electron','muon'], }, # good before run 281639
    'Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'          : {'path' : 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\[0-9]+',       'objects' : ['electron','muon'], }, # good before run 281639
    'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'        : {'path' : 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',     'objects' : ['electron','muon'], }, # >=281639
    'Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'       : {'path' : 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',    'objects' : ['electron','muon'], }, # >=281639
    'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ'        : {'path' : 'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',     'objects' : ['electron','muon'], }, # >=281639
    'Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'       : {'path' : 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\[0-9]+',    'objects' : ['electron','muon'], }, # >=281639
    # double tau
    #'DoubleMediumIsoPFTau32_Trk1_eta2p1_Reg'               : {'path' : 'HLT_DoubleMediumIsoPFTau32_Trk1_eta2p1_Reg_v\\[0-9]+',            'objects' : ['tau'], },
    #'DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg'               : {'path' : 'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v\\[0-9]+',            'objects' : ['tau'], },
    #'DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg'               : {'path' : 'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v\\[0-9]+',            'objects' : ['tau'], },
    'DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg'       : {'path' : 'HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v\\[0-9]+',    'objects' : ['tau'], },
    'DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg'       : {'path' : 'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v\\[0-9]+',    'objects' : ['tau'], },
    # double photon
    'DoublePhoton60'                                       : {'path' : 'HLT_DoublePhoton60_v\\[0-9]+',                                    'objects' : ['photon'], },
    'DoublePhoton85'                                       : {'path' : 'HLT_DoublePhoton85_v\\[0-9]+',                                    'objects' : ['photon'], },
    'Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90'   : {'path' : 'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v\\[0-9]+','objects' : ['photon'], },
    # muon tau
    #'IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1'              : {'path' : 'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v\\[0-9]+',           'objects' : ['muon','tau'], }, # prescaled/removed
    'IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1'              : {'path' : 'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v\\[0-9]+',           'objects' : ['muon','tau'], },
    'IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1'              : {'path' : 'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v\\[0-9]+',           'objects' : ['muon','tau'], },
    #'IsoMu17_eta2p1_LooseIsoPFTau20'                       : {'path' : 'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v\\[0-9]+',                    'objects' : ['muon','tau'], }, # prescaled/removed
    'IsoMu19_eta2p1_LooseIsoPFTau20'                       : {'path' : 'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v\\[0-9]+',                    'objects' : ['muon','tau'], },
    # electron tau
    #'Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : {'path' : 'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\[0-9]+', 'objects' : ['electron','tau'], }, # prescaled
    'Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : {'path' : 'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\[0-9]+', 'objects' : ['electron','tau'], }, # removed
    'Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : {'path' : 'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\[0-9]+', 'objects' : ['electron','tau'], }, # removed
    'Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : {'path' : 'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\[0-9]+', 'objects' : ['electron','tau'], }, # removed
    'Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : {'path' : 'HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\[0-9]+', 'objects' : ['electron','tau'], },
    #'Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20'             : {'path' : 'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v\\[0-9]+',          'objects' : ['electron','tau'], }, # removed
    # triple lepton
    'Ele16_Ele12_Ele8_CaloIdL_TrackIdL'                    : {'path' : 'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v\\[0-9]+',                 'objects' : ['electron'], },
    'Mu8_DiEle12_CaloIdL_TrackIdL'                         : {'path' : 'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v\\[0-9]+',                      'objects' : ['electron','muon'], },
    'DiMu9_Ele9_CaloIdL_TrackIdL'                          : {'path' : 'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v\\[0-9]+',                       'objects' : ['electron','muon'], },
    'TripleMu_12_10_5'                                     : {'path' : 'HLT_TripleMu_12_10_5_v\\[0-9]+',                                  'objects' : ['muon'], },
    
    # other triggers from Kens list:
    'DoubleEle33_CaloIdL_GsfTrkIdVL'                       : {'path' : 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v\\[0-9]+',                   'objects' : ['electron','electron'], },
}
