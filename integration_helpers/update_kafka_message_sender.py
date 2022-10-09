new_topic_name = "ldm_tur"
start_class_name = "StartLdmTur"
file_name = "../harmony_interface/kafka_message_sender.py"
new_file_name = file_name

start_class_package = "start_" + new_topic_name + "_pb2"
start_class_full_name = start_class_package + "." + start_class_name

with open(file_name) as f:
    lines = f.readlines()

    new_lines = []
    for line in lines:
        if "from .protos.common import progress_outputs_pb2" in line:
            new_lines.append("from .protos." + new_topic_name + " import " + start_class_package + "\n")
        if "class ComponentKafkaMessageSender(KafkaMessageSender):" in line:
            new_lines.append("    def send_start_{}(self, params):\n".format(new_topic_name))
            new_lines.append("        self.logger.warning('START {} params: %s', params)\n".format(new_topic_name))
            new_lines.append("        inputs = {}.Inputs(**params[\"inputs\"])\n".format(start_class_full_name))
            new_lines.append("        outputs = {}.Outputs(**params[\"outputs\"])\n".format(start_class_full_name))
            new_lines.append("        serializer = ProtobufSerializer({}, schema_registry_client)\n".format(start_class_full_name))
            new_lines.append("        conf = self.__get_producer_config(serializer)\n")
            new_lines.append("        message = {}(scenarioId = params[\"scenarioId\"], inputs = inputs, outputs = outputs)\n".format(start_class_full_name))
            new_lines.append("        self.__send_anything(self.topic, message, conf)\n")
            new_lines.append("\n")
        new_lines.append(line)

    proto_file = open(new_file_name, "w")
    n = proto_file.writelines(new_lines)
    proto_file.close()

    print("New file generated.")
