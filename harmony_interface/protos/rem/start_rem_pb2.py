# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_rem.proto

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
  name='start_rem.proto',
  package='harmonyServer',
  syntax='proto2',
  serialized_pb=_b('\n\x0fstart_rem.proto\x12\rharmonyServer\"\x83\x04\n\x08StartREM\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12.\n\x06inputs\x18\x02 \x02(\x0b\x32\x1e.harmonyServer.StartREM.Inputs\x12\x30\n\x07outputs\x18\x03 \x02(\x0b\x32\x1f.harmonyServer.StartREM.Outputs\x1a\xf0\x01\n\x06Inputs\x12\x10\n\x08\x42\x61seJobs\x18\x01 \x02(\t\x12\x11\n\tbetaCoeff\x18\x02 \x02(\t\x12\x0f\n\x07MacroEc\x18\x03 \x02(\t\x12\x0f\n\x07MicroEc\x18\x04 \x02(\t\x12\x0b\n\x03Pop\x18\x05 \x02(\t\x12\x11\n\tTechCoeff\x18\x06 \x02(\t\x12\x12\n\nTrendsCnst\x18\x07 \x02(\t\x12\x11\n\tTrendsPar\x18\x08 \x02(\t\x12\x1d\n\x15YearlyJobsGroundTruth\x18\t \x02(\t\x12\x18\n\x10zoneDistribution\x18\n \x02(\t\x12\x0e\n\x06Income\x18\x0b \x02(\t\x12\x0f\n\x07yearOut\x18\x0c \x02(\t\x1a\x8d\x01\n\x07Outputs\x12\x1b\n\x13\x62\x65taCoeffCalibrated\x18\x01 \x02(\t\x12\x12\n\nYearlyJobs\x18\x02 \x02(\t\x12\x17\n\x0fYearlyJobs_xlsx\x18\x03 \x02(\t\x12\x16\n\x0eYearlyJobsZone\x18\x04 \x02(\t\x12 \n\x18YearlyJobsZoneAggregated\x18\x05 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTREM_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='harmonyServer.StartREM.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='BaseJobs', full_name='harmonyServer.StartREM.Inputs.BaseJobs', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='betaCoeff', full_name='harmonyServer.StartREM.Inputs.betaCoeff', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MacroEc', full_name='harmonyServer.StartREM.Inputs.MacroEc', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MicroEc', full_name='harmonyServer.StartREM.Inputs.MicroEc', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pop', full_name='harmonyServer.StartREM.Inputs.Pop', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TechCoeff', full_name='harmonyServer.StartREM.Inputs.TechCoeff', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TrendsCnst', full_name='harmonyServer.StartREM.Inputs.TrendsCnst', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TrendsPar', full_name='harmonyServer.StartREM.Inputs.TrendsPar', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YearlyJobsGroundTruth', full_name='harmonyServer.StartREM.Inputs.YearlyJobsGroundTruth', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zoneDistribution', full_name='harmonyServer.StartREM.Inputs.zoneDistribution', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Income', full_name='harmonyServer.StartREM.Inputs.Income', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yearOut', full_name='harmonyServer.StartREM.Inputs.yearOut', index=11,
      number=12, type=9, cpp_type=9, label=2,
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
  serialized_start=166,
  serialized_end=406,
)

_STARTREM_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='harmonyServer.StartREM.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='betaCoeffCalibrated', full_name='harmonyServer.StartREM.Outputs.betaCoeffCalibrated', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YearlyJobs', full_name='harmonyServer.StartREM.Outputs.YearlyJobs', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YearlyJobs_xlsx', full_name='harmonyServer.StartREM.Outputs.YearlyJobs_xlsx', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YearlyJobsZone', full_name='harmonyServer.StartREM.Outputs.YearlyJobsZone', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YearlyJobsZoneAggregated', full_name='harmonyServer.StartREM.Outputs.YearlyJobsZoneAggregated', index=4,
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
  serialized_start=409,
  serialized_end=550,
)

_STARTREM = _descriptor.Descriptor(
  name='StartREM',
  full_name='harmonyServer.StartREM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenarioId', full_name='harmonyServer.StartREM.scenarioId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='harmonyServer.StartREM.inputs', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='harmonyServer.StartREM.outputs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTREM_INPUTS, _STARTREM_OUTPUTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=550,
)

_STARTREM_INPUTS.containing_type = _STARTREM
_STARTREM_OUTPUTS.containing_type = _STARTREM
_STARTREM.fields_by_name['inputs'].message_type = _STARTREM_INPUTS
_STARTREM.fields_by_name['outputs'].message_type = _STARTREM_OUTPUTS
DESCRIPTOR.message_types_by_name['StartREM'] = _STARTREM

StartREM = _reflection.GeneratedProtocolMessageType('StartREM', (_message.Message,), dict(

  Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTREM_INPUTS,
    __module__ = 'start_rem_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartREM.Inputs)
    ))
  ,

  Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
    DESCRIPTOR = _STARTREM_OUTPUTS,
    __module__ = 'start_rem_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartREM.Outputs)
    ))
  ,
  DESCRIPTOR = _STARTREM,
  __module__ = 'start_rem_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartREM)
  ))
_sym_db.RegisterMessage(StartREM)
_sym_db.RegisterMessage(StartREM.Inputs)
_sym_db.RegisterMessage(StartREM.Outputs)


# @@protoc_insertion_point(module_scope)
