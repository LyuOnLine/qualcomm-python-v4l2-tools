# python bindings for the msm camera
# see: media/msm_cam_sensor.h
from .v4l2 import *
from .msmb_camera import *

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


# depending data structure

msm_camera_i2c_reg_addr_type = enum
(
    MSM_CAMERA_I2C_BYTE_ADDR,
    MSM_CAMERA_I2C_WORD_ADDR,
    MSM_CAMERA_I2C_3B_ADDR,
) = range(1, 4)

msm_camera_i2c_data_type = enum
(
    MSM_CAMERA_I2C_BYTE_DATA,
    MSM_CAMERA_I2C_WORD_DATA,
    MSM_CAMERA_I2C_SET_BYTE_MASK,
    MSM_CAMERA_I2C_UNSET_BYTE_MASK,
    MSM_CAMERA_I2C_SET_WORD_MASK,
    MSM_CAMERA_I2C_UNSET_WORD_MASK,
    MSM_CAMERA_I2C_SET_BYTE_WRITE_MASK_DATA,
) = range(1, 8)

i2c_freq_mode_t = enum
(
    I2C_STANDARD_MODE,
    I2C_FAST_MODE,
    I2C_CUSTOM_MODE,
    I2C_FAST_PLUS_MODE,
    I2C_MAX_MODES,
) = range(5)


class msm_camera_i2c_reg_array(ctypes.Structure):
    _fields_ = [
        ('reg_addr', ctypes.c_uint16),
        ('reg_data', ctypes.c_uint16),
        ('delay', ctypes.c_uint32),
    ]


class msm_camera_i2c_reg_setting(ctypes.Structure):
    _fields_ = [
        ('reg_setting', ctypes.POINTER(msm_camera_i2c_reg_array)),
        ('size', ctypes.c_uint16),
        ('addr_type', msm_camera_i2c_reg_addr_type),
        ('data_type', msm_camera_i2c_data_type),
        ('delay', ctypes.c_uint16),
    ]

class eeprom_write_t(ctypes.Structure):
    _fields_ = [
        ('dbuffer', ctypes.POINTER(ctypes.c_uint8)),
        ('num_bytes', ctypes.c_uint32),
    ]


msm_sensor_power_seq_type_t = enum
(
    SENSOR_CLK,
    SENSOR_GPIO,
    SENSOR_VREG,
    SENSOR_I2C_MUX,
    SENSOR_I2C,
) = range(5)

MAX_POWER_CONFIG = 12


class msm_sensor_power_setting(ctypes.Structure):
    _fields_ = [
        ('seq_type', msm_sensor_power_seq_type_t),
        ('seq_val', ctypes.c_ushort),
        ('config_val', ctypes.c_long),
        ('delay', ctypes.c_ushort),
        ('data', ctypes.c_void_p * 10),
    ]


class msm_sensor_power_setting_array(ctypes.Structure):
    _fields_ = [
        ('power_setting_a', msm_sensor_power_setting * MAX_POWER_CONFIG),
        ('power_setting', msm_sensor_power_setting),
        ('size', ctypes.c_ushort),
        ('power_down_setting_a', msm_sensor_power_setting * MAX_POWER_CONFIG),
        ('power_down_setting', msm_sensor_power_setting),
        ('size_down', ctypes.c_short),
    ]


i2c_freq_mode_t = enum
(
    I2C_STANDARD_MODE,
    I2C_FAST_MODE,
    I2C_CUSTOM_MODE,
    I2C_FAST_PLUS_MODE,
    I2C_MAX_MODES,
) = range(5)

MSM_EEPROM_MEMORY_MAP_MAX_SIZE = 80

msm_camera_i2c_operation = enum
(
    MSM_CAM_WRITE,
    MSM_CAM_POLL,
    MSM_CAM_READ,
) = range(3)


class msm_camera_reg_settings_t(ctypes.Structure):
    _fields_ = [
        ('reg_addr', ctypes.c_uint16),
        ('addr_type', msm_camera_i2c_reg_addr_type),
        ('reg_data', ctypes.c_uint16),
        ('data_type', msm_camera_i2c_data_type),
        ('i2c_operation', msm_camera_i2c_operation),
        ('delay', ctypes.c_uint16),
    ]


class msm_eeprom_mem_map_t(ctypes.Structure):
    _fields_ = [
        ('slave_addr', ctypes.c_int),
        ('mem_settings', msm_camera_reg_settings_t * MSM_EEPROM_MEMORY_MAP_MAX_SIZE),
        ('memory_map_size', ctypes.c_int),
    ]


MSM_EEPROM_MAX_MEM_MAP_CNT = 8


class msm_eeprom_memory_map_array(ctypes.Structure):
    _fields_ = [
        ('memory_map', msm_eeprom_mem_map_t * MSM_EEPROM_MAX_MEM_MAP_CNT),
        ('msm_size_of_max_mappings', ctypes.c_uint32),
    ]


# end of depending data structure



I2C_SEQ_REG_SETTING_MAX = 5

MSM_SENSOR_MCLK_8HZ = 8000000
MSM_SENSOR_MCLK_16HZ = 16000000
MSM_SENSOR_MCLK_24HZ = 24000000

MAX_SENSOR_NAME = 32
MAX_ACTUATOR_AF_TOTAL_STEPS = 1024

MAX_OIS_MOD_NAME_SIZE = 32
MAX_OIS_NAME_SIZE = 32
MAX_OIS_REG_SETTINGS = 800

MOVE_NEAR = 0
MOVE_FAR = 1

MSM_ACTUATOR_MOVE_SIGNED_FAR = -1
MSM_ACTUATOR_MOVE_SIGNED_NEAR = 1

MAX_ACTUATOR_REGION = 5

MAX_EEPROM_NAME = 32

MAX_AF_ITERATIONS = 3
MAX_NUMBER_OF_STEPS = 47
MAX_REGULATOR = 5

MSM_V4L2_PIX_FMT_META = v4l2_fourcc('M', 'E', 'T', 'A')
MSM_V4L2_PIX_FMT_META10 = v4l2_fourcc('M', 'E', '1', '0')
MSM_V4L2_PIX_FMT_SBGGR14 = v4l2_fourcc('B', 'G', '1', '4')
MSM_V4L2_PIX_FMT_SGBRG14 = v4l2_fourcc('G', 'B', '1', '4')
MSM_V4L2_PIX_FMT_SGRBG14 = v4l2_fourcc('B', 'A', '1', '4')
MSM_V4L2_PIX_FMT_SRGGB14 = v4l2_fourcc('R', 'G', '1', '4')

flash_type = enum
(
    LED_FLASH,
    STROBE_FLASH,
    GPIO_FLASH
) = range(1, 4)

msm_sensor_resolution_t = enum
(
    MSM_SENSOR_RES_FULL,
    MSM_SENSOR_RES_QTR,
    MSM_SENSOR_RES_2,
    MSM_SENSOR_RES_3,
    MSM_SENSOR_RES_4,
    MSM_SENSOR_RES_5,
    MSM_SENSOR_RES_6,
    MSM_SENSOR_RES_7,
    MSM_SENSOR_INVALID_RES,
) = range(9)

msm_camera_stream_type_t = enum
(
    MSM_CAMERA_STREAM_PREVIEW,
    MSM_CAMERA_STREAM_SNAPSHOT,
    MSM_CAMERA_STREAM_VIDEO,
    MSM_CAMERA_STREAM_INVALID,
) = range(4)

sensor_sub_module_t = enum
(
    SUB_MODULE_SENSOR,
    SUB_MODULE_CHROMATIX,
    SUB_MODULE_ACTUATOR,
    SUB_MODULE_EEPROM,
    SUB_MODULE_LED_FLASH,
    SUB_MODULE_STROBE_FLASH,
    SUB_MODULE_CSID,
    SUB_MODULE_CSID_3D,
    SUB_MODULE_CSIPHY,
    SUB_MODULE_CSIPHY_3D,
    SUB_MODULE_OIS,
    SUB_MODULE_EXT,
    SUB_MODULE_IR_LED,
    SUB_MODULE_IR_CUT,
    SUB_MODULE_MAX,
) = range(15)

(
    MSM_CAMERA_EFFECT_MODE_OFF,
    MSM_CAMERA_EFFECT_MODE_MONO,
    MSM_CAMERA_EFFECT_MODE_NEGATIVE,
    MSM_CAMERA_EFFECT_MODE_SOLARIZE,
    MSM_CAMERA_EFFECT_MODE_SEPIA,
    MSM_CAMERA_EFFECT_MODE_POSTERIZE,
    MSM_CAMERA_EFFECT_MODE_WHITEBOARD,
    MSM_CAMERA_EFFECT_MODE_BLACKBOARD,
    MSM_CAMERA_EFFECT_MODE_AQUA,
    MSM_CAMERA_EFFECT_MODE_EMBOSS,
    MSM_CAMERA_EFFECT_MODE_SKETCH,
    MSM_CAMERA_EFFECT_MODE_NEON,
    MSM_CAMERA_EFFECT_MODE_MAX
) = range(13)

(
    MSM_CAMERA_WB_MODE_AUTO,
    MSM_CAMERA_WB_MODE_CUSTOM,
    MSM_CAMERA_WB_MODE_INCANDESCENT,
    MSM_CAMERA_WB_MODE_FLUORESCENT,
    MSM_CAMERA_WB_MODE_WARM_FLUORESCENT,
    MSM_CAMERA_WB_MODE_DAYLIGHT,
    MSM_CAMERA_WB_MODE_CLOUDY_DAYLIGHT,
    MSM_CAMERA_WB_MODE_TWILIGHT,
    MSM_CAMERA_WB_MODE_SHADE,
    MSM_CAMERA_WB_MODE_OFF,
    MSM_CAMERA_WB_MODE_MAX
) = range(11)

(
    MSM_CAMERA_SCENE_MODE_OFF,
    MSM_CAMERA_SCENE_MODE_AUTO,
    MSM_CAMERA_SCENE_MODE_LANDSCAPE,
    MSM_CAMERA_SCENE_MODE_SNOW,
    MSM_CAMERA_SCENE_MODE_BEACH,
    MSM_CAMERA_SCENE_MODE_SUNSET,
    MSM_CAMERA_SCENE_MODE_NIGHT,
    MSM_CAMERA_SCENE_MODE_PORTRAIT,
    MSM_CAMERA_SCENE_MODE_BACKLIGHT,
    MSM_CAMERA_SCENE_MODE_SPORTS,
    MSM_CAMERA_SCENE_MODE_ANTISHAKE,
    MSM_CAMERA_SCENE_MODE_FLOWERS,
    MSM_CAMERA_SCENE_MODE_CANDLELIGHT,
    MSM_CAMERA_SCENE_MODE_FIREWORKS,
    MSM_CAMERA_SCENE_MODE_PARTY,
    MSM_CAMERA_SCENE_MODE_NIGHT_PORTRAIT,
    MSM_CAMERA_SCENE_MODE_THEATRE,
    MSM_CAMERA_SCENE_MODE_ACTION,
    MSM_CAMERA_SCENE_MODE_AR,
    MSM_CAMERA_SCENE_MODE_FACE_PRIORITY,
    MSM_CAMERA_SCENE_MODE_BARCODE,
    MSM_CAMERA_SCENE_MODE_HDR,
    MSM_CAMERA_SCENE_MODE_MAX
) = range(23)

csid_cfg_type_t = enum
(
    CSID_INIT,
    CSID_CFG,
    CSID_TESTMODE_CFG,
    CSID_RELEASE,
) = range(4)

csiphy_cfg_type_t = enum
(
    CSIPHY_INIT,
    CSIPHY_CFG,
    CSIPHY_RELEASE,
) = range(3)

camera_vreg_type = enum
(
    VREG_TYPE_DEFAULT,
    VREG_TYPE_CUSTOM,
) = range(2)

sensor_af_t = enum
(
    SENSOR_AF_FOCUSSED,
    SENSOR_AF_NOT_FOCUSSED,
) = range(2)

cci_i2c_master_t = enum
(
    MASTER_0,
    MASTER_1,
    MASTER_MAX,
) = range(3)


class msm_camera_i2c_array_write_config(ctypes.Structure):
    _fields_ = [
        ('conf_array', msm_camera_i2c_reg_setting),
        ('slave_addr', ctypes.c_uint16),
    ]


class msm_camera_i2c_read_config(ctypes.Structure):
    _fields_ = [
        ('slave_addr', ctypes.c_uint16),
        ('reg_addr', ctypes.c_uint16),
        ('addr_type', msm_camera_i2c_reg_addr_type),
        ('data_type', msm_camera_i2c_data_type),
        ('data', ctypes.c_uint16),
    ]


# csi config

# sensor config

# csiphy config
csiphy_cfg_type_t = enum
(
    CSIPHY_INIT,
    CSIPHY_CFG,
    CSIPHY_RELEASE,
) = range(3)


class msm_camera_csi_lane_params(ctypes.Structure):
    _fields_ = [
        ("csi_lane_assign", ctypes.c_uint16),
        ("csi_lane_mask", ctypes.c_uint16),
    ]


class msm_camera_csid_testmode_parms(ctypes.Structure):
    _fields_ = [
        ("num_bytes_per_line", ctypes.c_uint32),
        ("num_lines", ctypes.c_uint32),
        ("h_blanking_count", ctypes.c_uint32),
        ("v_blanking_count", ctypes.c_uint32),
        ("payload_mode", ctypes.c_uint32),
    ]


# from msm_camsensor_sdk.h
class msm_camera_csiphy_params(ctypes.Structure):
    _fields_ = [
        ("lane_cnt", ctypes.c_uint8),
        ("settle_cnt", ctypes.c_uint8),
        ("lane_mask", ctypes.c_uint8),
        ("combo_mode", ctypes.c_uint8),
        ("csid_core", ctypes.c_uint8),
        ("csiphy_clk", ctypes.c_uint8),
        ("csi_3phase", ctypes.c_uint8),
    ]


class csiphy_cfg_data(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ("csiphy_params", ctypes.POINTER(msm_camera_csiphy_params)),
            ("csi_lane_params", ctypes.POINTER(msm_camera_csi_lane_params)),
        ]

    _fields_ = [
        ("cfgtype", csiphy_cfg_type_t),
        ("cfg", _u),
    ]


# csid config
MAX_CID = 16
class msm_camera_csid_vc_cfg(ctypes.Structure):
    _fields_ = [
        ("cid", ctypes.c_uint8),
        ("dt", ctypes.c_uint8),
        ("decode_format", ctypes.c_uint8),
    ]


csid_cfg_type_t = enum
(
    CSID_INIT,
    CSID_CFG,
    CSID_TESTMODE_CFG,
    CSID_RELEASE,
) = range(4)


class msm_camera_csid_lut_params(ctypes.Structure):
    _fields_ = [
        ("num_cid", ctypes.c_uint8),
        ("vc_cfg_a", msm_camera_csid_vc_cfg * MAX_CID),
        ("vc_cfg", ctypes.POINTER(msm_camera_csid_vc_cfg) * MAX_CID)
    ]


class msm_camera_csid_params(ctypes.Structure):
    _fields_ = [
        ("lane_cnt", ctypes.c_uint8),
        ("lane_assign", ctypes.c_uint16),
        ("phy_sel", ctypes.c_uint8),
        ("csi_clk", ctypes.c_uint32),
        ("lut_params", msm_camera_csid_lut_params),
        ("csi_3p_sel", ctypes.c_uint8),
        #("tt", ctypes.c_uint8 * 500),
    ]


class csid_cfg_data(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ("csif_version", ctypes.c_uint32),
            ("csid_params", ctypes.POINTER(msm_camera_csid_params)),
            ("csid_testmode_params", ctypes.POINTER(msm_camera_csid_testmode_parms)),
        ]

    _fields_ = [
        ("cfgtype", csid_cfg_type_t),
        ("cfg", _u),
    ]


# ispif
msm_ispif_vfe_intf = enum
(
    VFE0,
    VFE1,
    VFE_MAX,
) = range(3)


class msm_isp_info(ctypes.Structure):
    _fields_ = [
        ("max_resolution", ctypes.c_uint32),
        ("id", ctypes.c_uint32),
        ("ver", ctypes.c_uint32),
    ]


class msm_ispif_vfe_info(ctypes.Structure):
    _fields_ = [
        ("num_vfe", ctypes.c_int),
        ("info", msm_isp_info * VFE_MAX)
    ]


msm_ispif_intftype = enum
(
    PIX0,
    RDI0,
    PIX1,
    RDI1,
    RDI2,
    INTF_MAX
) = range(6)

MAX_PARAM_ENTRIES = INTF_MAX * 2
MAX_CID_CH_v2 = 3

msm_ispif_cid = enum
(
    CID0,
    CID1,
    CID2,
    CID3,
    CID4,
    CID5,
    CID6,
    CID7,
    CID8,
    CID9,
    CID10,
    CID11,
    CID12,
    CID13,
    CID14,
    CID15,
    CID_MAX
) = range(17)

msm_ispif_csid = enum
(
    CSID0,
    CSID1,
    CSID2,
    CSID3,
    CSID_MAX
) = range(5)


class msm_ispif_params_entry(ctypes.Structure):
    _fields_ = [
        ("vfe_intf", msm_ispif_vfe_intf),
        ("intftype", msm_ispif_intftype),
        ("num_cids", ctypes.c_int),
        ("cids", msm_ispif_cid * MAX_CID_CH_v2),
        ("csid", msm_ispif_csid),
        ("crop_enable", ctypes.c_int32),
        ("crop_start_pixel", ctypes.c_uint16),
        ("crop_end_pixel", ctypes.c_uint16),
    ]


class msm_ispif_param_data(ctypes.Structure):
    _fields_ = [
        ("num", ctypes.c_uint32),
        ("entries", msm_ispif_params_entry * MAX_PARAM_ENTRIES)
    ]


ispif_cfg_type_t = enum
(
    ISPIF_CLK_ENABLE,
    ISPIF_CLK_DISABLE,
    ISPIF_INIT,
    ISPIF_CFG,
    ISPIF_START_FRAME_BOUNDARY,
    ISPIF_RESTART_FRAME_BOUNDARY,
    ISPIF_STOP_FRAME_BOUNDARY,
    ISPIF_STOP_IMMEDIATELY,
    ISPIF_RELEASE,
    ISPIF_ENABLE_REG_DUMP,
    ISPIF_SET_VFE_INFO,
    ISPIF_CFG2,
    ISPIF_CFG_STEREO,
) = range(13)


class ispif_cfg_data(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ("reg_dump", ctypes.c_int32),
            ("csid_version", ctypes.c_uint32),
            ("vfe_info", msm_ispif_vfe_info),
            ("params", msm_ispif_param_data),
        ]

    _fields_ = [
        ("cfg_type", ispif_cfg_type_t),
        ("_u", _u),
    ]
    _anonymous_ = ('_u',)


class ispif_cfg_data_ext(ctypes.Structure):
    _fields_ = [
        ("cfg_type", ispif_cfg_type_t),
        ("data", ctypes.c_void_p),
        ("size", ctypes.c_uint32),
    ]


# vfe(iface)
# msmb_isp.h
msm_vfe_camif_input = enum
(
    CAMIF_DISABLED,
    CAMIF_PAD_REG_INPUT,
    CAMIF_MIDDI_INPUT,
    CAMIF_MIPI_INPUT,
) = range(4)

msm_vfe_camif_output_format = enum
(
    CAMIF_QCOM_RAW,
    CAMIF_MIPI_RAW,
    CAMIF_PLAIN_8,
    CAMIF_PLAIN_16,
    CAMIF_MAX_FORMAT,
) = range(5)


class msm_vfe_camif_subsample_cfg(ctypes.Structure):
    _fields_ = [
        ("irq_subsample_period", ctypes.c_uint32),
        ("irq_subsample_pattern", ctypes.c_uint32),
        ("sof_counter_step", ctypes.c_uint32),
        ("pixel_skip", ctypes.c_uint32),
        ("line_skip", ctypes.c_uint32),
        ("first_line", ctypes.c_uint32),
        ("last_line", ctypes.c_uint32),
        ("first_pixel", ctypes.c_uint32),
        ("last_pixel", ctypes.c_uint32),
        ("output_format", msm_vfe_camif_output_format),
    ]


class msm_vfe_camif_cfg(ctypes.Structure):
    _fields_ = [
        ("lines_per_frame", ctypes.c_uint32),
        ("pixels_per_line", ctypes.c_uint32),
        ("first_pixel", ctypes.c_uint32),
        ("last_pixel", ctypes.c_uint32),
        ("first_line", ctypes.c_uint32),
        ("last_line", ctypes.c_uint32),
        ("epoch_line0", ctypes.c_uint32),
        ("epoch_line1", ctypes.c_uint32),
        ("is_split", ctypes.c_uint32),
        ("camif_input", msm_vfe_camif_input),
        ("subsample_cfg", msm_vfe_camif_subsample_cfg),
    ]


ISP_START_PIXEL_PATTERN = enum
(
    ISP_BAYER_RGRGRG,
    ISP_BAYER_GRGRGR,
    ISP_BAYER_BGBGBG,
    ISP_BAYER_GBGBGB,
    ISP_YUV_YCbYCr,
    ISP_YUV_YCrYCb,
    ISP_YUV_CbYCrY,
    ISP_YUV_CrYCbY,
    ISP_PIX_PATTERN_MAX
) = range(9)

msm_vfe_testgen_color_pattern = enum
(
    COLOR_BAR_8_COLOR,
    UNICOLOR_WHITE,
    UNICOLOR_YELLOW,
    UNICOLOR_CYAN,
    UNICOLOR_GREEN,
    UNICOLOR_MAGENTA,
    UNICOLOR_RED,
    UNICOLOR_BLUE,
    UNICOLOR_BLACK,
    MAX_COLOR,
) = range(10)


class msm_vfe_testgen_cfg(ctypes.Structure):
    _fields_ = [
        ("lines_per_frame", ctypes.c_uint32),
        ("pixels_per_line", ctypes.c_uint32),
        ("v_blank", ctypes.c_uint32),
        ("h_blank", ctypes.c_uint32),
        ("pixel_bayer_pattern", ISP_START_PIXEL_PATTERN),
        ("rotate_period", ctypes.c_uint32),
        ("color_bar_pattern", msm_vfe_testgen_color_pattern),
        ("burst_num_frame", ctypes.c_uint32),
    ]


class msm_vfe_fetch_engine_cfg(ctypes.Structure):
    _fields_ = [
        ("input_format", ctypes.c_uint32),
        ("buf_width", ctypes.c_uint32),
        ("buf_height", ctypes.c_uint32),
        ("fetch_width", ctypes.c_uint32),
        ("fetch_height", ctypes.c_uint32),
        ("x_offset", ctypes.c_uint32),
        ("y_offset", ctypes.c_uint32),
        ("buf_stride", ctypes.c_uint32),
    ]


msm_vfe_inputmux = enum
(
    CAMIF,
    TESTGEN,
    EXTERNAL_READ,
) = range(3)

msm_vfe_hvx_streaming_cmd = enum
(
    HVX_DISABLE,
    HVX_ONE_WAY,
    HVX_ROUND_TRIP
) = range(3)


class msm_vfe_pix_cfg(ctypes.Structure):
    _fields_ = [
        ("camif_cfg", msm_vfe_camif_cfg),
        ("testgen_cfg", msm_vfe_testgen_cfg),
        ("fetch_engine_cfg", msm_vfe_fetch_engine_cfg),
        ("input_mux", msm_vfe_inputmux),
        ("pixel_pattern", ISP_START_PIXEL_PATTERN),
        ("input_format", ctypes.c_uint32),
        ("hvx_cmd", msm_vfe_hvx_streaming_cmd),
        ("is_split", ctypes.c_uint32),
    ]


class msm_vfe_rdi_cfg(ctypes.Structure):
    _fields_ = [
        ("cid", ctypes.c_uint8),
        ("frame_based", ctypes.c_uint8),
    ]


msm_vfe_input_src = enum
(
    VFE_PIX_0,
    VFE_RAW_0,
    VFE_RAW_1,
    VFE_RAW_2,
    VFE_SRC_MAX,
) = range(5)


class msm_vfe_input_cfg(ctypes.Structure):
    class _u(ctypes.Union):
        _fields_ = [
            ("pix_cfg", msm_vfe_pix_cfg),
            ("rdi_cfg", msm_vfe_rdi_cfg),
        ]

    _fields_ = [
        ("d", _u),
        ("input_src", msm_vfe_input_src),
        ("input_pix_clk", ctypes.c_uint32),
    ]


# buffer_manager
# @msmb_generic_buf_mgr.h
msm_camera_buf_mngr_buf_type = enum
(
    MSM_CAMERA_BUF_MNGR_BUF_PLANAR,
    MSM_CAMERA_BUF_MNGR_BUF_USER,
    MSM_CAMERA_BUF_MNGR_BUF_INVALID,
) = range(3)


class timeval(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_uint64),
        ("tv_usec", ctypes.c_uint16),
    ]


class msm_buf_mngr_info(ctypes.Structure):
    _fields_ = [
        ("session_id", ctypes.c_uint32),
        ("stream_id", ctypes.c_uint32),
        ("frame_id", ctypes.c_uint32),
        ("timestamp", timeval),
        ("index", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("type", msm_camera_buf_mngr_buf_type),
        ("user_buf", msm_camera_user_buf_cont_t),
    ]


# eeprom config
eeprom_cfg_type_t = enum
(
    CFG_EEPROM_GET_INFO,
    CFG_EEPROM_GET_CAL_DATA,
    CFG_EEPROM_READ_CAL_DATA,
    CFG_EEPROM_WRITE_DATA,
    CFG_EEPROM_GET_MM_INFO,
    CFG_EEPROM_INIT,
) = range(6)


class eeprom_get_t(ctypes.Structure):
    _fields_ = [
        ('num_bytes', ctypes.c_uint32)
    ]


class eeprom_read_t(ctypes.Structure):
    _fields_ = [
        ('dbuffer', ctypes.POINTER(ctypes.c_uint8)),
        ('num_bytes', ctypes.c_uint32),
    ]


class eeprom_get_cmm_t(ctypes.Structure):
    _fields_ = [
        ('cmm_support', ctypes.c_uint32),
        ('cmm_compression', ctypes.c_uint32),
        ('cmm_size', ctypes.c_uint32),
    ]


class msm_eeprom_info_t(ctypes.Structure):
    _fields_ = [
        ('power_setting_array', ctypes.POINTER(msm_sensor_power_setting_array)),
        ('i2c_freq_mode', i2c_freq_mode_t),
        ('mem_map_array', ctypes.POINTER(msm_eeprom_memory_map_array)),
    ]


class msm_eeprom_cfg_data(ctypes.Structure):
    class _cfg(ctypes.Union):
        _fields_ = [
            ('eeprom_name', ctypes.c_char * MAX_SENSOR_NAME),
            ('get_data', eeprom_get_t),
            ('read_data', eeprom_read_t),
            ('write_data', eeprom_write_t),
            ('get_cmm_data', eeprom_get_cmm_t),
            ('eeprom_info', msm_eeprom_info_t),
        ]

    _fields_ = [
        ('cfgtype', eeprom_cfg_type_t),
        ('is_supported', ctypes.c_uint8),
        ('cfg', _cfg)
    ]


# common
VIDIOC_MSM_SENSOR_GET_SUBDEV_ID = IOWR('V', BASE_VIDIOC_PRIVATE + 3, ctypes.POINTER(ctypes.c_uint32))

# VIDIOC_MSM_SENSOR_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 1, sensorb_cfg_data)

VIDIOC_MSM_SENSOR_RELEASE = IO('V', BASE_VIDIOC_PRIVATE + 2)

VIDIOC_MSM_SENSOR_GET_SUBDEV_ID = IOWR('V', BASE_VIDIOC_PRIVATE + 3, ctypes.c_uint32)

VIDIOC_MSM_CSIPHY_IO_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 4, csiphy_cfg_data)

VIDIOC_MSM_CSID_IO_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 5, csid_cfg_data)

# VIDIOC_MSM_ACTUATOR_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 6, msm_actuator_cfg_data)

# VIDIOC_MSM_FLASH_LED_DATA_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 7, msm_camera_led_cfg_t)

VIDIOC_MSM_EEPROM_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 8, msm_eeprom_cfg_data)

VIDIOC_MSM_SENSOR_GET_AF_STATUS = IOWR('V', BASE_VIDIOC_PRIVATE + 9, ctypes.c_uint32)

# VIDIOC_MSM_SENSOR_INIT_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 10, sensor_init_cfg_data)

# VIDIOC_MSM_OIS_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 11, msm_ois_cfg_data)

# VIDIOC_MSM_FLASH_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 13, msm_flash_cfg_data_t)

# VIDIOC_MSM_OIS_CFG_DOWNLOAD = IOWR('V', BASE_VIDIOC_PRIVATE + 14, msm_ois_cfg_download_data)

# VIDIOC_MSM_IR_LED_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 15, msm_ir_led_cfg_data_t)

# VIDIOC_MSM_IR_CUT_CFG =	IOWR('V', BASE_VIDIOC_PRIVATE + 15,  msm_ir_cut_cfg_data_t)

# csiphy
VIDIOC_MSM_CSIPHY_IO_CFG = IOWR("V", BASE_VIDIOC_PRIVATE + 4, csiphy_cfg_data)

# csid
VIDIOC_MSM_CSID_IO_CFG = IOWR('V', BASE_VIDIOC_PRIVATE + 5, csid_cfg_data)

# ispif
VIDIOC_MSM_ISPIF_CFG = IOWR('V', BASE_VIDIOC_PRIVATE, ispif_cfg_data)
VIDIOC_MSM_ISPIF_CFG_EXT = IOWR('V', BASE_VIDIOC_PRIVATE + 1, ispif_cfg_data_ext)

# vfe

# buffer manager
VIDIOC_MSM_BUF_MNGR_GET_BUF = IOWR('V', BASE_VIDIOC_PRIVATE + 33, msm_buf_mngr_info)
VIDIOC_MSM_BUF_MNGR_PUT_BUF = IOWR('V', BASE_VIDIOC_PRIVATE + 34, msm_buf_mngr_info)
# VIDIOC_MSM_BUF_MNGR_BUF_DONE = IOWR('V', BASE_VIDIOC_PRIVATE + 35, msm_buf_mngr_info)
# VIDIOC_MSM_BUF_MNGR_CONT_CMD = IOWR('V', BASE_VIDIOC_PRIVATE + 36, msm_buf_mngr_main_cont_info)
# VIDIOC_MSM_BUF_MNGR_INIT = IOWR('V', BASE_VIDIOC_PRIVATE + 37, msm_buf_mngr_info)
# VIDIOC_MSM_BUF_MNGR_DEINIT = IOWR('V', BASE_VIDIOC_PRIVATE + 38, msm_buf_mngr_info)
# VIDIOC_MSM_BUF_MNGR_FLUSH = IOWR('V', BASE_VIDIOC_PRIVATE + 39, msm_buf_mngr_info)
# VIDIOC_MSM_BUF_MNGR_IOCTL_CMD = IOWR('V', BASE_VIDIOC_PRIVATE + 40, msm_camera_private_ioctl_arg)
