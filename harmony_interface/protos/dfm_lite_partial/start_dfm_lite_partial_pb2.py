# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_dfm_lite_partial.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cstart_dfm_lite_partial.proto\x12\rharmonyServer\"\x93\x03\n\x13StartDFMLitePartial\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x39\n\x06inputs\x18\x02 \x02(\x0b\x32).harmonyServer.StartDFMLitePartial.Inputs\x12;\n\x07outputs\x18\x03 \x02(\x0b\x32*.harmonyServer.StartDFMLitePartial.Outputs\x1am\n\x06Inputs\x12\x12\n\nPopulation\x18\x01 \x02(\t\x12\x16\n\x0ePopulationRate\x18\x02 \x02(\t\x12\x11\n\tMacroZone\x18\x03 \x02(\t\x12\r\n\x05Years\x18\x04 \x02(\t\x12\x15\n\rYearsToExport\x18\x05 \x02(\t\x1a\x80\x01\n\x07Outputs\x12\x15\n\rPopResultsCsv\x18\x01 \x02(\t\x12\x12\n\nPopYearTot\x18\x02 \x02(\t\x12\x12\n\nPopDistrY0\x18\x03 \x02(\t\x12\x12\n\nPopDistrY1\x18\x04 \x02(\t\x12\x10\n\x08PupilsY0\x18\x05 \x02(\t\x12\x10\n\x08PupilsY1\x18\x06 \x02(\t')



_STARTDFMLITEPARTIAL = DESCRIPTOR.message_types_by_name['StartDFMLitePartial']
_STARTDFMLITEPARTIAL_INPUTS = _STARTDFMLITEPARTIAL.nested_types_by_name['Inputs']
_STARTDFMLITEPARTIAL_OUTPUTS = _STARTDFMLITEPARTIAL.nested_types_by_name['Outputs']
StartDFMLitePartial = _reflection.GeneratedProtocolMessageType('StartDFMLitePartial', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTDFMLITEPARTIAL_INPUTS,
    '__module__' : 'start_dfm_lite_partial_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDFMLitePartial.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTDFMLITEPARTIAL_OUTPUTS,
    '__module__' : 'start_dfm_lite_partial_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDFMLitePartial.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTDFMLITEPARTIAL,
  '__module__' : 'start_dfm_lite_partial_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartDFMLitePartial)
  })
_sym_db.RegisterMessage(StartDFMLitePartial)
_sym_db.RegisterMessage(StartDFMLitePartial.Inputs)
_sym_db.RegisterMessage(StartDFMLitePartial.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTDFMLITEPARTIAL._serialized_start=48
  _STARTDFMLITEPARTIAL._serialized_end=451
  _STARTDFMLITEPARTIAL_INPUTS._serialized_start=211
  _STARTDFMLITEPARTIAL_INPUTS._serialized_end=320
  _STARTDFMLITEPARTIAL_OUTPUTS._serialized_start=323
  _STARTDFMLITEPARTIAL_OUTPUTS._serialized_end=451
# @@protoc_insertion_point(module_scope)
