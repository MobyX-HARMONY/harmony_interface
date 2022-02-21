import imp
import logging
from .config import Config
from .protos.common import progress_outputs_pb2
from .protos.common import output_produced_pb2
from .protos.common import progress_pb2
from .protos.common import stop_pb2
from .protos.demo2 import start_demo2_pb2
from .protos.demo import start_demo_pb2
from .protos.tfs import start_tfs_pb2
from .protos.ops import start_ops_pb2
from .protos.onm import start_onm_pb2
from .protos.trt import start_trt_pb2

from uuid import uuid4
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

schema_registry_client = SchemaRegistryClient({'url': 'http://schema-registry:8081'})
config = Config()

class KafkaMessageSender:
    def __init__(self, model_id):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        self.logger = logger
        self.topic = model_id

    def __get_producer_config(self, proto_serializer):
        return {'bootstrap.servers':  config.KAFKA_BOOTSTRAP_SERVERS,
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
            self.logger.warning('PRODUCER MSGS: %s with topic : %s', message, kafka_topic)
            kp.produce(topic=kafka_topic, value=message, key=str(uuid4()), on_delivery=self.__delivery_report)
            kp.poll(0)
        except Exception as ex:
            self.logger.warning('Exception in publishing message %s', str(ex))
        kp.flush()

    def send_progress_and_outputs(self, scenario_id, percent, outputList):
        serializer = ProtobufSerializer(progress_outputs_pb2.UpdateServerWithProgressAndOutputs, schema_registry_client)
        progress_output_conf = self.__get_producer_config(serializer)
        message = progress_outputs_pb2.UpdateServerWithProgressAndOutputs(
            scenarioId = scenario_id,
            percentage = int(percent),
            outputs = outputList
        )
        self.logger.warning('PROGRESS AND OUTPUTS: %s', message)
        self.__send_anything((self.topic + '_progress'), message, progress_output_conf)
        
    def send_output_produced(self, scenario_id, key, value):
        serializer = ProtobufSerializer(output_produced_pb2.UpdateServerWithOutputMetaData, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = output_produced_pb2.UpdateServerWithOutputMetaData(
            scenarioId=scenario_id,
            key=key,
            value=value
        )

        self.logger.warning('OUTPUT PRODUCED: %s', message)
        self.__send_anything((self.topic + '_outputs'), message, conf)

    def send_progress(self, exp_id, percent):
        progress_serializer = ProtobufSerializer(progress_pb2.UpdateServerWithProgress, schema_registry_client)
        progress_conf = self.__get_producer_config(progress_serializer)
        progress_message = progress_pb2.UpdateServerWithProgress(experiment_id=exp_id, percentage=int(percent))

        self.logger.warning('PROGRESS: %s', progress_message)
        self.__send_anything((self.topic + '_progress'), progress_message, progress_conf)

    def send_stop(self, experiment_id):
        # easy, just use the stop proto from the common folder
        self.logger.warning('MESSAGE: STOP ')
        message = stop_pb2.StopModel(experiment_id=experiment_id)
        self.__send_anything(message)

    def send_start_demo2(self, params):
        self.logger.warning('START DEMO2')
        self.logger.warning('params["inputs"]')
        self.logger.warning(params["inputs"])
        inputs = start_demo2_pb2.StartDemo2Component.Inputs(**params["inputs"])
        outputs = start_demo2_pb2.StartDemo2Component.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        serializer = ProtobufSerializer(start_demo2_pb2.StartDemo2Component, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo2_pb2.StartDemo2Component(scenarioId=scenarioId,inputs=inputs,outputs=outputs)

        self.__send_anything(self.topic, message, conf)

    def send_start_demo(self, params):
        self.logger.warning('START DEMO')

        inputs = start_demo_pb2.StartDemoComponent.Inputs(**params["inputs"])
        outputs = start_demo_pb2.StartDemoComponent.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        serializer = ProtobufSerializer(start_demo_pb2.StartDemoComponent, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo_pb2.StartDemoComponent(scenarioId=scenarioId,inputs=inputs,outputs=outputs)

        self.__send_anything(self.topic, message, conf)

    def send_start_tfs(self, experiment_id):
        # eventually, we should pass more parameters via this function
        self.logger.warning('START TFS')
        start_tfs_serializer = ProtobufSerializer(start_tfs_pb2.StartTFSModel, schema_registry_client)
        start_tfs_conf = self.__get_producer_config(start_tfs_serializer)
        message = start_tfs_pb2.StartTFSModel(experiment_id=experiment_id)
        self.__send_anything(self.topic, message, start_tfs_conf)

    def send_start_ofs(self):
        pass

    def start_ops(self, experiment_id):
        self.logger.warning('START OPS')
        start_ops_serializer = ProtobufSerializer(start_ops_pb2.StartOPSModel, schema_registry_client)
        start_ops_conf = self.__get_producer_config(start_ops_serializer)
        message = start_ops_pb2.StartOPSModel(experiment_id=experiment_id)
        self.__send_anything(self.topic, message, start_ops_conf)

    def start_onm(self, experiment_id):
        self.logger.warning('START ONM')
        start_onm_serializer = ProtobufSerializer(start_onm_pb2.StartONMModel, schema_registry_client)
        start_onm_conf = self.__get_producer_config(start_onm_serializer)
        message = start_onm_pb2.StartONMModel(experiment_id=experiment_id)
        self.__send_anything(self.topic, message, start_onm_conf)

    def start_trt(self, experiment_id):
        self.logger.warning('START TRT')
        start_trt_serializer = ProtobufSerializer(start_trt_pb2.StartTRTModel, schema_registry_client)
        start_trt_conf = self.__get_producer_config(start_trt_serializer)
        message = start_trt_pb2.StartTRTModel(experiment_id=experiment_id)
        self.__send_anything(self.topic, message, start_trt_conf)

class ComponentKafkaMessageSender(KafkaMessageSender):
    def send_progress(self, experiment_id, percentage):
        super().send_progress()
