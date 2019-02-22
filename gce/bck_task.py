#!/usr/bin/env/ python

import time
import os
import sys
import logging

log = logging.getLogger(__name__)

try:
    os.mkdir('/tmp/foo')
except:
    pass

for x in range(20):
    print "Doing work... %s" % x
    try:
        os.mkdir('/tmp/foo/%s' % x)
    except:
        pass
    time.sleep(.5)

sys.exit(0)
