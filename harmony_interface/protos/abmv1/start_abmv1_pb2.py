# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_abmv1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11start_abmv1.proto\x12\rharmonyServer\"\xd7\x02\n\nStartAbmv1\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x30\n\x06inputs\x18\x02 \x02(\x0b\x32 .harmonyServer.StartAbmv1.Inputs\x12\x32\n\x07outputs\x18\x03 \x02(\x0b\x32!.harmonyServer.StartAbmv1.Outputs\x1as\n\x06Inputs\x12\"\n\x1aworkFirstTimediffThreshold\x18\x01 \x02(\t\x12\x15\n\rCleanTripsTUR\x18\x02 \x02(\t\x12.\n&TURPersonSyntheticFinal1ActivitiesWork\x18\x03 \x02(\t\x1aZ\n\x07Outputs\x12+\n#syntheticTURSecondaryStartTimesInt2\x18\x01 \x02(\t\x12\"\n\x1asyntheticTURFordestpredict\x18\x02 \x02(\t')



_STARTABMV1 = DESCRIPTOR.message_types_by_name['StartAbmv1']
_STARTABMV1_INPUTS = _STARTABMV1.nested_types_by_name['Inputs']
_STARTABMV1_OUTPUTS = _STARTABMV1.nested_types_by_name['Outputs']
StartAbmv1 = _reflection.GeneratedProtocolMessageType('StartAbmv1', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTABMV1_INPUTS,
    '__module__' : 'start_abmv1_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartAbmv1.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTABMV1_OUTPUTS,
    '__module__' : 'start_abmv1_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartAbmv1.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTABMV1,
  '__module__' : 'start_abmv1_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartAbmv1)
  })
_sym_db.RegisterMessage(StartAbmv1)
_sym_db.RegisterMessage(StartAbmv1.Inputs)
_sym_db.RegisterMessage(StartAbmv1.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTABMV1._serialized_start=37
  _STARTABMV1._serialized_end=380
  _STARTABMV1_INPUTS._serialized_start=173
  _STARTABMV1_INPUTS._serialized_end=288
  _STARTABMV1_OUTPUTS._serialized_start=290
  _STARTABMV1_OUTPUTS._serialized_end=380
# @@protoc_insertion_point(module_scope)
