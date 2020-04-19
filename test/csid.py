#!/usr/bin/env python
import sys
import os
sys.path.append(os.getcwd())
from v4l2 import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="csiphy ioctl.")
    parser.add_argument('-i', '--dev_id', help='device id', required=False, type=int)
    parser.add_argument('-c', "--csid_core", help="csid_core", required=False, type=int)
    parser.add_argument('-m', "--lane_mask", help="lane_mask", required=False, default=0xff, type=int)
    parser.add_argument('-l', "--lane_count", help="lane count", required=False, default=4, type=int)
    parser.add_argument('-f', "--csiphy_clk", help="csiphy_clk", required=False, default=0, type=int)

    parser.add_argument("command", help="commands: [init, config, release]")
    args = parser.parse_args()
    dev_id = args.dev_id
    command = args.command

    # find all eeprom subdev
    medias = MediaDesc.find(type=MediaDesc.MSM_CONFIG)
    csiphy = []
    for m in medias:
        csiphy += EntityDesc.find(m, group_id=MSM_CAMERA_SUBDEV_CSIPHY, subdev_id=dev_id)
    print(str(csiphy[0]))
    dev = SubdevCSIPhy(csiphy[0])


    if command == "init":
        dev.open()
    elif command == "config":
        dev.config(csid_core=args.csid_core, lane_mask=args.lane_mask, lane_cnt=args.lane_count,
                      csiphy_clk=args.csiphy_clk)
    elif command == "release":
        dev.close(lane_mask=args.lane_mask)
    print("[OK]")
