#!/usr/bin/python

with open('0-5.txt', 'r') as f:
    print "</br>Number of visitors between midnight and 6am:  "
    print f.readline().strip()
with open('6-11.txt', 'r') as f:
    print "</br>Number of visitors between 6am and noon:  "
    print f.readline().strip()
with open('12-17.txt', 'r') as f:
    print "</br>Number of visitors between noon and 6pm:  "
    print f.readline().strip()
with open('18-23.txt', 'r') as f:
    print "</br>Number of visitors between 6pm and midnight:  "
    print f.readline().strip()
