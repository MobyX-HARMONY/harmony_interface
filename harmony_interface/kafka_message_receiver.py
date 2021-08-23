import logging
import time
from abc import abstractmethod
from .protos.common import progress_pb2
from .protos.common import stop_pb2
from .protos.tfs import start_tfs_pb2
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer
from confluent_kafka.serialization import StringDeserializer
from google.protobuf.json_format import MessageToJson
from .config import Config

config = Config()

class KafkaMessageReceiver:
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        self.logger = logger

    def initialize_receiver(self, model_id):
        self.topic = model_id
        self.check_for_start_messages()
        self.check_for_stop_messages()

    def initialize_progress(self, topic_name):
        self.check_for_progress_messages(topic_name)

    def check_for_any_messages(self, kafka_topic, protobuf_deserializer):
        string_deserializer = StringDeserializer('utf_8')
        consumer_conf = {
            'session.timeout.ms': config.KAFKA_SESSION_TIME_OUT,
            'max.poll.interval.ms': config.KAFKA_MAX_POLL,
            'bootstrap.servers': config.KAFKA_BOOTSTRAP_SERVERS,
            'key.deserializer': string_deserializer,
            'value.deserializer': protobuf_deserializer,
            'group.id': config.KAFKA_GROUP_ID,
            'auto.offset.reset': config.KAFKA_OFFSET_RESET,
            "enable.auto.commit": config.KAFKA_AUTO_COMMIT_ENABLE,
        }
        consumer = None
        # flag = 1
        # while flag == 1:
        try:
            consumer = DeserializingConsumer(consumer_conf)
            consumer.subscribe([kafka_topic])
            self.logger.warning('Consumer created with topic %s', kafka_topic)
            flag = 2
        except Exception as ex:
            self.logger.warning('%s : Exception while connecting Kafka with Consumer : %s', kafka_topic, str(ex))

        while True:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            try:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    self.logger.warning("Consumer error: {}".format(msg.error()))
                    continue
                else:
                    self.logger.warning("topic: %s", msg.topic())
                    # proto_exp = msg.value()
                    json_obj = MessageToJson(msg.value())
                    self.logger.warning("Received Proto: %s", json_obj)
                    if msg.topic() == 'tfs':
                        self.start_message_received(json_obj)
                    if msg.topic() == 'tfs_output':
                        self.progress_message_received()

            except Exception as ex:
                self.logger.warning('Exception occured ! : %s', str(ex))
        consumer.close()

    def check_for_stop_messages(self):
        protobuf_deserializer = ProtobufDeserializer(stop_pb2.StopModel)
        self.check_for_any_messages((self.topic + '_stop'), protobuf_deserializer)

    def check_for_progress_messages(self, topic_name):
        protobuf_deserializer = ProtobufDeserializer(progress_pb2.UpdateServerWithProgress)
        self.check_for_any_messages(topic_name, protobuf_deserializer)

    def check_for_start_messages(self):
        self.logger.warning('check_for_start_messages')
        protobuf_deserializer = None
        if self.topic == "tfs":
            protobuf_deserializer = ProtobufDeserializer(start_tfs_pb2.StartTFSModel)
        if self.topic == "ofs":
            pass
        self.check_for_any_messages(self.topic, protobuf_deserializer)

    @abstractmethod
    def start_message_received(self):
        pass

    @abstractmethod
    def progress_message_received(self):
        pass

    @abstractmethod
    def stop_message_received(self):
        pass