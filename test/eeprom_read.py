#!/usr/bin/env python
import sys
import os
sys.path.append(os.getcwd())
from v4l2 import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reading CalData from EEPROM.")
    parser.add_argument('-f', '--file', help='output filename', required=False, default='', type=str)
    args = parser.parse_args()
    outputFile = args.file

    # find all eeprom subdev
    medias = MediaDesc.find(type=MediaDesc.MSM_CONFIG)
    print(repr(medias))
    eeproms = []
    for m in medias:
        eeproms += EntityDesc.find(m, group_id=MSM_CAMERA_SUBDEV_EEPROM)
    print(repr(eeproms))

    # reading eeprom
    for e in eeproms:
        print("=======================================")
        print("reading eeprom: ")
        print(str(e))
        print("=======================================")
        try:
            subdev = SubdevEEPROM(e)
            name = subdev.readName()
            print("eeprom = %s" % (name))
            calData = subdev.readCalData()
            print("cal Data len = %d" % (len(calData)))
            strCalData = ''.join('0x{:02x} '.format(x) for x in calData)
            print("cal Data: " + strCalData)

            # output to file
            if outputFile != "":
                fileName = outputFile + "_" + subdev.readName()
                with open(fileName, "wb+") as fl:
                    fl.write(calData)
        except Exception as e:
            print("reading eeprom fail!err=%s" % (repr(e)))
