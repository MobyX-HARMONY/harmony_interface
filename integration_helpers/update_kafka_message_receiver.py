new_topic_name = "ldm_tur"
start_class_name = "StartLdmTur"
file_name = "../harmony_interface/kafka_message_receiver.py"
new_file_name = file_name

start_class_package = "start_" + new_topic_name + "_pb2"
start_class_full_name = start_class_package + "." + start_class_name

with open(file_name) as f:
    lines = f.readlines()

    new_lines = []
    for line in lines:
        if "from .config import Config" in line:
            new_lines.append("from .protos." + new_topic_name + " import " + start_class_package + "\n")
        if "if protobuf_deserializer is None:" in line:
            new_lines.append("        elif self.topic == \"" + new_topic_name +  "\":\n")
            new_lines.append("            protobuf_deserializer = ProtobufDeserializer(" + start_class_full_name + ")\n")
            new_lines.append("\n")
        new_lines.append(line)

    proto_file = open(new_file_name, "w")
    n = proto_file.writelines(new_lines)
    proto_file.close()

    print("New file generated.")



