# python bindings for the msm camera
# see: msmb_camera.h

from .v4l2 import *
from .media import *
import ctypes


class msm_v4l2_event_data(ctypes.Structure):
    _fields_ = [
        ('command', ctypes.c_uint32),
        ('status', ctypes.c_uint32),
        ('session_id', ctypes.c_uint32),
        ('stream_id', ctypes.c_uint32),
        ('map_op', ctypes.c_uint32),
        ('map_buf_idx', ctypes.c_uint32),
        ('notify', ctypes.c_uint32),
        ('arg_value', ctypes.c_uint32),
        ('ret_value', ctypes.c_uint32),
        ('v4l2_event_type', ctypes.c_uint32),
        ('v4l2_event_id', ctypes.c_uint32),
        ('handle', ctypes.c_uint32),
        ('nop6', ctypes.c_uint32),
        ('nop7', ctypes.c_uint32),
        ('nop8', ctypes.c_uint32),
        ('nop9', ctypes.c_uint32),
    ]


MSM_CAM_V4L2_IOCTL_NOTIFY = IOW('V', BASE_VIDIOC_PRIVATE + 30, msm_v4l2_event_data)
MSM_CAM_V4L2_IOCTL_NOTIFY_META = IOW('V', BASE_VIDIOC_PRIVATE + 31, msm_v4l2_event_data)
MSM_CAM_V4L2_IOCTL_CMD_ACK = IOW('V', BASE_VIDIOC_PRIVATE + 32, msm_v4l2_event_data)
MSM_CAM_V4L2_IOCTL_NOTIFY_ERROR = IOW('V', BASE_VIDIOC_PRIVATE + 33, msm_v4l2_event_data)
MSM_CAM_V4L2_IOCTL_NOTIFY_DEBUG = IOW('V', BASE_VIDIOC_PRIVATE + 34, msm_v4l2_event_data)
MSM_CAM_V4L2_IOCTL_DAEMON_DISABLED = IOW('V', BASE_VIDIOC_PRIVATE + 35, msm_v4l2_event_data)

QCAMERA_DEVICE_GROUP_ID = 1
QCAMERA_VNODE_GROUP_ID = 2
MSM_CAMERA_NAME = b"msm_camera"
MSM_CONFIGURATION_NAME = b"msm_config"

MSM_CAMERA_SUBDEV_CSIPHY = 0
MSM_CAMERA_SUBDEV_CSID = 1
MSM_CAMERA_SUBDEV_ISPIF = 2
MSM_CAMERA_SUBDEV_VFE = 3
MSM_CAMERA_SUBDEV_AXI = 4
MSM_CAMERA_SUBDEV_VPE = 5
MSM_CAMERA_SUBDEV_SENSOR = 6
MSM_CAMERA_SUBDEV_ACTUATOR = 7
MSM_CAMERA_SUBDEV_EEPROM = 8
MSM_CAMERA_SUBDEV_CPP = 9
MSM_CAMERA_SUBDEV_CCI = 10
MSM_CAMERA_SUBDEV_LED_FLASH = 11
MSM_CAMERA_SUBDEV_STROBE_FLASH = 12
MSM_CAMERA_SUBDEV_BUF_MNGR = 13
MSM_CAMERA_SUBDEV_SENSOR_INIT = 14
MSM_CAMERA_SUBDEV_OIS = 15
MSM_CAMERA_SUBDEV_FLASH = 16
MSM_CAMERA_SUBDEV_IR_LED = 17
MSM_CAMERA_SUBDEV_IR_CUT = 18
MSM_CAMERA_SUBDEV_EXT = 19

MSM_MAX_CAMERA_SENSORS = 5

MSM_CAMERA_MAX_STREAM_BUF = 72

MSM_CAMERA_MAX_USER_BUFF_CNT = 16

MSM_CAMERA_FEATURE_BASE = 0x00010000
MSM_CAMERA_FEATURE_SHUTDOWN = (MSM_CAMERA_FEATURE_BASE + 1)

MSM_CAMERA_STATUS_BASE = 0x00020000
MSM_CAMERA_STATUS_FAIL = (MSM_CAMERA_STATUS_BASE + 1)
MSM_CAMERA_STATUS_SUCCESS = (MSM_CAMERA_STATUS_BASE + 2)

MSM_CAMERA_V4L2_EVENT_TYPE = (V4L2_EVENT_PRIVATE_START + 0x00002000)

MSM_CAMERA_EVENT_MIN = 0
MSM_CAMERA_NEW_SESSION = (MSM_CAMERA_EVENT_MIN + 1)
MSM_CAMERA_DEL_SESSION = (MSM_CAMERA_EVENT_MIN + 2)
MSM_CAMERA_SET_PARM = (MSM_CAMERA_EVENT_MIN + 3)
MSM_CAMERA_GET_PARM = (MSM_CAMERA_EVENT_MIN + 4)
MSM_CAMERA_MAPPING_CFG = (MSM_CAMERA_EVENT_MIN + 5)
MSM_CAMERA_MAPPING_SES = (MSM_CAMERA_EVENT_MIN + 6)
MSM_CAMERA_MSM_NOTIFY = (MSM_CAMERA_EVENT_MIN + 7)
MSM_CAMERA_EVENT_MAX = (MSM_CAMERA_EVENT_MIN + 8)

MSM_CAMERA_PRIV_S_CROP = (V4L2_CID_PRIVATE_BASE + 1)
MSM_CAMERA_PRIV_G_CROP = (V4L2_CID_PRIVATE_BASE + 2)
MSM_CAMERA_PRIV_G_FMT = (V4L2_CID_PRIVATE_BASE + 3)
MSM_CAMERA_PRIV_S_FMT = (V4L2_CID_PRIVATE_BASE + 4)
MSM_CAMERA_PRIV_TRY_FMT = (V4L2_CID_PRIVATE_BASE + 5)
MSM_CAMERA_PRIV_METADATA = (V4L2_CID_PRIVATE_BASE + 6)
MSM_CAMERA_PRIV_QUERY_CAP = (V4L2_CID_PRIVATE_BASE + 7)
MSM_CAMERA_PRIV_STREAM_ON = (V4L2_CID_PRIVATE_BASE + 8)
MSM_CAMERA_PRIV_STREAM_OFF = (V4L2_CID_PRIVATE_BASE + 9)
MSM_CAMERA_PRIV_NEW_STREAM = (V4L2_CID_PRIVATE_BASE + 10)
MSM_CAMERA_PRIV_DEL_STREAM = (V4L2_CID_PRIVATE_BASE + 11)
MSM_CAMERA_PRIV_SHUTDOWN = (V4L2_CID_PRIVATE_BASE + 12)
MSM_CAMERA_PRIV_STREAM_INFO_SYNC = (V4L2_CID_PRIVATE_BASE + 13)
MSM_CAMERA_PRIV_G_SESSION_ID = (V4L2_CID_PRIVATE_BASE + 14)
MSM_CAMERA_PRIV_CMD_MAX = 20

MSM_CAMERA_CMD_SUCESS = 0x00000001
MSM_CAMERA_BUF_MAP_SUCESS = 0x00000002

MSM_CAMERA_ERR_EVT_BASE = 0x00010000
MSM_CAMERA_ERR_CMD_FAIL = (MSM_CAMERA_ERR_EVT_BASE + 1)
MSM_CAMERA_ERR_MAPPING = (MSM_CAMERA_ERR_EVT_BASE + 2)
MSM_CAMERA_ERR_DEVICE_BUSY = (MSM_CAMERA_ERR_EVT_BASE + 3)


class msm_v4l2_format_data(ctypes.Structure):
    _fields_ = [
        ('type', v4l2_buf_type),
        ('widith', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('pixelformat', ctypes.c_uint32),
        ('num_planes', ctypes.c_uint8),
        ('plane_sizes', ctypes.c_uint32 * VIDEO_MAX_PLANES),
    ]


MSM_V4L2_PIX_FMT_STATS_COMB = v4l2_fourcc('S', 'T', 'C', 'M')
MSM_V4L2_PIX_FMT_STATS_AE = v4l2_fourcc('S', 'T', 'A', 'E')
MSM_V4L2_PIX_FMT_STATS_AF = v4l2_fourcc('S', 'T', 'A', 'F')
MSM_V4L2_PIX_FMT_STATS_AWB = v4l2_fourcc('S', 'T', 'W', 'B')
MSM_V4L2_PIX_FMT_STATS_IHST = v4l2_fourcc('I', 'H', 'S', 'T')
MSM_V4L2_PIX_FMT_STATS_CS = v4l2_fourcc('S', 'T', 'C', 'S')
MSM_V4L2_PIX_FMT_STATS_RS = v4l2_fourcc('S', 'T', 'R', 'S')
MSM_V4L2_PIX_FMT_STATS_BG = v4l2_fourcc('S', 'T', 'B', 'G')
MSM_V4L2_PIX_FMT_STATS_BF = v4l2_fourcc('S', 'T', 'B', 'F')
MSM_V4L2_PIX_FMT_STATS_BHST = v4l2_fourcc('B', 'H', 'S', 'T')

smmu_attach_mode = enum
(
    NON_SECURE_MODE,
    SECURE_MODE,
    MAX_PROTECTION_MODE
) = range(1, 1 + 3)


class msm_camera_smmu_attach_type(ctypes.Structure):
    _fields_ = [
        ('attach', smmu_attach_mode),
    ]


class msm_camera_user_buf_cont_t(ctypes.Structure):
    _fields_ = [
        ('buf_cnt', ctypes.c_uint32),
        ('buf_idx', ctypes.c_uint32 * MSM_CAMERA_MAX_USER_BUFF_CNT),
    ]


class msm_camera_return_buf(ctypes.Structure):
    _fields_ = [
        ('index', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32),
    ]


MSM_CAMERA_PRIV_IOCTL_ID_BASE = 0
MSM_CAMERA_PRIV_IOCTL_ID_RETURN_BUF = 1


class msm_camera_private_ioctl_arg(ctypes.Structure):
    _fields_ = [
        ('id', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('result', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32),
        ('ioctl_ptr', ctypes.c_uint64),
    ]


VIDIOC_MSM_CAMERA_PRIVATE_IOCTL_CMD = IOWR('V', BASE_VIDIOC_PRIVATE, msm_camera_private_ioctl_arg)
