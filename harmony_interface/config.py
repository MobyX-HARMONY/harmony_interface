import json
import logging
import os

logger = logging.getLogger()

supported_modelIds = set([
        "demo", 
        "demo2", 
        "demo3",
        "demo-multiple-files-1", 
        "demo-multiple-files-2",
        "tfs",
        "ops",
        "onm",
        "trt",
        "rem",
        "dfm_lite",
        "luti_ath"
    ])

class Config:
    def __init__(self):
        self.KAFKA_BOOTSTRAP_SERVERS = 'kafka:29092'
        self.MONGO_DB_URL = "mongodb://tsdwAdmin:d8adm1n@mongodb:27017/tsdwdb_v1_6"
        self.MONGO_DB_NAME = 'tsdwdb_v1_6'

        self.KAFKA_SESSION_TIME_OUT = 6000
        self.KAFKA_MAX_POLL = 10000
        self.KAFKA_GROUP_ID = '200'
        self.KAFKA_OFFSET_RESET = 'earliest'
        self.KAFKA_AUTO_COMMIT_ENABLE = True

        # credential = json.load(open('credentials.json'))
        # logger.warning('credentials: %s', credential)

    def is_allowed_modelId(self, modelId):
        if modelId in supported_modelIds:
            return True
        return False
        
       
# if __name__ == "__main__":
#     Config()
