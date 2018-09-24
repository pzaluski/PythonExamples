#!/usr/bin/env python3

try:
    f = open("/etc/passwd")
    print(f)
except SyntaxError:
    print("Wrong file")


max_uid=0
for line in f:
    if line[0] == "#":
        continue
    splitted=line.split(":")
    if int(splitted[2]) > max_uid:
        max_uid=int(splitted[2])
print(max_uid)

#dupa zbita

