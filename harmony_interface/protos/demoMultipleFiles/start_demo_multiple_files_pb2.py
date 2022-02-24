# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_demo_multiple_files.proto

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
  name='start_demo_multiple_files.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x1fstart_demo_multiple_files.proto\x12\rharmonyServer\"\xc7\x03\n\x1fStartDemoMultipleFilesComponent\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x45\n\x06inputs\x18\x02 \x02(\x0b\x32\x35.harmonyServer.StartDemoMultipleFilesComponent.Inputs\x12G\n\x07outputs\x18\x03 \x02(\x0b\x32\x36.harmonyServer.StartDemoMultipleFilesComponent.Outputs\x1a\xa2\x01\n\x06Inputs\x12\x13\n\x0bstringInput\x18\x01 \x02(\t\x12\x14\n\x0cnumericInput\x18\x02 \x02(\x05\x12\x19\n\x11\x64\x65moBaseInputFile\x18\x03 \x02(\t\x12\x13\n\x0bnumber1File\x18\x04 \x02(\t\x12\x13\n\x0bnumber2File\x18\x05 \x02(\t\x12\x13\n\x0bnumber3File\x18\x06 \x02(\t\x12\x13\n\x0bnumber4File\x18\x07 \x02(\t\x1a[\n\x07Outputs\x12\x1a\n\x12\x64\x65moBaseOutputFile\x18\x01 \x02(\t\x12\x19\n\x11\x64\x65moOutputNumber1\x18\x02 \x02(\t\x12\x19\n\x11\x64\x65moOutputNumber2\x18\x03 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTDEMOMULTIPLEFILESCOMPONENT_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringInput', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.stringInput', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numericInput', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.numericInput', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoBaseInputFile', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.demoBaseInputFile', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number1File', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.number1File', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number2File', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.number2File', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number3File', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.number3File', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number4File', full_name='harmonyServer.StartDemoMultipleFilesComponent.Inputs.number4File', index=6,
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
  serialized_start=251,
  serialized_end=413,
)

_STARTDEMOMULTIPLEFILESCOMPONENT_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='harmonyServer.StartDemoMultipleFilesComponent.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='demoBaseOutputFile', full_name='harmonyServer.StartDemoMultipleFilesComponent.Outputs.demoBaseOutputFile', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoOutputNumber1', full_name='harmonyServer.StartDemoMultipleFilesComponent.Outputs.demoOutputNumber1', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demoOutputNumber2', full_name='harmonyServer.StartDemoMultipleFilesComponent.Outputs.demoOutputNumber2', index=2,
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
  serialized_start=415,
  serialized_end=506,
)

_STARTDEMOMULTIPLEFILESCOMPONENT = _descriptor.Descriptor(
  name='StartDemoMultipleFilesComponent',
  full_name='harmonyServer.StartDemoMultipleFilesComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyServer.StartDemoMultipleFilesComponent.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='harmonyServer.StartDemoMultipleFilesComponent.inputs', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyServer.StartDemoMultipleFilesComponent.outputs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTDEMOMULTIPLEFILESCOMPONENT_INPUTS, _STARTDEMOMULTIPLEFILESCOMPONENT_OUTPUTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=506,
)

_STARTDEMOMULTIPLEFILESCOMPONENT_INPUTS.containing_type = _STARTDEMOMULTIPLEFILESCOMPONENT
_STARTDEMOMULTIPLEFILESCOMPONENT_OUTPUTS.containing_type = _STARTDEMOMULTIPLEFILESCOMPONENT
_STARTDEMOMULTIPLEFILESCOMPONENT.fields_by_name['inputs'].message_type = _STARTDEMOMULTIPLEFILESCOMPONENT_INPUTS
_STARTDEMOMULTIPLEFILESCOMPONENT.fields_by_name['outputs'].message_type = _STARTDEMOMULTIPLEFILESCOMPONENT_OUTPUTS
DESCRIPTOR.message_types_by_name['StartDemoMultipleFilesComponent'] = _STARTDEMOMULTIPLEFILESCOMPONENT

StartDemoMultipleFilesComponent = _reflection.GeneratedProtocolMessageType('StartDemoMultipleFilesComponent', (_message.Message,), dict(

  Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT_INPUTS,
    __module__ = 'start_demo_multiple_files_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent.Inputs)
    ))
  ,

  Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT_OUTPUTS,
    __module__ = 'start_demo_multiple_files_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent.Outputs)
    ))
  ,
  DESCRIPTOR = _STARTDEMOMULTIPLEFILESCOMPONENT,
  __module__ = 'start_demo_multiple_files_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartDemoMultipleFilesComponent)
  ))
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent)
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent.Inputs)
_sym_db.RegisterMessage(StartDemoMultipleFilesComponent.Outputs)


# @@protoc_insertion_point(module_scope)
