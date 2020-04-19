#!/usr/bin/env python

from .v4l2 import *
import ctypes


class media_device_info(ctypes.Structure):
    _fields_ = [
        ('driver', ctypes.c_char * 16),
        ('model', ctypes.c_char * 32),
        ('serial', ctypes.c_char * 40),
        ('bus_info', ctypes.c_char * 32),
        ('media_version', ctypes.c_uint32),
        ('hw_revision', ctypes.c_uint32),
        ('driver_version', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32 * 31),
    ]


MEDIA_ENT_ID_FLAG_NEXT = (1 << 31)

MEDIA_ENT_TYPE_SHIFT = 16
MEDIA_ENT_TYPE_MASK = 0x00ff0000
MEDIA_ENT_SUBTYPE_MASK = 0x0000ffff

MEDIA_ENT_T_DEVNODE = (1 << MEDIA_ENT_TYPE_SHIFT)
MEDIA_ENT_T_DEVNODE_V4L = (MEDIA_ENT_T_DEVNODE + 1)
MEDIA_ENT_T_DEVNODE_FB = (MEDIA_ENT_T_DEVNODE + 2)
MEDIA_ENT_T_DEVNODE_ALSA = (MEDIA_ENT_T_DEVNODE + 3)
MEDIA_ENT_T_DEVNODE_DVB = (MEDIA_ENT_T_DEVNODE + 4)

MEDIA_ENT_T_V4L2_SUBDEV = (2 << MEDIA_ENT_TYPE_SHIFT)
MEDIA_ENT_T_V4L2_SUBDEV_SENSOR = (MEDIA_ENT_T_V4L2_SUBDEV + 1)
MEDIA_ENT_T_V4L2_SUBDEV_FLASH = (MEDIA_ENT_T_V4L2_SUBDEV + 2)
MEDIA_ENT_T_V4L2_SUBDEV_LENS = (MEDIA_ENT_T_V4L2_SUBDEV + 3)
MEDIA_ENT_T_V4L2_SUBDEV_DECODER = (MEDIA_ENT_T_V4L2_SUBDEV + 4)
MEDIA_ENT_FL_DEFAULT = (1 << 0)


class _u_v4l(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint32),
        ('minor', ctypes.c_uint32),
    ]


class _u_fb(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint32),
        ('minor', ctypes.c_uint32),
    ]


class _u_alsa(ctypes.Structure):
    _fields_ = [
        ('card', ctypes.c_uint32),
        ('device', ctypes.c_uint32),
        ('subdevice', ctypes.c_uint32),
    ]


class media_entity_desc(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ('v4l', _u_v4l),
            ('fb', _u_fb),
            ('alsa', _u_alsa),
            ('dvb', ctypes.c_int32),
            ('raw', ctypes.c_uint8 * 184)
        ]

    _fields_ = [
        ('id', ctypes.c_uint32),
        ('name', ctypes.c_char * 32),
        ('type', ctypes.c_uint32),
        ('revision', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
        ('group_id', ctypes.c_uint32),
        ('pads', ctypes.c_uint16),
        ('links', ctypes.c_uint16),
        ('reserved', ctypes.c_uint32 * 4),
        ('_u', _u),
    ]
    _anonymous_ = ('_u',)


MEDIA_PAD_FL_SINK = (1 << 0)
MEDIA_PAD_FL_SOURCE = (1 << 1)
MEDIA_PAD_FL_MUST_CONNECT = (1 << 2)


class media_pad_desc(ctypes.Structure):
    _fields_ = [
        ('entity', ctypes.c_uint32),
        ('index', ctypes.c_uint16),
        ('flags', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32 * 2),
    ]


MEDIA_LNK_FL_ENABLED = (1 << 0)
MEDIA_LNK_FL_IMMUTABLE = (1 << 1)
MEDIA_LNK_FL_DYNAMIC = (1 << 2)


class media_link_desc(ctypes.Structure):
    _fields_ = [
        ('source', media_pad_desc),
        ('sink', media_pad_desc),
        ('flags', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32 * 2),
    ]


class media_links_enum(ctypes.Structure):
    _fields_ = [
        ('entity', ctypes.c_uint32),
        ('pads', ctypes.POINTER(media_pad_desc)),
        ('links', ctypes.POINTER(media_link_desc)),
        ('reserved', ctypes.c_uint32 * 4),
    ]


MEDIA_IOC_DEVICE_INFO = IOWR('|', 0x00, media_device_info)
MEDIA_IOC_ENUM_ENTITIES = IOWR('|', 0x01, media_entity_desc)
MEDIA_IOC_ENUM_LINKS = IOWR('|', 0x02, media_links_enum)
MEDIA_IOC_SETUP_LINK = IOWR('|', 0x03, media_link_desc)


