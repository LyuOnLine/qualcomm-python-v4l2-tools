#!/usr/bin/env python

# shortcut function for qualcomm V4L2 operations.
from .media import *
from .msmb_camera import *
from .msm_cam_sensor import *
from .msm_cci import *
from fcntl import ioctl
import os
import ctypes
import traceback


# Function for V4L2 prefinination
def GROUP_ID_STR(group_id):
    GROUPS = [
        "MSM_CAMERA_SUBDEV_CSIPHY",
        "MSM_CAMERA_SUBDEV_CSID",
        "MSM_CAMERA_SUBDEV_ISPIF",
        "MSM_CAMERA_SUBDEV_VFE",
        "MSM_CAMERA_SUBDEV_AXI",
        "MSM_CAMERA_SUBDEV_VPE",
        "MSM_CAMERA_SUBDEV_SENSOR",
        "MSM_CAMERA_SUBDEV_ACTUATOR",
        "MSM_CAMERA_SUBDEV_EEPROM",
        "MSM_CAMERA_SUBDEV_CPP",
        "MSM_CAMERA_SUBDEV_CCI",
        "MSM_CAMERA_SUBDEV_LED_FLASH",
        "MSM_CAMERA_SUBDEV_STROBE_FLASH",
        "MSM_CAMERA_SUBDEV_BUF_MNGR",
        "MSM_CAMERA_SUBDEV_SENSOR_INIT",
        "MSM_CAMERA_SUBDEV_OIS",
        "MSM_CAMERA_SUBDEV_FLASH",
        "MSM_CAMERA_SUBDEV_IR_LED",
        "MSM_CAMERA_SUBDEV_IR_CUT",
        "MSM_CAMERA_SUBDEV_EXT",
    ]
    return GROUPS[group_id]


class MediaDesc(object):
    TYPE_NON_MSM, MSM_CAMERA, MSM_CONFIG = range(3)
    MODELS = [
        # non-msm
        {
            "type": TYPE_NON_MSM,
            "model": None
        },
        # msm-camera
        {
            "type": MSM_CAMERA,
            "model": b"msm_camera"
        },
        # msm-config
        {
            "type": MSM_CONFIG,
            "model": b"msm_config"
        }
    ]

    MEDIA_MAXIMUM = 10

    def __init__(self, fd=-1):
        self.fd = fd

    def __del__(self):
        os.close(self.fd)

    @classmethod
    def _getMODELS(cls, type):
        for m in cls.MODELS:
            if m['type'] == type:
                return m
        return None

    @classmethod
    def all(cls):
        medias = []
        for i in range(cls.MEDIA_MAXIMUM):
            try:
                mediaFd = os.open("/dev/media%d" % (i), os.O_RDWR)
                medias.append(MediaDesc(mediaFd))
            except:
                # iterate end
                break
        return medias

    @classmethod
    def find(cls, type=MSM_CONFIG):
        strModel = cls._getMODELS(type)

        medias = cls.all()
        mediaFilter = []
        for m in medias:
            _media = media_device_info()
            ioctl(m.fd, MEDIA_IOC_DEVICE_INFO, _media)
            if strModel and _media.model != strModel:
                mediaFilter.append(m)

        return mediaFilter


class EntityDesc(object):
    # entity_desc:
    #     DataType: media_entity_desc(a ctypes structure)
    def __init__(self, entity_desc):
        # media_entity_desc
        self.id = entity_desc.id
        self.name = '/dev/' + entity_desc.name.decode('ascii')
        # MEDIA_ENT_T_V4L2_SUBDEV
        self.type = entity_desc.type
        # MSM_CAMERA_SUBDEV_SENSOR
        self.group_id = entity_desc.group_id
        self.revision = entity_desc.revision
        self.flags = entity_desc.flags
        # self.subdev_id = -1
        self.subdev_id = self._getSubdevId()

    def __str__(self):
        return '''
        id = {id}
        name = {name}
        type = {type}
        group_id = {group_id}
        subdev_id = {subdev_id}
        '''.format(id=self.id, name=self.name, type=self.type, group_id=GROUP_ID_STR(self.group_id),
                   subdev_id=self.subdev_id)

    def _getSubdevId(self):
        SUBDEVS = [MSM_CAMERA_SUBDEV_ACTUATOR, MSM_CAMERA_SUBDEV_EEPROM, MSM_CAMERA_SUBDEV_LED_FLASH,
                   MSM_CAMERA_SUBDEV_STROBE_FLASH, MSM_CAMERA_SUBDEV_CSIPHY, MSM_CAMERA_SUBDEV_CSID]

        if self.type != MEDIA_ENT_T_V4L2_SUBDEV:
            return -1
        if self.group_id not in SUBDEVS:
            return -1
        subdev_id = ctypes.c_uint32()

        try:
            fd = os.open(self.name, os.O_RDWR)
            ioctl(fd, VIDIOC_MSM_SENSOR_GET_SUBDEV_ID, subdev_id)
            os.close(fd)
            return subdev_id.value
        except:
            # traceback.print_exc()
            # fix Qualcomm bug: /dev/msm_cci iterate as MSM_CAMERA_SUBDEV_CSIPHY
            return -1

    @classmethod
    def all(cls, media):
        id = 1
        entities = []
        while True:
            try:
                _entity = media_entity_desc()
                _entity.id = id
                ioctl(media.fd, MEDIA_IOC_ENUM_ENTITIES, _entity)
                entities.append(EntityDesc(_entity))
                id += 1
            except:
                # traceback.print_exc()
                break
        return entities

    @classmethod
    def find(cls, media, group_id=MSM_CAMERA_SUBDEV_CSIPHY, subdev_id=-1):
        id = 1
        devName = []
        while True:
            try:
                _entity = media_entity_desc()
                _entity.id = id
                ioctl(media.fd, MEDIA_IOC_ENUM_ENTITIES, _entity)
                # wrapper as EntityDesc class.
                ent = EntityDesc(_entity)
                if _entity.type == (MEDIA_ENT_T_V4L2_SUBDEV) and _entity.group_id == group_id:
                    if subdev_id != -1:
                        if ent.subdev_id == subdev_id:
                            devName.append(ent)
                    else:
                        devName.append(ent)
                id += 1
            except:
                # iteration end
                break
        return devName


# EEPROM subdev
class SubdevEEPROM(object):
    def __init__(self, entityDesc):
        self.devname = entityDesc.name
        self.fd = os.open(self.devname, os.O_RDWR)

    def __del__(self):
        if self.fd:
            os.close(self.fd)

    # read eeprom name
    def readName(self):
        cmd = msm_eeprom_cfg_data()
        cmd.cfgtype = CFG_EEPROM_GET_INFO
        ioctl(self.fd, VIDIOC_MSM_EEPROM_CFG, cmd)
        return cmd.cfg.eeprom_name.decode("ascii")

    def readCalData(self):
        cmd = msm_eeprom_cfg_data()
        cmd.cfgtype = CFG_EEPROM_GET_CAL_DATA
        ioctl(self.fd, VIDIOC_MSM_EEPROM_CFG, cmd)
        dataLen = cmd.cfg.get_data.num_bytes
        buffer = (ctypes.c_uint8 * dataLen)()
        cmd.cfgtype = CFG_EEPROM_READ_CAL_DATA
        cmd.cfg.read_data.dbuffer = buffer
        cmd.cfg.read_data.num_bytes = dataLen
        ioctl(self.fd, VIDIOC_MSM_EEPROM_CFG, cmd)
        return bytearray([d for d in buffer])

        # not support by msm_eeprom_config32
        # def readContent(self):
        #     cmd = msm_eeprom_cfg_data()
        #     cmd.cfgtype = CFG_EEPROM_GET_MM_INFO
        #     cmd.cfg.get_cmm_data.cmm_support = 0
        #     cmd.cfg.get_cmm_data.cmm_compression = 0
        #     cmd.cfg.get_cmm_data.cmm_size = 0
        #     ioctl(self.fd, VIDIOC_MSM_EEPROM_CFG, cmd)
        #     print(repr(cmd.cfg.get_cmm_data.cmm_size))

    def writeCalData(self, buffer):
        c_buffer = (ctypes.c_uint8 * len(buffer))()
        for i, d in enumerate(buffer):
            c_buffer[i] = d
        cmd = msm_eeprom_cfg_data()
        cmd.cfg.write_data.num_bytes = len(buffer)
        cmd.cfg.write_data.dbuffer = c_buffer
        cmd.cfgtype = CFG_EEPROM_WRITE_DATA
        ioctl(self.fd, VIDIOC_MSM_EEPROM_CFG, cmd)


# CCI subdev
# EEPROM subdev
class SubdevCCI(object):
    CCI_MASTER_0, CCI_MASTER_1 = range(2)

    def __init__(self, entityDesc):
        self.devname = entityDesc.name
        self.fd = os.open(self.devname, os.O_RDWR)

    def __del__(self):
        if self.fd:
            os.close(self.fd)

    # read eeprom name
    def init(self, sid, cci=MASTER_0, retries=3, i2c_freq=I2C_STANDARD_MODE):
        self.cmd = msm_camera_cci_ctrl()
        self.cci_info = msm_camera_cci_client()
        self.cci_info.cci_i2c_master = cci
        self.cci_info.sid = sid
        self.cci_info.i2c_freq_mode = i2c_freq
        self.cci_info.retries = retries
        self.cmd.cci_info = ctypes.pointer(self.cci_info)

        self.cmd.cmd = MSM_CCI_INIT
        # print(repr(self.cmd))
        # print(repr(ctypes.addressof(self.cmd)))
        # buf = ctypes.cast(ctypes.pointer(self.cmd),ctypes.POINTER(ctypes.c_uint8))
        # for i in range(ctypes.sizeof(self.cmd)):
        #     print("%x"%(buf[i]))
        # print("cci_ctl size=%d"%(ctypes.sizeof(ctypes.pointer(self.cmd))))

        ioctl(self.fd, VIDIOC_MSM_CCI_CFG, self.cmd)

    def release(self):
        self.cmd.cmd = MSM_CCI_RELEASE
        ioctl(self.fd, VIDIOC_MSM_CCI_CFG, self.cmd)

    def read(self, addr, num_byte, addr_type=MSM_CAMERA_I2C_WORD_ADDR):
        c_buffer = (ctypes.c_uint8 * num_byte)()
        self.cmd.cmd = MSM_CCI_I2C_READ
        self.cmd.cfg.cci_i2c_read_cfg.addr = addr
        self.cmd.cfg.cci_i2c_read_cfg.addr_type = addr_type
        self.cmd.cfg.cci_i2c_read_cfg.num_byte = num_byte
        self.cmd.cfg.cci_i2c_read_cfg.data = c_buffer
        ioctl(self.fd, VIDIOC_MSM_CCI_CFG, self.cmd)
        # return c_buffer.decode('ascii')
        return [c_buffer[i] for i in range(num_byte)]


# csiphy subdev
class SubdevCSIPhy(object):
    def __init__(self, entityDesc):
        self.devname = entityDesc.name
        self.fd = os.open(self.devname, os.O_RDWR)

    def __del__(self):
        if self.fd:
            os.cloase(self.fd)

    def open(self):
        cfg = csiphy_cfg_data()
        cfg.cfgtype = CSIPHY_INIT
        ioctl(self.fd, VIDIOC_MSM_CSIPHY_IO_CFG, cfg)

    def config(self, csid_core, lane_mask, lane_cnt, csiphy_clk, combo_mode=0, csi_3phase=0):
        cfg = csiphy_cfg_data()
        cfg.cfgtype = CSIPHY_CFG
        param = msm_camera_csiphy_params()
        param.csid_core = csid_core
        param.csiphy_clk = csiphy_clk
        param.lane_mask = lane_mask
        param.lane_cnt = lane_cnt
        param.combo_mode = combo_mode
        param.csi_3phase = csi_3phase
        cfg.cfg.csiphy_params = ctypes.pointer(param)
        ioctl(self.fd, VIDIOC_MSM_CSIPHY_IO_CFG, cfg)

    def close(self, lane_mask):
        cfg = csiphy_cfg_data()
        cfg.cfgtype = CSIPHY_RELEASE
        param = msm_camera_csi_lane_params()
        param.csi_lane_mask = lane_mask
        cfg.cfg.csi_lane_params = ctypes.pointer(param)
        ioctl(self.fd, VIDIOC_MSM_CSIPHY_IO_CFG, cfg)


# csid subdev
class SubdevCSID(object):
    def __init__(self, entityDesc):
        self.devname = entityDesc.name
        self.fd = os.open(self.devname, os.O_RDWR)

    def __del__(self):
        if self.fd:
            os.close(self.fd)

    def open(self):
        cfg = csid_cfg_data()
        cfg.cfgtype = CSID_INIT
        ioctl(self.fd, VIDIOC_MSM_CSID_IO_CFG, cfg)

    def config(self, csiphy_id, lane_cnt, lane_assign, csi_clk=0):
        cfg = csid_cfg_data()
        cfg.cfgtype = CSID_CFG
        csid_param = msm_camera_csid_params()
        csid_param.phy_sel = csiphy_id
        csid_param.lane_cnt = lane_cnt
        csid_param.lane_assign = lane_assign
        csid_param.csi_clk = csi_clk
        print("pointer:"+repr(ctypes.pointer(csid_param)) + "  size:" +repr(ctypes.sizeof(csid_param)))
        cfg.cfg.csid_param = ctypes.pointer(csid_param)
        ioctl(self.fd, VIDIOC_MSM_CSID_IO_CFG, cfg)
        csid_param.csi_clk = 0

    def close(self):
        cfg = csid_cfg_data()
        cfg.cfgtype = CSID_RELEASE
        ioctl(self.fd, VIDIOC_MSM_CSID_IO_CFG, cfg)
