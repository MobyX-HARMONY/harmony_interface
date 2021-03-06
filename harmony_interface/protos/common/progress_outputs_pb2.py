# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: progress_outputs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='progress_outputs.proto',
  package='harmonyProgressOutputs',
  syntax='proto2',
  serialized_pb=_b('\n\x16progress_outputs.proto\x12\x16harmonyProgressOutputs\"\xc6\x01\n\"UpdateServerWithProgressAndOutputs\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x12\n\npercentage\x18\x02 \x02(\x05\x12R\n\x07outputs\x18\x03 \x03(\x0b\x32\x41.harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.Output\x1a$\n\x06Output\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPDATESERVERWITHPROGRESSANDOUTPUTS_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.Output.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.Output.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=249,
)

_UPDATESERVERWITHPROGRESSANDOUTPUTS = _descriptor.Descriptor(
  name='UpdateServerWithProgressAndOutputs',
  full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.percentage', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UPDATESERVERWITHPROGRESSANDOUTPUTS_OUTPUT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=249,
)

_UPDATESERVERWITHPROGRESSANDOUTPUTS_OUTPUT.containing_type = _UPDATESERVERWITHPROGRESSANDOUTPUTS
_UPDATESERVERWITHPROGRESSANDOUTPUTS.fields_by_name['outputs'].message_type = _UPDATESERVERWITHPROGRESSANDOUTPUTS_OUTPUT
DESCRIPTOR.message_types_by_name['UpdateServerWithProgressAndOutputs'] = _UPDATESERVERWITHPROGRESSANDOUTPUTS

UpdateServerWithProgressAndOutputs = _reflection.GeneratedProtocolMessageType('UpdateServerWithProgressAndOutputs', (_message.Message,), dict(

  Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
    DESCRIPTOR = _UPDATESERVERWITHPROGRESSANDOUTPUTS_OUTPUT,
    __module__ = 'progress_outputs_pb2'
    # @@protoc_insertion_point(class_scope:harmonyProgressOutputs.UpdateServerWithProgressAndOutputs.Output)
    ))
  ,
  DESCRIPTOR = _UPDATESERVERWITHPROGRESSANDOUTPUTS,
  __module__ = 'progress_outputs_pb2'
  # @@protoc_insertion_point(class_scope:harmonyProgressOutputs.UpdateServerWithProgressAndOutputs)
  ))
_sym_db.RegisterMessage(UpdateServerWithProgressAndOutputs)
_sym_db.RegisterMessage(UpdateServerWithProgressAndOutputs.Output)


# @@protoc_insertion_point(module_scope)
