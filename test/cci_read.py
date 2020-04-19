#!/usr/bin/env python
import sys
import os
sys.path.append(os.getcwd())
from v4l2 import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reading CalData from EEPROM.")
    parser.add_argument('master', help="cci master", type=int)
    parser.add_argument('slave', help="slave address(8bit)", type=str)
    parser.add_argument('address', help="register address", type=str)
    parser.add_argument('len', help="read length", type=str)
    parser.add_argument('-t', '--address_type', help='address type(1:byte,2:word,3:3B)', required=False, default=2,
                        type=int)
    args = parser.parse_args()
    master = args.master
    slave = args.slave
    if slave.startswith("0x"):
        slave = int(slave, 16)
    else:
        slave = int(slave)
    slave = slave // 2
    address = args.address
    if address.startswith("0x"):
        address = int(address, 16)
    else:
        address = int(address)

    length = args.len
    if length.startswith("0x"):
        length = int(length, 16)
    else:
        length = int(length)
    addressType = args.address_type

    print("====================================================")
    print("read dev(0x%x) addr=0x%x len=%d @ master_%d" % (slave, address, length, master))
    print("====================================================")

    # find cci
    medias = MediaDesc.find(type=MediaDesc.MSM_CONFIG)
    ccis = []
    # workaround for qualcomm bug, group_id of CCI is MSM_CAMERA_SUBDEV_CSIPHY.
    # for m in medias:
    #     ccis += EntityDesc.find(m, group_id=MSM_CAMERA_SUBDEV_CSIPHY)
    # cci = None
    # for c in ccis:
    #     if c.name == "/dev/msm_cci":
    #         cci = c
    for m in medias:
        ccis += EntityDesc.find(m, group_id=MSM_CAMERA_SUBDEV_CCI)
    cci = ccis[0]
    print(repr(cci))

    if cci:
        subdev = SubdevCCI(cci)
        subdev.init(slave, cci=master)
        result = subdev.read(address, length, addr_type=addressType)
        print(repr(result))
        subdev.release()
