# python bindings for the msm cci
# see: msm_cci.h

from .v4l2 import *
from .msm_cam_sensor import *

msm_cci_cmd_type = enum
(
    MSM_CCI_INIT,
    MSM_CCI_RELEASE,
    MSM_CCI_SET_SID,
    MSM_CCI_SET_FREQ,
    MSM_CCI_SET_SYNC_CID,
    MSM_CCI_I2C_READ,
    MSM_CCI_I2C_WRITE,
    MSM_CCI_I2C_WRITE_SEQ,
    MSM_CCI_I2C_WRITE_ASYNC,
    MSM_CCI_GPIO_WRITE,
    MSM_CCI_I2C_WRITE_SYNC,
    MSM_CCI_I2C_WRITE_SYNC_BLOCK,
) = range(12)


class msm_camera_cci_client(ctypes.Structure):
    _fields_ = [
        # struct v4l2_subdev, not used when user call.
        # so we use c_void_p.
        ('cci_subdev', ctypes.c_void_p),
        ('freq', ctypes.c_uint32),
        ('i2c_freq_mode', i2c_freq_mode_t),
        ('cci_i2c_master', cci_i2c_master_t),
        ('sid', ctypes.c_uint16),
        ('cid', ctypes.c_uint16),
        ('timeout', ctypes.c_uint32),
        ('retries', ctypes.c_uint16),
        ('id_map', ctypes.c_uint16),
    ]


class msm_camera_cci_i2c_read_cfg(ctypes.Structure):
    _fields_ = [
        ('addr', ctypes.c_uint32),
        ('addr_type', msm_camera_i2c_reg_addr_type),
        ('data', ctypes.POINTER(ctypes.c_uint8)),
        ('num_byte', ctypes.c_uint16),
    ]


class msm_camera_cci_wait_sync_cfg(ctypes.Structure):
    _fields_ = [
        ('cid', ctypes.c_uint16),
        ('csid', ctypes.c_int16),
        ('line', ctypes.c_uint16),
        ('delay', ctypes.c_uint16),
    ]


class msm_camera_cci_gpio_cfg(ctypes.Structure):
    _fields_ = [
        ('gpio_queue', ctypes.c_uint16),
        ('i2c_queue', ctypes.c_int16),
    ]


class msm_camera_cci_ctrl(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ('cci_i2c_write_cfg', msm_camera_i2c_reg_setting),
            ('cci_i2c_read_cfg', msm_camera_cci_i2c_read_cfg),
            ('cci_wait_sync_cfg', msm_camera_cci_wait_sync_cfg),
            ('gpio_cfg', msm_camera_cci_gpio_cfg),
        ]

    _fields_ = [
        ('status', ctypes.c_uint64),
        ('cci_info', ctypes.POINTER(msm_camera_cci_client)),
        ('cmd', ctypes.c_uint64),
        ('cfg', _u)
    ]


VIDIOC_MSM_CCI_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 23, msm_camera_cci_ctrl)
