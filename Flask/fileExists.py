#!/usr/bin/env python3

import os


try:
   f = open("/etc/hosts2")
   f.read
   print(f)
   
except FileNotFoundError:
    print ("file not found") 
