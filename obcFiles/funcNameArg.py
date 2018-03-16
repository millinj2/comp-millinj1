#!/usr/bin/python

#ref : http://www.python-course.eu/sys_module.php

import sys

# it's easy to print this list of course:
print "  Your command line was :", sys.argv

# or it can be iterated via a for loop:
for i in range(len(sys.argv)):
    if i == 0:
        print "Function name: %s" % sys.argv[0]
    else:
        print "%d. argument: %s" % (i,sys.argv[i])

