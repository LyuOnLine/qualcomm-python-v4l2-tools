#!/usr/bin/env python
import sys
import os
sys.path.append(os.getcwd())
from v4l2 import *

if __name__ == "__main__":
    medias = MediaDesc.all()
    for i, m in enumerate(medias):
        print("==============================================================")
        print("/dev/media%d" % (i))
        print("==============================================================")
        entities = EntityDesc.all(m)
        for e in entities:
            print(str(e))
