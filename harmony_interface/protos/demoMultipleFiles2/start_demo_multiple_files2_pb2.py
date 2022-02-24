# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_demo_multiple_files2.proto

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
  name='start_demo_multiple_files2.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n start_demo_multiple_files2.proto\x12\rharmonyServer\"\xca\x03\n StartDemoMultipleFilesComponent2\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x46\n\x06inputs\x18\x02 \x02(\x0b\x32\x36.harmonyServer.StartDemoMultipleFilesComponent2.Inputs\x12H\n\x07outputs\x18\x03 \x02(\x0b\x32\x37.harmonyServer.StartDemoMultipleFilesComponent2.Outputs\x1a\xa2\x01\n\x06Inputs\x12\x13\n\x0bstringInput\x18\x01 \x02(\t\x12\x14\n\x0cnumericInput\x18\x02 \x02(\x05\x12\x19\n\x11\x64\x65moBaseInputFile\x18\x03 \x02(\t\x12\x13\n\x0bnumber1File\x18\x04 \x02(\t\x12\x13\n\x0bnumber2File\x18\x05 \x02(\t\x12\x13\n\x0bnumber3File\x18\x06 \x02(\t\x12\x13\n\x0bnumber4File\x18\x07 \x02(\t\x1a[\n\x07Outputs\x12\x1a\n\x12\x64\x65moBaseOutputFile\x18\x01 \x02(\t\x12\x19\n\x11\x64\x65moOutputNumber1\x18\x02 \x02(\t\x12\x19\n\x11\x64\x65moOutputNumber2\x18\x03 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTDEMOMULTIPLEFILESCOMPONENT2_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringInput', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.stringInput', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numericInput', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.numericInput', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoBaseInputFile', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.demoBaseInputFile', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number1File', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.number1File', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number2File', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.number2File', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number3File', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.number3File', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number4File', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Inputs.number4File', index=6,
      number=7, type=9, cpp_type=9, label=2,
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
  serialized_start=255,
  serialized_end=417,
)

_STARTDEMOMULTIPLEFILESCOMPONENT2_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='harmonyServer.StartDemoMultipleFilesComponent2.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='demoBaseOutputFile', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Outputs.demoBaseOutputFile', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoOutputNumber1', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Outputs.demoOutputNumber1', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoOutputNumber2', full_name='harmonyServer.StartDemoMultipleFilesComponent2.Outputs.demoOutputNumber2', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=419,
  serialized_end=510,
)

_STARTDEMOMULTIPLEFILESCOMPONENT2 = _descriptor.Descriptor(
  name='StartDemoMultipleFilesComponent2',
  full_name='harmonyServer.StartDemoMultipleFilesComponent2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyServer.StartDemoMultipleFilesComponent2.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='harmonyServer.StartDemoMultipleFilesComponent2.inputs', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyServer.StartDemoMultipleFilesComponent2.outputs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTDEMOMULTIPLEFILESCOMPONENT2_INPUTS, _STARTDEMOMULTIPLEFILESCOMPONENT2_OUTPUTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=510,
)

_STARTDEMOMULTIPLEFILESCOMPONENT2_INPUTS.containing_type = _STARTDEMOMULTIPLEFILESCOMPONENT2
_STARTDEMOMULTIPLEFILESCOMPONENT2_OUTPUTS.containing_type = _STARTDEMOMULTIPLEFILESCOMPONENT2
_STARTDEMOMULTIPLEFILESCOMPONENT2.fields_by_name['inputs'].message_type = _STARTDEMOMULTIPLEFILESCOMPONENT2_INPUTS
_STARTDEMOMULTIPLEFILESCOMPONENT2.fields_by_name['outputs'].message_type = _STARTDEMOMULTIPLEFILESCOMPONENT2_OUTPUTS
DESCRIPTOR.message_types_by_name['StartDemoMultipleFilesComponent2'] = _STARTDEMOMULTIPLEFILESCOMPONENT2

StartDemoMultipleFilesComponent2 = _reflection.GeneratedProtocolMessageType('StartDemoMultipleFilesComponent2', (_message.Message,), dict(

  Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT2_INPUTS,
    __module__ = 'start_demo_multiple_files2_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent2.Inputs)
    ))
  ,

  Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT2_OUTPUTS,
    __module__ = 'start_demo_multiple_files2_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent2.Outputs)
    ))
  ,
  DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT2,
  __module__ = 'start_demo_multiple_files2_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent2)
  ))
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent2)
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent2.Inputs)
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent2.Outputs)


# @@protoc_insertion_point(module_scope)
