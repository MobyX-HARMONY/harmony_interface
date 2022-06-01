import imp
import logging
from .config import Config
from .protos.common import progress_outputs_pb2
from .protos.common import stop_pb2
from .protos.demoMultipleFiles import start_demo_multiple_files_pb2
from .protos.demoMultipleFiles2 import start_demo_multiple_files2_pb2
from .protos.demo3 import start_demo3_pb2
from .protos.demo2 import start_demo2_pb2
from .protos.demo import start_demo_pb2
from .protos.tfs import start_tfs_pb2
from .protos.rem import start_rem_pb2
from .protos.dfm_lite import start_dfm_lite_pb2
from .protos.dfm_lite_partial import start_dfm_lite_partial_pb2
from .protos.luti_ath import start_luti_ath_pb2

from uuid import uuid4
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

schema_registry_client = SchemaRegistryClient({'url': 'http://schema-registry:8081'})
config = Config()

class KafkaMessageSender(object):
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

    def send_progress_and_outputs(self, scenarioId, percent, outputList):
        serializer = ProtobufSerializer(progress_outputs_pb2.UpdateServerWithProgressAndOutputs, schema_registry_client)
        progress_output_conf = self.__get_producer_config(serializer)
        message = progress_outputs_pb2.UpdateServerWithProgressAndOutputs(
            scenarioId = scenarioId,
            percentage = int(percent),
            outputs = outputList
        )
        self.logger.warning('PROGRESS AND OUTPUTS: %s', message)
        self.__send_anything((self.topic + '_progress_output'), message, progress_output_conf)

    def send_stop(self, experiment_id):
        self.logger.warning('MESSAGE: STOP ')
        message = stop_pb2.StopModel(experiment_id=experiment_id)
        self.__send_anything(message)

    def send_start_demo_multiple_files(self, params):
        self.logger.warning('START DEMO MULTIPLE FILES')
        self.logger.warning('params["inputs"]')
        self.logger.warning(params["inputs"])
        inputs = start_demo_multiple_files_pb2.StartDemoMultipleFilesComponent.Inputs(**params["inputs"])
        outputs = start_demo_multiple_files_pb2.StartDemoMultipleFilesComponent.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        serializer = ProtobufSerializer(start_demo_multiple_files_pb2.StartDemoMultipleFilesComponent, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo_multiple_files_pb2.StartDemoMultipleFilesComponent(scenarioId=scenarioId,inputs=inputs,outputs=outputs)

        self.__send_anything(self.topic, message, conf)

    def send_start_demo_multiple_files2(self, params):
        self.logger.warning('START DEMO MULTIPLE FILES 2')
        self.logger.warning('params["inputs"]')
        self.logger.warning(params["inputs"])
        inputs = start_demo_multiple_files2_pb2.StartDemoMultipleFilesComponent2.Inputs(**params["inputs"])
        outputs = start_demo_multiple_files2_pb2.StartDemoMultipleFilesComponent2.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        serializer = ProtobufSerializer(start_demo_multiple_files2_pb2.StartDemoMultipleFilesComponent2, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo_multiple_files2_pb2.StartDemoMultipleFilesComponent2(scenarioId=scenarioId,inputs=inputs,outputs=outputs)

        self.__send_anything(self.topic, message, conf)

    def send_start_demo3(self, params):
        self.logger.warning('START DEMO_3')
        self.logger.warning('params["inputs"]')
        self.logger.warning(params["inputs"])
        inputs = start_demo3_pb2.StartDemo3Component.Inputs(**params["inputs"])
        outputs = start_demo3_pb2.StartDemo3Component.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        serializer = ProtobufSerializer(start_demo3_pb2.StartDemo3Component, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo3_pb2.StartDemo3Component(scenarioId=scenarioId,inputs=inputs,outputs=outputs)

        self.__send_anything(self.topic, message, conf)

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
        self.logger.warning('START DEMO params: %s', params)

        inputs = start_demo_pb2.StartDemoComponent.Inputs(**params["inputs"])
        outputs = start_demo_pb2.StartDemoComponent.Outputs(**params["outputs"])

        scenarioId = params["scenarioId"]
        testVal = params["testValue"]

        self.logger.warning('testValue: %s', testVal)
        
        serializer = ProtobufSerializer(start_demo_pb2.StartDemoComponent, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_demo_pb2.StartDemoComponent(scenarioId = scenarioId,testValue = testVal, inputs = inputs, outputs = outputs)

        self.__send_anything(self.topic, message, conf)

    def send_start_tfs(self, params):
        self.logger.warning('START TFS params: %s', params)
        inputs = start_tfs_pb2.StartTFS.Inputs(**params["inputs"])
        outputs = start_tfs_pb2.StartTFS.Outputs(**params["outputs"])
        serializer = ProtobufSerializer(start_tfs_pb2.StartTFS, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_tfs_pb2.StartTFS(scenarioId = params["scenarioId"], inputs = inputs, outputs = outputs)
        self.__send_anything(self.topic, message, conf)

    def send_start_ofs(self):
        pass

    def send_start_rem(self, params):
        self.logger.warning('START REM params: %s', params)
        inputs = start_rem_pb2.StartREM.Inputs(**params["inputs"])
        outputs = start_rem_pb2.StartREM.Outputs(**params["outputs"])
        serializer = ProtobufSerializer(start_rem_pb2.StartREM, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_rem_pb2.StartREM(scenarioId = params["scenarioId"], inputs = inputs, outputs = outputs)
        self.__send_anything(self.topic, message, conf)

    def send_start_dfm_lite(self, params):
        self.logger.warning('START DFMLite params: %s', params)
        inputs = start_dfm_lite_pb2.StartDFMLite.Inputs(**params["inputs"])
        outputs = start_dfm_lite_pb2.StartDFMLite.Outputs(**params["outputs"])
        serializer = ProtobufSerializer(start_dfm_lite_pb2.StartDFMLite, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_dfm_lite_pb2.StartDFMLite(scenarioId = params["scenarioId"], inputs = inputs, outputs = outputs)
        self.__send_anything(self.topic, message, conf)

    def send_start_dfm_lite_partial(self, params):
        self.logger.warning('START DFMLite partial params: %s', params)
        inputs = start_dfm_lite_partial_pb2.StartDFMLitePartial.Inputs(**params["inputs"])
        outputs = start_dfm_lite_partial_pb2.StartDFMLitePartial.Outputs(**params["outputs"])
        serializer = ProtobufSerializer(start_dfm_lite_partial_pb2.StartDFMLitePartial, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_dfm_lite_partial_pb2.StartDFMLitePartial(scenarioId = params["scenarioId"], inputs = inputs, outputs = outputs)
        self.__send_anything(self.topic, message, conf)

    def send_start_luti_ath(self, params):
        self.logger.warning('START LUTI ATH params: %s', params)
        inputs = start_luti_ath_pb2.StartLutiAth.Inputs(**params["inputs"])
        outputs = start_luti_ath_pb2.StartLutiAth.Outputs(**params["outputs"])
        serializer = ProtobufSerializer(start_luti_ath_pb2.StartLutiAth, schema_registry_client)
        conf = self.__get_producer_config(serializer)
        message = start_luti_ath_pb2.StartLutiAth(scenarioId = params["scenarioId"], inputs = inputs, outputs = outputs)
        self.__send_anything(self.topic, message, conf)

class ComponentKafkaMessageSender(KafkaMessageSender):
    def send_progress(self, experiment_id, percentage):
        super().send_progress()
