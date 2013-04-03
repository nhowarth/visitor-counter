#!/usr/bin/python

import sys

if sys.argv[1] == '0':
    with open("0-5.txt", 'w') as f:
        f.write(str(int(sys.argv[2]) + 1))
elif sys.argv[1] == '1':
    with open('6-11.txt', 'w') as f:
        f.write(str(int(sys.argv[2]) + 1))
elif sys.argv[1] == '2':
    with open('12-17.txt', 'w') as f:
        f.write(str(int(sys.argv[2]) + 1))
elif sys.argv[1] == '3':
    with open('18-23.txt', 'w') as f:
        f.write(str(int(sys.argv[2]) + 1))
