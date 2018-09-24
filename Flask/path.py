#!/usr/bin/env python3
import sys
import os.path
s=10
print(sys.argv[0])
print(os.path.abspath(sys.argv[0]))
print(os.path.isfile("test.txt"))
print(os.walk(os.path.abspath(sys.argv[0])))

