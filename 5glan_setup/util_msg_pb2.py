# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='util_msg.proto',
  package='bess.pb',
  syntax='proto3',
  serialized_options=_b('Z1github.com/omec-project/upf-epc/pfcpiface/bess_pb'),
  serialized_pb=_b('\n\x0eutil_msg.proto\x12\x07\x62\x65ss.pb\"M\n\x05\x46ield\x12\x13\n\tattr_name\x18\x01 \x01(\tH\x00\x12\x10\n\x06offset\x18\x02 \x01(\rH\x00\x12\x11\n\tnum_bytes\x18\x03 \x01(\rB\n\n\x08position\"A\n\tFieldData\x12\x13\n\tvalue_bin\x18\x01 \x01(\x0cH\x00\x12\x13\n\tvalue_int\x18\x02 \x01(\x04H\x00\x42\n\n\x08\x65ncodingB3Z1github.com/omec-project/upf-epc/pfcpiface/bess_pbb\x06proto3')
)




_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='bess.pb.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr_name', full_name='bess.pb.Field.attr_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='bess.pb.Field.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_bytes', full_name='bess.pb.Field.num_bytes', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='position', full_name='bess.pb.Field.position',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=27,
  serialized_end=104,
)


_FIELDDATA = _descriptor.Descriptor(
  name='FieldData',
  full_name='bess.pb.FieldData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_bin', full_name='bess.pb.FieldData.value_bin', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_int', full_name='bess.pb.FieldData.value_int', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='encoding', full_name='bess.pb.FieldData.encoding',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=106,
  serialized_end=171,
)

_FIELD.oneofs_by_name['position'].fields.append(
  _FIELD.fields_by_name['attr_name'])
_FIELD.fields_by_name['attr_name'].containing_oneof = _FIELD.oneofs_by_name['position']
_FIELD.oneofs_by_name['position'].fields.append(
  _FIELD.fields_by_name['offset'])
_FIELD.fields_by_name['offset'].containing_oneof = _FIELD.oneofs_by_name['position']
_FIELDDATA.oneofs_by_name['encoding'].fields.append(
  _FIELDDATA.fields_by_name['value_bin'])
_FIELDDATA.fields_by_name['value_bin'].containing_oneof = _FIELDDATA.oneofs_by_name['encoding']
_FIELDDATA.oneofs_by_name['encoding'].fields.append(
  _FIELDDATA.fields_by_name['value_int'])
_FIELDDATA.fields_by_name['value_int'].containing_oneof = _FIELDDATA.oneofs_by_name['encoding']
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['FieldData'] = _FIELDDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'util_msg_pb2'
  # @@protoc_insertion_point(class_scope:bess.pb.Field)
  })
_sym_db.RegisterMessage(Field)

FieldData = _reflection.GeneratedProtocolMessageType('FieldData', (_message.Message,), {
  'DESCRIPTOR' : _FIELDDATA,
  '__module__' : 'util_msg_pb2'
  # @@protoc_insertion_point(class_scope:bess.pb.FieldData)
  })
_sym_db.RegisterMessage(FieldData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
