# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_onm.proto

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
  name='start_onm.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x0fstart_onm.proto\x12\rharmonyServer\"&\n\rStartONMModel\x12\x15\n\rexperiment_id\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTONMMODEL = _descriptor.Descriptor(
  name='StartONMModel',
  full_name='harmonyServer.StartONMModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='harmonyServer.StartONMModel.experiment_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=34,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['StartONMModel'] = _STARTONMMODEL

StartONMModel = _reflection.GeneratedProtocolMessageType('StartONMModel', (_message.Message,), dict(
  DESCRIPTOR = _STARTONMMODEL,
  __module__ = 'start_onm_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartONMModel)
  ))
_sym_db.RegisterMessage(StartONMModel)


# @@protoc_insertion_point(module_scope)
