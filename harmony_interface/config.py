
class Config:
    def __init__(self):
        self.KAFKA_BOOTSTRAP_SERVERS = 'kafka:29092'
        self.MONGO_DB_URL = 'mongodb://mongodb:27017/'
        self.MONGO_DB_NAME = 'MobyXDB'

        self.KAFKA_SESSION_TIME_OUT = 6000
        self.KAFKA_MAX_POLL = 6000
        self.KAFKA_GROUP_ID = '200'
        self.KAFKA_OFFSET_RESET = 'earliest'
        self.KAFKA_AUTO_COMMIT_ENABLE = True