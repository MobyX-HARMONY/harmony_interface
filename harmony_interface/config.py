import json
import os

class Config:
    def __init__(self):
        self.KAFKA_BOOTSTRAP_SERVERS = 'kafka:29092'
        self.MONGO_DB_URL = "mongodb://tsdwAdmin:d8adm1n@mongodb:27017/tsdwdb_v1_6"
        self.MONGO_DB_NAME = 'tsdwdb_v1_6'

        self.KAFKA_SESSION_TIME_OUT = 6000
        self.KAFKA_MAX_POLL = 16000
        self.KAFKA_GROUP_ID = '200'
        self.KAFKA_OFFSET_RESET = 'earliest'
        self.KAFKA_AUTO_COMMIT_ENABLE = True

        # credential = json.load(open('../credentials.json'))
        # print(credential)


    def get_group_id(self, topic_name):
        if topic_name == 'demo': return 211
        if topic_name == 'demo2': return 221
        if topic_name == 'demo3': return 231
        if topic_name == 'demo-multiple-files-1': return 241
        if topic_name == 'demo-multiple-files-2': return 251


        
# if __name__ == "__main__":
#     Config()