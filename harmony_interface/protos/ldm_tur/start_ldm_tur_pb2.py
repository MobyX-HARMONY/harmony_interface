# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_ldm_tur.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13start_ldm_tur.proto\x12\rharmonyServer\"\x83\x08\n\x0bStartLdmTur\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x31\n\x06inputs\x18\x02 \x02(\x0b\x32!.harmonyServer.StartLdmTur.Inputs\x12\x33\n\x07outputs\x18\x03 \x02(\x0b\x32\".harmonyServer.StartLdmTur.Outputs\x1a\xae\x05\n\x06Inputs\x12\x10\n\x08TurinFUA\x18\x01 \x02(\t\x12\x16\n\x0e\x42\x44TRErailcover\x18\x02 \x02(\t\x12\x16\n\x0e\x42\x44TREroadcover\x18\x03 \x02(\t\x12\x17\n\x0f\x42\x44TREwatercover\x18\x04 \x02(\t\x12\x10\n\x08\x44\x45Mslope\x18\x05 \x02(\t\x12\x16\n\x0eJobAccessCar19\x18\x06 \x02(\t\x12\x16\n\x0eJobAccessBus19\x18\x07 \x02(\t\x12\x17\n\x0fJobAccessRail19\x18\x08 \x02(\t\x12\x16\n\x0eJobAccessCar30\x18\t \x02(\t\x12\x16\n\x0eJobAccessBus30\x18\n \x02(\t\x12\x17\n\x0fJobAccessRail30\x18\x0b \x02(\t\x12\x1a\n\x12HousingAccessCar19\x18\x0c \x02(\t\x12\x1a\n\x12HousingAccessBus19\x18\r \x02(\t\x12\x1b\n\x13HousingAccessRail19\x18\x0e \x02(\t\x12\x1a\n\x12HousingAccessCar30\x18\x0f \x02(\t\x12\x1a\n\x12HousingAccessBus30\x18\x10 \x02(\t\x12\x1b\n\x13HousingAccessRail30\x18\x11 \x02(\t\x12\x14\n\x0cPAIfloodzone\x18\x12 \x02(\t\x12\x1b\n\x13PPRconservationarea\x18\x13 \x02(\t\x12\x16\n\x0ePTCforestcover\x18\x14 \x02(\t\x12\x11\n\tPTCunesco\x18\x15 \x02(\t\x12\x15\n\rPTCurbangreen\x18\x16 \x02(\t\x12\x13\n\x0bPRGcemetery\x18\x17 \x02(\t\x12\x14\n\x0cPRGeducation\x18\x18 \x02(\t\x12\x15\n\rPRGhealthcare\x18\x19 \x02(\t\x12\x13\n\x0bPRGindustry\x18\x1a \x02(\t\x12\x1a\n\x12PRGparksandgardens\x18\x1b \x02(\t\x12\x13\n\x0bTurLutiGpkg\x18\x1c \x02(\t\x1a\xc6\x01\n\x07Outputs\x12\x11\n\tScenario1\x18\x01 \x02(\t\x12\x11\n\tScenario2\x18\x02 \x02(\t\x12\x11\n\tScenario3\x18\x03 \x02(\t\x12\x11\n\tScenario4\x18\x04 \x02(\t\x12\x11\n\tScenario5\x18\x05 \x02(\t\x12\x11\n\tScenario6\x18\x06 \x02(\t\x12\x11\n\tScenario7\x18\x07 \x02(\t\x12\x11\n\tScenario8\x18\x08 \x02(\t\x12\x11\n\tScenario9\x18\t \x02(\t\x12\x10\n\x08\x44iff1930\x18\n \x02(\t')



_STARTLDMTUR = DESCRIPTOR.message_types_by_name['StartLdmTur']
_STARTLDMTUR_INPUTS = _STARTLDMTUR.nested_types_by_name['Inputs']
_STARTLDMTUR_OUTPUTS = _STARTLDMTUR.nested_types_by_name['Outputs']
StartLdmTur = _reflection.GeneratedProtocolMessageType('StartLdmTur', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLDMTUR_INPUTS,
    '__module__' : 'start_ldm_tur_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLdmTur.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLDMTUR_OUTPUTS,
    '__module__' : 'start_ldm_tur_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLdmTur.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTLDMTUR,
  '__module__' : 'start_ldm_tur_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartLdmTur)
  })
_sym_db.RegisterMessage(StartLdmTur)
_sym_db.RegisterMessage(StartLdmTur.Inputs)
_sym_db.RegisterMessage(StartLdmTur.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTLDMTUR._serialized_start=39
  _STARTLDMTUR._serialized_end=1066
  _STARTLDMTUR_INPUTS._serialized_start=179
  _STARTLDMTUR_INPUTS._serialized_end=865
  _STARTLDMTUR_OUTPUTS._serialized_start=868
  _STARTLDMTUR_OUTPUTS._serialized_end=1066
# @@protoc_insertion_point(module_scope)
