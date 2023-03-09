import numpy as np
import sys
from ctypes import *

def decrypt(v, k):
    v0 = c_uint32(v[0])
    v1 = c_uint32(v[1])
    sum = 0xC6EF3720
    delta = 0x9E3779B9
    k0 = k[0]
    k1 = k[1]
    k2 = k[2]
    k3 = k[3]
    for i in range(32):
        v1.value = v1.value - ((v0.value << 4) + k2) ^ (v0.value + sum) ^ ((v0.value >> 5) + k3)
        v0.value = v0.value - ((v1.value << 4) + k0) ^ (v1.value + sum) ^ ((v1.value >> 5) + k1)
        sum = sum - delta
    v[0] = v0
    v[1] = v1

    list_of_str_ints = [str(x) for x in v]
    print(str(0x2440951619))

v = [0xE3238557, 0x6204A1F8]
k = [0, 4, 5, 1]

decrypt(v, k)

