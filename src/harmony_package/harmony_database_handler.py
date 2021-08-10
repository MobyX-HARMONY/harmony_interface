from pymongo import MongoClient
import config
import logging

class HarmonyDatabaseHandler:

    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        self.logger = logger
        self.client = MongoClient(config.MONGO_DB_URL)
        self.db = self.client[config.MONGO_DB_NAME]

    def save_collectionList_to_db(self, collectionName, collectionData):
        self.logger.warning("tableName: %s\nData: %s", collectionName, collectionData)
        collection = self.db[collectionName]
        try:
            collection.insert_many(collectionData)
        except Exception as e:
            self.logger.warning('Exception occured: %s',e)
        self.logger.warning("table Name: %s", collectionName)

    def save_collection_to_db(self, collectionName, collectionData):
        self.logger.warning("tableName: %s", collectionName)
        collection = self.db[collectionName]
        try:
            collection.insert_one(collectionData)
        except Exception as e:
            self.logger.warning('Exception Occured: %s',e)