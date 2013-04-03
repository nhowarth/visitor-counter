#!/usr/bin/python

import sys

with open(sys.argv[1], 'w') as f:
    f.write(str(int(sys.argv[2]) + 1))
