#%% Docker related settings

MONGO_DB_URL = 'mongodb://mongodb:27017/'
MONGO_DB_NAME = 'Harmony'
TABLE_NAME = 'Data-TFS-test-run-001'

KAFKA_TOPIC_NAME = 'TFS-test-run-001'
KAFKA_BROKERS = ['kafka:9092']

#%% TFS configuration settings

# Dictionary in which we store all configuation arguments
varDict = {}

# Which modules to run
varDict['MODULES'] = ['FS', 'SIF', 'SHIP', 'TOUR','PARCEL_DMND','PARCEL_SCHD','SERVICE','TRAF','OUTP']
# varDict['MODULES'] = ['PARCEL_SCHD']

# Which scenario to run (REF or UCC)
varDict['LABEL'] = 'REF'

# General folders
COMMONFOLDER = '/tfs/data'
INPUTFOLDER = COMMONFOLDER + '/data/2016/'
PARAMFOLDER = COMMONFOLDER + '/parameters/'
varDict['INPUTFOLDER']  = INPUTFOLDER
varDict['OUTPUTFOLDER'] = COMMONFOLDER + '/runs/RunREF2016/'
varDict['PARAMFOLDER']  = PARAMFOLDER

# Input files
varDict['SKIMTIME']             = COMMONFOLDER + '/data/LOS/2016/skimTijd_REF.mtx'
varDict['SKIMDISTANCE']         = COMMONFOLDER + '/data/LOS/2016/skimAfstand_REF.mtx'
varDict['LINKS']                = INPUTFOLDER + 'links_v5.shp'
varDict['NODES']                = INPUTFOLDER + 'nodes_v5.shp'
varDict['ZONES']                = INPUTFOLDER + 'Zones_v5.shp'
varDict['SEGS']                 = INPUTFOLDER + 'SEGS2016_verrijkt.csv'
varDict['COMMODITYMATRIX']      = INPUTFOLDER + 'CommodityMatrixNUTS3_2016.csv'
varDict['PARCELNODES']          = INPUTFOLDER + 'parcelNodes_v2.shp'
varDict['CEP_SHARES']           = INPUTFOLDER + 'CEPshares.csv'
varDict['DISTRIBUTIECENTRA']    = INPUTFOLDER + 'distributieCentra.csv'
varDict['CORRECTIONS_TONNES']   = INPUTFOLDER + 'CorrectionsTonnes2016.csv'
varDict['COST_VEHTYPE']          = PARAMFOLDER + 'Cost_VehType_2016.csv'
varDict['COST_SOURCING']         = PARAMFOLDER + 'Cost_Sourcing_2016.csv'
varDict['MRDH_TO_NUTS3']         = PARAMFOLDER + 'MRDHtoNUTS32013.csv'
varDict['NUTS3_TO_MRDH']         = PARAMFOLDER + 'NUTS32013toMRDH.csv'
varDict['SERVICE_DISTANCEDECAY'] = PARAMFOLDER + 'Params_DistanceDecay_SERVICE.csv'

# Numeric parameters
varDict['YEARFACTOR'        ] = 5000 # Actually 209, but higher for shorter runtime in testing
varDict['NUTSLEVEL_INPUT'   ] = 3
varDict['PARCELS_PER_HH'    ] = 0.112
varDict['PARCELS_PER_EMPL'  ] = 0.041
varDict['PARCELS_MAXLOAD'   ] = 180
varDict['PARCELS_DROPTIME'  ] = 120
varDict['PARCELS_SUCCESS_B2C'   ] = 0.75
varDict['PARCELS_SUCCESS_B2B'   ] = 0.95
varDict['PARCELS_GROWTHFREIGHT' ] = 1.0

# Crowdshipping parameters
varDict['CROWDSHIPPING']    = 'FALSE'
varDict['CRW_PARCELSHARE']  = 0.06
varDict['CRW_MODEPARAMS']   = PARAMFOLDER + 'Params_UseCase_CrowdShipping.csv'
varDict['CRW_PDEMAND_CAR']  = INPUTFOLDER + 'MRDH_2016_Auto_Etmaal.mtx'
varDict['CRW_PDEMAND_BIKE'] = INPUTFOLDER + 'MRDH_2016_Fiets_Etmaal.mtx'

# Traffic assignment parameters
varDict['IMPEDANCE_SPEED_FREIGHT'] = 'V_FR_OS'
varDict['IMPEDANCE_SPEED_VAN']     = 'V_PA_OS'
varDict['N_MULTIROUTE']            = 1

# Some optional parameters
varDict['SHIPMENTS_REF'] = ""
varDict['SELECTED_LINKS'] = ""
varDict['N_CPU'] = ""


        
