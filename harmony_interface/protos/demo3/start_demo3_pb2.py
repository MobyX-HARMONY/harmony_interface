# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_demo3.proto

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
  name='start_demo3.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x11start_demo3.proto\x12\rharmonyServer\"\x9f\x02\n\x13StartDemo3Component\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x39\n\x06inputs\x18\x02 \x02(\x0b\x32).harmonyServer.StartDemo3Component.Inputs\x12;\n\x07outputs\x18\x03 \x02(\x0b\x32*.harmonyServer.StartDemo3Component.Outputs\x1a[\n\x06Inputs\x12\x13\n\x0bstringInput\x18\x01 \x02(\t\x12\x14\n\x0cnumericInput\x18\x02 \x02(\x05\x12\x12\n\ndemo3File1\x18\x03 \x02(\t\x12\x12\n\ndemo3File2\x18\x04 \x02(\t\x1a\x1f\n\x07Outputs\x12\x14\n\x0c\x64\x65mo3Output1\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTDEMO3COMPONENT_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='harmonyServer.StartDemo3Component.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringInput', full_name='harmonyServer.StartDemo3Component.Inputs.stringInput', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numericInput', full_name='harmonyServer.StartDemo3Component.Inputs.numericInput', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demo3File1', full_name='harmonyServer.StartDemo3Component.Inputs.demo3File1', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demo3File2', full_name='harmonyServer.StartDemo3Component.Inputs.demo3File2', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  serialized_start=200,
  serialized_end=291,
)

_STARTDEMO3COMPONENT_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='harmonyServer.StartDemo3Component.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='demo3Output1', full_name='harmonyServer.StartDemo3Component.Outputs.demo3Output1', index=0,
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
  serialized_start=293,
  serialized_end=324,
)

_STARTDEMO3COMPONENT = _descriptor.Descriptor(
  name='StartDemo3Component',
  full_name='harmonyServer.StartDemo3Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyServer.StartDemo3Component.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='harmonyServer.StartDemo3Component.inputs', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyServer.StartDemo3Component.outputs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTDEMO3COMPONENT_INPUTS, _STARTDEMO3COMPONENT_OUTPUTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=324,
)

_STARTDEMO3COMPONENT_INPUTS.containing_type = _STARTDEMO3COMPONENT
_STARTDEMO3COMPONENT_OUTPUTS.containing_type = _STARTDEMO3COMPONENT
_STARTDEMO3COMPONENT.fields_by_name['inputs'].message_type = _STARTDEMO3COMPONENT_INPUTS
_STARTDEMO3COMPONENT.fields_by_name['outputs'].message_type = _STARTDEMO3COMPONENT_OUTPUTS
DESCRIPTOR.message_types_by_name['StartDemo3Component'] = _STARTDEMO3COMPONENT

StartDemo3Component = _reflection.GeneratedProtocolMessageType('StartDemo3Component', (_message.Message,), dict(

  Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMO3COMPONENT_INPUTS,
    __module__ = 'start_demo3_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemo3Component.Inputs)
    ))
  ,

  Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMO3COMPONENT_OUTPUTS,
    __module__ = 'start_demo3_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemo3Component.Outputs)
    ))
  ,
  DESCRIPTOR = _STARTDEMO3COMPONENT,
  __module__ = 'start_demo3_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartDemo3Component)
  ))
_sym_db.RegisterMessage(StartDemo3Component)
_sym_db.RegisterMessage(StartDemo3Component.Inputs)
_sym_db.RegisterMessage(StartDemo3Component.Outputs)


# @@protoc_insertion_point(module_scope)
