# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/web_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/web_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/data/telemetry/web_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"f\n\x0cWebTelemetry\x12\x38\n\rweb_click_ids\x18\x01 \x01(\x0e\x32!.pogoprotos.enums.WebTelemetryIds\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_WEBTELEMETRY = _descriptor.Descriptor(
  name='WebTelemetry',
  full_name='pogoprotos.data.telemetry.WebTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='web_click_ids', full_name='pogoprotos.data.telemetry.WebTelemetry.web_click_ids', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='pogoprotos.data.telemetry.WebTelemetry.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.telemetry.WebTelemetry.fort_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=216,
)

_WEBTELEMETRY.fields_by_name['web_click_ids'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._WEBTELEMETRYIDS
DESCRIPTOR.message_types_by_name['WebTelemetry'] = _WEBTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebTelemetry = _reflection.GeneratedProtocolMessageType('WebTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _WEBTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.web_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.WebTelemetry)
  ))
_sym_db.RegisterMessage(WebTelemetry)


# @@protoc_insertion_point(module_scope)
