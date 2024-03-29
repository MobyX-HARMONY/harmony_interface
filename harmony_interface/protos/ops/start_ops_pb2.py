# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_ops.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fstart_ops.proto\x12\rharmonyServer\"\xee\x01\n\x08StartOps\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12.\n\x06inputs\x18\x02 \x02(\x0b\x32\x1e.harmonyServer.StartOps.Inputs\x12\x30\n\x07outputs\x18\x03 \x02(\x0b\x32\x1f.harmonyServer.StartOps.Outputs\x1a.\n\x06Inputs\x12\x15\n\rVehicleNumber\x18\x01 \x02(\x05\x12\r\n\x05Trips\x18\x02 \x02(\t\x1a<\n\x07Outputs\x12\x1e\n\x16\x41verageRoadSectionData\x18\x01 \x02(\t\x12\x11\n\tEmissions\x18\x02 \x02(\t')



_STARTOPS = DESCRIPTOR.message_types_by_name['StartOps']
_STARTOPS_INPUTS = _STARTOPS.nested_types_by_name['Inputs']
_STARTOPS_OUTPUTS = _STARTOPS.nested_types_by_name['Outputs']
StartOps = _reflection.GeneratedProtocolMessageType('StartOps', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTOPS_INPUTS,
    '__module__' : 'start_ops_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartOps.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTOPS_OUTPUTS,
    '__module__' : 'start_ops_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartOps.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTOPS,
  '__module__' : 'start_ops_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartOps)
  })
_sym_db.RegisterMessage(StartOps)
_sym_db.RegisterMessage(StartOps.Inputs)
_sym_db.RegisterMessage(StartOps.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTOPS._serialized_start=35
  _STARTOPS._serialized_end=273
  _STARTOPS_INPUTS._serialized_start=165
  _STARTOPS_INPUTS._serialized_end=211
  _STARTOPS_OUTPUTS._serialized_start=213
  _STARTOPS_OUTPUTS._serialized_end=273
# @@protoc_insertion_point(module_scope)
