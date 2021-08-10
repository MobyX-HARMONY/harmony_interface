import logging
from abc import abstractmethod

try:
    from protos.common import progress_pb2,stop_pb2
    from protos.tfs import start_tfs_pb2
except ImportError:
    import sys
    sys.path.append(sys.path[0] + '/..')
    from protos.common import progress_pb2,stop_pb2
    from protos.tfs import start_tfs_pb2

from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer
from confluent_kafka.serialization import StringDeserializer


class KafkaMessageReceiver:

    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        self.logger = logger

    def initialize_receiver(self, model_id):
        self.topic = model_id
        self.check_for_stop_messages()
        self.check_for_progress_messages()
        self.check_for_start_messages()

    def check_for_any_messages(self, protobuf_deserializer):

        string_deserializer = StringDeserializer('utf_8')
        consumer_conf = {
            'session.timeout.ms': 6000,
            'max.poll.interval.ms': 6000,
            'bootstrap.servers': 'kafka:29092',
            'key.deserializer': string_deserializer,
            'value.deserializer': protobuf_deserializer,
            'group.id': '200',
            'auto.offset.reset': "earliest",
            "enable.auto.commit": True,
        }
        consumer = None
        flag = 1
        while flag == 1:
            try:
                consumer = DeserializingConsumer(consumer_conf)
                consumer.subscribe([self.topic])
                self.logger.warning('%s -> Consumer created !',self.topic)
                flag = 2
            except Exception as ex:
                self.logger.warning('%s : Exception while connecting Kafka with Consumer : %s', self.topic, str(ex))

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
                    proto_exp = msg.value()
                    self.start_message_received(proto_exp)

            except Exception as ex:
                self.logger.warning('ops No topic found : %s', str(ex))
        consumer.close()

    def check_for_stop_messages(self):
        protobuf_deserializer = ProtobufDeserializer(stop_pb2.StopModel)
        self.check_for_any_messages(protobuf_deserializer)

    def check_for_progress_messages(self):
        protobuf_deserializer = ProtobufDeserializer(progress_pb2.UpdateServerWithProgress)
        self.check_for_any_messages(protobuf_deserializer)

    def check_for_start_messages(self):
        if self.topic == "tfs":
            protobuf_deserializer = ProtobufDeserializer(start_tfs_pb2.StartTFSModel)
        if self.topic == "ofs":
            pass # TODO
        self.check_for_any_messages(protobuf_deserializer)

    @abstractmethod
    def stop_message_received(self):
        pass

    @abstractmethod
    def progress_message_received(self):
        pass

    @abstractmethod
    def start_message_received(self):
        pass