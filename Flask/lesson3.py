#!/usr/bin/env python3

count=0


def set(x):
    global count
    count=x

def show():
    global count
    print(count)



set(5)
show()