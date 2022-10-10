# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_luti_oxf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14start_luti_oxf.proto\x12\rharmonyServer\"\x95\x1b\n\x0cStartLutiOxf\x12\x12\n\nscenarioId\x18\x01 \x02(\t\x12\x32\n\x06inputs\x18\x02 \x02(\x0b\x32\".harmonyServer.StartLutiOxf.Inputs\x12\x34\n\x07outputs\x18\x03 \x02(\x0b\x32#.harmonyServer.StartLutiOxf.Outputs\x1a\xbe\x05\n\x06Inputs\x12\"\n\x1a\x44\x61taOpenGeolytixRegression\x18\x01 \x02(\t\x12\x17\n\x0f\x44\x61taCensusQS103\x18\x02 \x02(\t\x12\x19\n\x11\x44\x61taCensusQS103SC\x18\x03 \x02(\t\x12\x1c\n\x14LookupDZ2001toIZ2001\x18\x04 \x02(\t\x12\x13\n\x0bOxfMsoaFile\x18\x05 \x02(\t\x12\x1f\n\x17QUANTCijRoadMinFilename\x18\x06 \x02(\t\x12\x1e\n\x16QUANTCijBusMinFilename\x18\x07 \x02(\t\x12\x1f\n\x17QUANTCijRailMinFilename\x18\x08 \x02(\t\x12\x18\n\x10SObsRoadFilename\x18\t \x02(\t\x12\x17\n\x0fSObsBusFilename\x18\n \x02(\t\x12\x18\n\x10SObsRailFilename\x18\x0b \x02(\t\x12\x18\n\x10OXFNewHousingDev\x18\x0c \x02(\t\x12\x18\n\x10\x45mployment2011GB\x18\r \x02(\t\x12\x16\n\x0e\x45mployment2019\x18\x0e \x02(\t\x12\x16\n\x0e\x45mployment2030\x18\x0f \x02(\t\x12\x14\n\x0c\x44wellingsOxf\x18\x10 \x02(\t\x12\x18\n\x10ZonesCoordinates\x18\x11 \x02(\t\x12\x14\n\x0cOxfPostcodes\x18\x12 \x02(\t\x12\x1d\n\x15\x44\x61taSchoolsEWSPrimary\x18\x13 \x02(\t\x12 \n\x18\x44\x61taSchoolsEWSPSecondary\x18\x14 \x02(\t\x12\x15\n\rDataHospitals\x18\x15 \x02(\t\x12\x15\n\rMsoaShapefile\x18\x16 \x02(\t\x12\x1c\n\x14RoadNetworkShapefile\x18\x17 \x02(\t\x12\x1e\n\x16MSOACentroidsShapefile\x18\x18 \x02(\t\x12#\n\x1bMSOACentroidsShapefileWGS84\x18\x19 \x02(\t\x1a\xc5\x14\n\x07Outputs\x12\x1d\n\x15JobsAccessibility2019\x18\x01 \x02(\t\x12\x1d\n\x15JobsAccessibility2030\x18\x02 \x02(\t\x12 \n\x18HousingAccessibility2019\x18\x03 \x02(\t\x12 \n\x18HousingAccessibility2030\x18\x04 \x02(\t\x12\x14\n\x0cJobsDjOi2019\x18\x05 \x02(\t\x12\x14\n\x0cJobsDjOi2030\x18\x06 \x02(\t\x12\x1c\n\x14JobsProbTijRoads2019\x18\x07 \x02(\t\x12\x1a\n\x12JobsProbTijBus2019\x18\x08 \x02(\t\x12\x1b\n\x13JobsProbTijRail2019\x18\t \x02(\t\x12\x18\n\x10JobsTijRoads2019\x18\n \x02(\t\x12\x16\n\x0eJobsTijBus2019\x18\x0b \x02(\t\x12\x17\n\x0fJobsTijRail2019\x18\x0c \x02(\t\x12\x1a\n\x12\x41rrowsFlowsCar2019\x18\r \x02(\t\x12\x1a\n\x12\x41rrowsFlowsBus2019\x18\x0e \x02(\t\x12\x1b\n\x13\x41rrowsFlowsRail2019\x18\x0f \x02(\t\x12\x1c\n\x14JobsProbTijRoads2030\x18\x10 \x02(\t\x12\x1a\n\x12JobsProbTijBus2030\x18\x11 \x02(\t\x12\x1b\n\x13JobsProbTijRail2030\x18\x12 \x02(\t\x12\x18\n\x10JobsTijRoads2030\x18\x13 \x02(\t\x12\x16\n\x0eJobsTijBus2030\x18\x14 \x02(\t\x12\x17\n\x0fJobsTijRail2030\x18\x15 \x02(\t\x12\x1a\n\x12\x41rrowsFlowsCar2030\x18\x16 \x02(\t\x12\x1a\n\x12\x41rrowsFlowsBus2030\x18\x17 \x02(\t\x12\x1b\n\x13\x41rrowsFlowsRail2030\x18\x18 \x02(\t\x12\x1e\n\x16RetailProbRijRoads2019\x18\x19 \x02(\t\x12\x1c\n\x14RetailProbRijBus2019\x18\x1a \x02(\t\x12\x1d\n\x15RetailProbRijRail2019\x18\x1b \x02(\t\x12\x1a\n\x12RetailRijRoads2019\x18\x1c \x02(\t\x12\x18\n\x10RetailRijBus2019\x18\x1d \x02(\t\x12\x19\n\x11RetailRijRail2019\x18\x1e \x02(\t\x12\x1e\n\x16RetailProbRijRoads2030\x18\x1f \x02(\t\x12\x1c\n\x14RetailProbRijBus2030\x18  \x02(\t\x12\x1d\n\x15RetailProbRijRail2030\x18! \x02(\t\x12\x1a\n\x12RetailRijRoads2030\x18\" \x02(\t\x12\x18\n\x10RetailRijBus2030\x18# \x02(\t\x12\x19\n\x11RetailRijRail2030\x18$ \x02(\t\x12\x1f\n\x17PrimaryProbPijRoads2019\x18% \x02(\t\x12\x1d\n\x15PrimaryProbPijBus2019\x18& \x02(\t\x12\x1e\n\x16PrimaryProbPijRail2019\x18\' \x02(\t\x12\x1b\n\x13PrimaryPijRoads2019\x18( \x02(\t\x12\x19\n\x11PrimaryPijBus2019\x18) \x02(\t\x12\x1a\n\x12PrimaryPijRail2019\x18* \x02(\t\x12\x1f\n\x17PrimaryProbPijRoads2030\x18+ \x02(\t\x12\x1d\n\x15PrimaryProbPijBus2030\x18, \x02(\t\x12\x1e\n\x16PrimaryProbPijRail2030\x18- \x02(\t\x12\x1b\n\x13PrimaryPijRoads2030\x18. \x02(\t\x12\x19\n\x11PrimaryPijBus2030\x18/ \x02(\t\x12\x1a\n\x12PrimaryPijRail2030\x18\x30 \x02(\t\x12!\n\x19SecondaryProbPijRoads2019\x18\x31 \x02(\t\x12\x1f\n\x17SecondaryProbPijBus2019\x18\x32 \x02(\t\x12 \n\x18SecondaryProbPijRail2019\x18\x33 \x02(\t\x12\x1d\n\x15SecondaryPijRoads2019\x18\x34 \x02(\t\x12\x1b\n\x13SecondaryPijBus2019\x18\x35 \x02(\t\x12\x1c\n\x14SecondaryPijRail2019\x18\x36 \x02(\t\x12!\n\x19SecondaryProbPijRoads2030\x18\x37 \x02(\t\x12\x1f\n\x17SecondaryProbPijBus2030\x18\x38 \x02(\t\x12 \n\x18SecondaryProbPijRail2030\x18\x39 \x02(\t\x12\x1d\n\x15SecondaryPijRoads2030\x18: \x02(\t\x12\x1b\n\x13SecondaryPijBus2030\x18; \x02(\t\x12\x1c\n\x14SecondaryPijRail2030\x18< \x02(\t\x12 \n\x18HospitalProbHijRoads2019\x18= \x02(\t\x12\x1e\n\x16HospitalProbHijBus2019\x18> \x02(\t\x12\x1f\n\x17HospitalProbHijRail2019\x18? \x02(\t\x12\x1c\n\x14HospitalHijRoads2019\x18@ \x02(\t\x12\x1a\n\x12HospitalHijBus2019\x18\x41 \x02(\t\x12\x1b\n\x13HospitalHijRail2019\x18\x42 \x02(\t\x12 \n\x18HospitalProbHijRoads2030\x18\x43 \x02(\t\x12\x1e\n\x16HospitalProbHijBus2030\x18\x44 \x02(\t\x12\x1f\n\x17HospitalProbHijRail2030\x18\x45 \x02(\t\x12\x1c\n\x14HospitalHijRoads2030\x18\x46 \x02(\t\x12\x1a\n\x12HospitalHijBus2030\x18G \x02(\t\x12\x1b\n\x13HospitalHijRail2030\x18H \x02(\t\x12\x1c\n\x14MapPopChange20192030\x18I \x02(\t\x12(\n MapHousingAccChange20192030Roads\x18J \x02(\t\x12&\n\x1eMapHousingAccChange20192030Bus\x18K \x02(\t\x12\'\n\x1fMapHousingAccChange20192030Rail\x18L \x02(\t\x12%\n\x1dMapJobsAccChange20192030Roads\x18M \x02(\t\x12#\n\x1bMapJobsAccChange20192030Bus\x18N \x02(\t\x12$\n\x1cMapJobsAccChange20192030Rail\x18O \x02(\t\x12\x1b\n\x13MapResultsShapefile\x18P \x02(\t\x12\x1f\n\x17JobsTijRoads2019FlowMap\x18Q \x02(\t\x12\x1d\n\x15JobsTijBus2019FlowMap\x18R \x02(\t\x12\x1e\n\x16JobsTijRail2019FlowMap\x18S \x02(\t\x12\x1f\n\x17JobsTijRoads2030FlowMap\x18T \x02(\t\x12\x1d\n\x15JobsTijBus2030FlowMap\x18U \x02(\t\x12\x1e\n\x16JobsTijRail2030FlowMap\x18V \x02(\t')



_STARTLUTIOXF = DESCRIPTOR.message_types_by_name['StartLutiOxf']
_STARTLUTIOXF_INPUTS = _STARTLUTIOXF.nested_types_by_name['Inputs']
_STARTLUTIOXF_OUTPUTS = _STARTLUTIOXF.nested_types_by_name['Outputs']
StartLutiOxf = _reflection.GeneratedProtocolMessageType('StartLutiOxf', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLUTIOXF_INPUTS,
    '__module__' : 'start_luti_oxf_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiOxf.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _STARTLUTIOXF_OUTPUTS,
    '__module__' : 'start_luti_oxf_pb2'
    # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiOxf.Outputs)
    })
  ,
  'DESCRIPTOR' : _STARTLUTIOXF,
  '__module__' : 'start_luti_oxf_pb2'
  # @@protoc_insertion_point(class_scope:harmonyServer.StartLutiOxf)
  })
_sym_db.RegisterMessage(StartLutiOxf)
_sym_db.RegisterMessage(StartLutiOxf.Inputs)
_sym_db.RegisterMessage(StartLutiOxf.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTLUTIOXF._serialized_start=40
  _STARTLUTIOXF._serialized_end=3517
  _STARTLUTIOXF_INPUTS._serialized_start=183
  _STARTLUTIOXF_INPUTS._serialized_end=885
  _STARTLUTIOXF_OUTPUTS._serialized_start=888
  _STARTLUTIOXF_OUTPUTS._serialized_end=3517
# @@protoc_insertion_point(module_scope)
