# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_demo.proto

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
  name='start_demo.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x10start_demo.proto\x12\rharmonyServer\"\xb3\x02\n\x12StartDemoComponent\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x11\n\ttestValue\x18\x02 \x02(\t\x12\x38\n\x06inputs\x18\x03 \x02(\x0b\x32(.harmonyServer.StartDemoComponent.Inputs\x12:\n\x07outputs\x18\x04 \x02(\x0b\x32).harmonyServer.StartDemoComponent.Outputs\x1a\x61\n\x06Inputs\x12\r\n\x05title\x18\x01 \x02(\t\x12\x12\n\nmultiplier\x18\x02 \x02(\x05\x12\r\n\x05\x63ount\x18\x03 \x02(\t\x12\x11\n\tfirstFile\x18\x04 \x02(\t\x12\x12\n\nsecondFile\x18\x05 \x02(\t\x1a\x1d\n\x07Outputs\x12\x12\n\noutputFile\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTDEMOCOMPONENT_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='harmonyServer.StartDemoComponent.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='harmonyServer.StartDemoComponent.Inputs.title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='harmonyServer.StartDemoComponent.Inputs.multiplier', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='harmonyServer.StartDemoComponent.Inputs.count', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firstFile', full_name='harmonyServer.StartDemoComponent.Inputs.firstFile', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondFile', full_name='harmonyServer.StartDemoComponent.Inputs.secondFile', index=4,
      number=5, type=9, cpp_type=9, label=2,
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
  serialized_start=215,
  serialized_end=312,
)

_STARTDEMOCOMPONENT_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='harmonyServer.StartDemoComponent.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputFile', full_name='harmonyServer.StartDemoComponent.Outputs.outputFile', index=0,
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
  serialized_start=314,
  serialized_end=343,
)

_STARTDEMOCOMPONENT = _descriptor.Descriptor(
  name='StartDemoComponent',
  full_name='harmonyServer.StartDemoComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyServer.StartDemoComponent.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testValue', full_name='harmonyServer.StartDemoComponent.testValue', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='harmonyServer.StartDemoComponent.inputs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyServer.StartDemoComponent.outputs', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTDEMOCOMPONENT_INPUTS, _STARTDEMOCOMPONENT_OUTPUTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=343,
)

_STARTDEMOCOMPONENT_INPUTS.containing_type = _STARTDEMOCOMPONENT
_STARTDEMOCOMPONENT_OUTPUTS.containing_type = _STARTDEMOCOMPONENT
_STARTDEMOCOMPONENT.fields_by_name['inputs'].message_type = _STARTDEMOCOMPONENT_INPUTS
_STARTDEMOCOMPONENT.fields_by_name['outputs'].message_type = _STARTDEMOCOMPONENT_OUTPUTS
DESCRIPTOR.message_types_by_name['StartDemoComponent'] = _STARTDEMOCOMPONENT

StartDemoComponent = _reflection.GeneratedProtocolMessageType('StartDemoComponent', (_message.Message,), dict(

  Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOCOMPONENT_INPUTS,
    __module__ = 'start_demo_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoComponent.Inputs)
    ))
  ,

  Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOCOMPONENT_OUTPUTS,
    __module__ = 'start_demo_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoComponent.Outputs)
    ))
  ,
  DESCRIPTOR = _STARTDEMOCOMPONENT,
  __module__ = 'start_demo_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoComponent)
  ))
_sym_db.RegisterMessage(StartDemoComponent)
_sym_db.RegisterMessage(StartDemoComponent.Inputs)
_sym_db.RegisterMessage(StartDemoComponent.Outputs)


# @@protoc_insertion_point(module_scope)
