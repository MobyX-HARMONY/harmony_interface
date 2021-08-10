# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:47:15 2020

@author: STH
"""

# Import the modules of the Tactical Freight Simulator
import __module_FS__
import __module_SIF__
import __module_SHIP__
import __module_TOUR__
import __module_PARCEL_DMND__
import __module_PARCEL_SCHD__
import __module_SERVICE__
import __module_TRAF__
import __module_OUTP__

# Import configuration settings
import config

# Other libraries
import logging
from pymongo import MongoClient
import time

        
        
#%% Run the modules with given configuration settings
        
if __name__ == '__main__':
    log = logging.getLogger()    
    client = MongoClient(config.MONGO_DB_URL)
    db = client[config.MONGO_DB_NAME]
    data = db[config.TABLE_NAME]
    
    modules = [__module_FS__,       __module_SIF__,         __module_SHIP__,
               __module_TOUR__,     __module_PARCEL_DMND__, __module_PARCEL_SCHD__,
               __module_SERVICE__,  __module_TRAF__,        __module_OUTP__]
    moduleNames = ['FS',        'SIF',          'SHIP',
                   'TOUR',      'PARCEL_DMND',  'PARCEL_SCHD',
                   'SERVICE',   'TRAF',         'OUTP']
    nModules = len(modules)
    
    run = True
    
    for m in range(nModules):
        if run:
            
            module      = modules[m]
            moduleName  = moduleNames[m]
            
            if moduleName in config.varDict['MODULES']:
                print("\n--------------------------------------------------")
                print("Running " + moduleName + " module...")
                print("--------------------------------------------------")
                log.info("Running " + moduleName + " module...")
                
                t0 = time.time()
                result = module.actually_run_module(['', config.varDict])
                runTime = round(time.time() - t0, 1)
                
                log.info(moduleName + " module finished in " + str(runTime) + " seconds.")
                    
                msg = {'name': f'result-{moduleName}', 'data': str(result[1])}
                log.info("Generated file with name: %s", msg['name'])
                
                data.insert_one(msg)
    
                # Print error message
                if result[0] == 1:
                    print('Error in ' + str(moduleName) + ' module!')
                    print(result[1][0])
                    print(result[1][1])
                    run = False
    
    if run:                               
        log.info("Run finished succesfully.")
    else:
        log.info("Run finished because of error(s).")
    
    
    
    
    
    
    
    
    
    
    
    
    