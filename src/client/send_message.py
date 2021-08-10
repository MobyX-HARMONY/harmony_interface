from pymongo import MongoClient
from kafka import KafkaProducer
import logging
import os
import json
import config
from HARMONY_Interface.kafka_message_sender import KafkaMessageSender

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(os.path.basename(__file__))

client = MongoClient(config.MONGO_DB_URL)
db = client[config.MONGO_DB_NAME]

def send_message_now():
    sender = KafkaMessageSender('tfs')
    sender.send_start_TFS('Asdf_fdsa_lfsa_kqpa')

if __name__ == '__main__':
    log.info("Reading data from database and sending it to consumer")
    # start_kafka_producer()
    send_message_now()
