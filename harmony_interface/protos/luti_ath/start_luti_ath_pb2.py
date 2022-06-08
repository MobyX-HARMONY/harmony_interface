# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_luti_ath.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14start_luti_ath.proto\x12\rharmonyServer\"\xd3\x0e\n\x0cStartLutiAth\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x32\n\x06inputs\x18\x02 \x02(\x0b\x32\".harmonyServer.StartLutiAth.Inputs\x12\x34\n\x07outputs\x18\x03 \x02(\x0b\x32#.harmonyServer.StartLutiAth.Outputs\x1a\xb0\x02\n\x06Inputs\x12\x15\n\rZoneCodesFile\x18\x01 \x02(\t\x12\x17\n\x0fZoneCoordinates\x18\x02 \x02(\t\x12\x15\n\rIntrazoneDist\x18\x03 \x02(\t\x12\x1d\n\x15\x43ijPrivateMinFilename\x18\x04 \x02(\t\x12\x1c\n\x14\x43ijPublicMinFilename\x18\x05 \x02(\t\x12\x1a\n\x12\x44\x61taEmployment2019\x18\x06 \x02(\t\x12\x1a\n\x12\x44\x61taEmployment2030\x18\x07 \x02(\t\x12\x1a\n\x12\x44\x61taEmployment2045\x18\x08 \x02(\t\x12\x18\n\x10HhFloorspace2019\x18\t \x02(\t\x12\x18\n\x10HhFloorspace2045\x18\n \x02(\t\x12\x1a\n\x12\x44\x61taZonesShapefile\x18\x0b \x02(\t\x1a\x91\x0b\n\x07Outputs\x12\x1d\n\x15JobsAccessibility2019\x18\x01 \x02(\t\x12\x1d\n\x15JobsAccessibility2030\x18\x02 \x02(\t\x12\x1d\n\x15JobsAccessibility2045\x18\x03 \x02(\t\x12 \n\x18HousingAccessibility2019\x18\x04 \x02(\t\x12 \n\x18HousingAccessibility2030\x18\x05 \x02(\t\x12 \n\x18HousingAccessibility2045\x18\x06 \x02(\t\x12\x10\n\x08\x45jOi2019\x18\x07 \x02(\t\x12\x10\n\x08\x45jOi2030\x18\x08 \x02(\t\x12\x10\n\x08\x45jOi2045\x18\t \x02(\t\x12\x1d\n\x15JobsProbTijPublic2019\x18\n \x02(\t\x12\x1e\n\x16JobsProbTijPrivate2019\x18\x0b \x02(\t\x12\x1d\n\x15JobsProbTijPublic2030\x18\x0c \x02(\t\x12\x1e\n\x16JobsProbTijPrivate2030\x18\r \x02(\t\x12\x1d\n\x15JobsProbTijPublic2045\x18\x0e \x02(\t\x12\x1e\n\x16JobsProbTijPrivate2045\x18\x0f \x02(\t\x12\x19\n\x11JobsTijPublic2019\x18\x10 \x02(\t\x12\x1a\n\x12JobsTijPrivate2019\x18\x11 \x02(\t\x12\x19\n\x11JobsTijPublic2030\x18\x12 \x02(\t\x12\x1a\n\x12JobsTijPrivate2030\x18\x13 \x02(\t\x12\x19\n\x11JobsTijPublic2045\x18\x14 \x02(\t\x12\x1a\n\x12JobsTijPrivate2045\x18\x15 \x02(\t\x12\x1d\n\x15\x41rrowsFlowsPublic2019\x18\x16 \x02(\t\x12\x1e\n\x16\x41rrowsFlowsPrivate2019\x18\x17 \x02(\t\x12\x1d\n\x15\x41rrowsFlowsPublic2030\x18\x18 \x02(\t\x12\x1e\n\x16\x41rrowsFlowsPrivate2030\x18\x19 \x02(\t\x12\x1d\n\x15\x41rrowsFlowsPublic2045\x18\x1a \x02(\t\x12\x1e\n\x16\x41rrowsFlowsPrivate2045\x18\x1b \x02(\t\x12\x1c\n\x14MapPopChange20192030\x18\x1c \x02(\t\x12\x1c\n\x14MapPopChange20302045\x18\x1d \x02(\t\x12\x1c\n\x14MapPopChange20192045\x18\x1e \x02(\t\x12)\n!MapHousingAccChange20192030Public\x18\x1f \x02(\t\x12*\n\"MapHousingAccChange20192030Private\x18  \x02(\t\x12)\n!MapHousingAccChange20192045Public\x18! \x02(\t\x12*\n\"MapHousingAccChange20192045Private\x18\" \x02(\t\x12)\n!MapHousingAccChange20302045Public\x18# \x02(\t\x12+\n#MapHousingAccChange201302045Private\x18$ \x02(\t\x12&\n\x1eMapJobsAccChange20192030Public\x18% \x02(\t\x12\'\n\x1fMapJobsAccChange20192030Private\x18& \x02(\t\x12&\n\x1eMapJobsAccChange20192045Public\x18\' \x02(\t\x12\'\n\x1fMapJobsAccChange20192045Private\x18( \x02(\t\x12&\n\x1eMapJobsAccChange20302045Public\x18) \x02(\t\x12\'\n\x1fMapJobsAccChange20302045Private\x18* \x02(\t\x12\x1b\n\x13MapResultsShapefile\x18+ \x02(\t')



_STARTLUTIATH = DESCRIPTOR.message_types_by_name['StartLutiAth']
_STARTLUTIATH_INPUTS = _STARTLUTIATH.nested_types_by_name['Inputs']
_STARTLUTIATH_OUTPUTS = _STARTLUTIATH.nested_types_by_name['Outputs']
StartLutiAth = _reflection.GeneratedProtocolMessageType('StartLutiAth', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLUTIATH_INPUTS,
    '__module__' : 'start_luti_ath_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiAth.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLUTIATH_OUTPUTS,
    '__module__' : 'start_luti_ath_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiAth.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTLUTIATH,
  '__module__' : 'start_luti_ath_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiAth)
  })
_sym_db.RegisterMessage(StartLutiAth)
_sym_db.RegisterMessage(StartLutiAth.Inputs)
_sym_db.RegisterMessage(StartLutiAth.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTLUTIATH._serialized_start=40
  _STARTLUTIATH._serialized_end=1915
  _STARTLUTIATH_INPUTS._serialized_start=183
  _STARTLUTIATH_INPUTS._serialized_end=487
  _STARTLUTIATH_OUTPUTS._serialized_start=490
  _STARTLUTIATH_OUTPUTS._serialized_end=1915
# @@protoc_insertion_point(module_scope)