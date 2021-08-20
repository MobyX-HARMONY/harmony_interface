import logging
import time

from .protos.common import progress_pb2
from .protos.common import stop_pb2
from .protos.tfs import start_tfs_pb2

from uuid import uuid4
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

schema_registry_client = SchemaRegistryClient({'url': 'http://schema-registry:8081'})
# schema_registry_client.set_compatibility("Harmony", "None")
# protobuf_serializer = ProtobufSerializer(start_tfs_pb2.StartTFSModel, schema_registry_client)

# producer_conf = {'bootstrap.servers':  'kafka:29092',
#                  'key.serializer': StringSerializer('utf_8'),
#                  'value.serializer': protobuf_serializer}

class KafkaMessageSender:
    def __init__(self, model_id):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        self.logger = logger
        self.topic = model_id

    def __get_producer_config(self, proto_serializer):
        return {'bootstrap.servers':  'kafka:29092',
                'key.serializer': StringSerializer('utf_8'),
                'value.serializer': proto_serializer}

    def __delivery_report(self, err, msg):
        if err is not None:
            self.logger.warning('Sender message delivery failed: {}'.format(err))
        else:
            self.logger.warning('Sender message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def __send_anything(self, kafka_topic, message, conf):
        kp = None
        try:
            kp = SerializingProducer(conf)
        except Exception as ex:
            self.logger.warning('Exception while connecting Kafka with Producer : %s', str(ex))
        try:
            self.logger.warning('PRODUCER MSGS: %s', message)
            kp.produce(topic=kafka_topic, value=message, key=str(uuid4()), on_delivery=self.__delivery_report)
            kp.poll(0)
        except Exception as ex:
            self.logger.warning('Exception in publishing message %s', str(ex))
        kp.flush()
        # time.sleep(3)

    def send_progress(self, exp_id, percent):
        # time.sleep(1)
        # easy, just use the progress proto from the common folder
        self.logger.warning('progress : %s', percent)

        progress_serializer = ProtobufSerializer(progress_pb2.UpdateServerWithProgress, schema_registry_client)
        progress_conf = self.__get_producer_config(progress_serializer)
        progress_message = progress_pb2.UpdateServerWithProgress(experiment_id=exp_id, percentage=str(percent))

        self.logger.warning('progress_message: %s', progress_message)
        self.__send_anything(self.topic + '_output', progress_message, progress_conf)

    def send_stop(self, experiment_id):
        # easy, just use the stop proto from the common folder
        self.logger.warning('stop ')
        message = stop_pb2.StopModel(experiment_id=experiment_id)
        self.__send_anything(message)

    def send_start_TFS(self, experiment_id):
        # eventually, we should pass more parameters via this function
        self.logger.warning('start TFS')
        start_tfs_serializer = ProtobufSerializer(start_tfs_pb2.StartTFSModel, schema_registry_client)
        start_tfs_conf = self.__get_producer_config(start_tfs_serializer)
        message = start_tfs_pb2.StartTFSModel(experiment_id=experiment_id)
        self.__send_anything(self.topic, message, start_tfs_conf)

    def send_start_OFS(self):
        # similar to the TFS case, but using a different proto file
        None


class ComponentKafkaMessageSender(KafkaMessageSender):

    def send_progress(self, experiment_id, percentage):
        super().send_progress()

