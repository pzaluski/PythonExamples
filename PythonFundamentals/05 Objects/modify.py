#!/usr/bin/env python3

m = [9,15,32]

def modify(k):
    k.append(39)
    print("k =", k)
    return k

k = modify(m)[:]
print(m , k)