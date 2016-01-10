# coding:utf-8

import sys
print sys.argv

if len(sys.argv) > 1:
    if sys.argv[1] == "init":
        print "init database"
    elif sys.argv[1] == "delete":
        print "stop"
else:
    print "no arguments"