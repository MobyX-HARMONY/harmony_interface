from pymongo import MongoClient
import logging
import os
import config

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(os.path.basename(__file__))

client = MongoClient(config.MONGO_DB_URL)
db = client[config.MONGO_DB_NAME]

if __name__ == '__main__':
    for i in range(10):
        msg = {'name': 'testData', 'number': i}
        log.debug("Generated JSON file: %s", msg)
        data = db[config.TABLE_NAME]
        data.insert_one(msg)

    log.info("Data generation completed.")