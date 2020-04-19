#!/usr/bin/env python
import sys
import os
sys.path.append(os.getcwd())
from v4l2 import *
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reading CalData from EEPROM.")
    parser.add_argument('-f', '--file', help='input filename', required=False, default='', type=str)
    parser.add_argument("name", help="EEPROM subdev name")
    args = parser.parse_args()
    devName = args.name
    inputFile = args.file

    # find all eeprom subdev
    medias = MediaDesc.find(type=MediaDesc.MSM_CONFIG)
    print(repr(medias))
    eeproms = []
    for m in medias:
        eeproms += EntityDesc.find(m, group_id=MSM_CAMERA_SUBDEV_EEPROM)
    print(repr(eeproms))

    # writing eeprom
    for e in eeproms:
        subdev = SubdevEEPROM(e)
        try:
            if subdev.readName() == devName:
                print("=======================================")
                print("writing eeprom: ")
                print(str(e))
                print("name = " + devName)
                print("=======================================")

                # read buffer from file
                fl = open(inputFile, "rb")
                buffer = fl.read()
                strBuffer = ''.join('0x{:02x} '.format(x) for x in buffer)
                print("buffer : " + strBuffer)
                calData = subdev.writeCalData(buffer)
        except Exception as e:
            print("err:%s"%(e))
