import numpy as np
import socket

def digitsum(n):
    if n // 10 == 0:
        return n
    return digitsum(n % 10) + digitsum(n // 10)


def valuesunion(*dicts): 
    a = set()
    for dic in dicts:
        for item in dic.values():
            a.add(item)
    return a


def popcount(n):
    a = int(np.binary_repr(n), 10)
    return digitsum(a)


def powers(n, m):
    a = list(range(1, n + 1))
    print(a)
    b = []
    for i in a:
        b.append((i ** i) % m)
    return dict(zip(a, b))


def isIPv4(s):
    try:
        socket.inet_aton(s)
        return True
    except socket.error:
        return False
