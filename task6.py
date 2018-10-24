import numpy as np


def getdimension(a):
    return a.ndim


def getdiagonal(a):
    return a.diagonal()


def cutarray(a, minvalue, maxvalue):
    a[a < minvalue] = minvalue
    a[a > maxvalue] = maxvalue
    return a


def getmoments(a):
    return tuple([a.mean(), a.var()])


def getdotproduct(a, b):
    return a@b


def checkequal(a, b):
    return a == b


def comparewithnumber(a, bound):
    return a < bound


def matrixproduct(a, b):
    return a@b


def matrixdet(a):
    return np.linalg.det(a)


def getones(n, k):
    return np.eye(n, n, k)
