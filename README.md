v4l2-tools for qualcomm MSM8996

-----------------------------------

A tools to control v4l2 device for MSM8996 & APQ8096.

- subdevices iterations.
- CCI read and write.
- Camera OTP read and write.



### operations:

```
# python test/iterate_subdevice.py
==============================================================
/dev/media0
==============================================================

        id = 1
        name = /dev/video0
        type = 65537
        group_id = MSM_CAMERA_SUBDEV_ISPIF
        subdev_id = -1


        id = 2
        name = /dev/msm_cci
        type = 131072
        group_id = MSM_CAMERA_SUBDEV_CCI
        subdev_id = -1


        id = 3
        name = /dev/v4l-subdev0
        type = 131072
        group_id = MSM_CAMERA_SUBDEV_CSIPHY
        subdev_id = 0

...

 # python test/eeprom_read.py
=======================================
reading eeprom:

        id = 13
        name = /dev/v4l-subdev10
        type = 131072
        group_id = MSM_CAMERA_SUBDEV_EEPROM
        subdev_id = 2

=======================================
eeprom = eeprom1
cal Data len = 8192
cal Data: 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff 0xff ....
```

