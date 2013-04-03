#!/usr/bin/python

from datetime import datetime

hour = datetime.now().hour

if hour >= 0 and hour < 6:
    print 0
elif hour > 5 and hour < 12:
    print 1
elif hour > 11 and hour < 18:
    print 2
elif hour > 17 and hour < 24:
    print 3
