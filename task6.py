import numpy as np

def getdimension(a):
    return a.ndim


def getdiagonal(a):
    return np.array([a[0,0],a[1,1]])


def cutarray(a, minvalue, maxvalue):
    for i in range(len(a)):
        if a[i] < minvalue:
            a[i] = minvalue
        elif a[i] > maxvalue:
            a[i] = maxvalue
    return a


def getmoments(a):
    return tuple([a.mean(), a.var()])


def getdotproduct(a,b):
    return a@b


def checkequal(a,b):
    return a == b


def comparewithnumber(a,bound):
    return a < bound


def matrixproduct(a,b):
    return a@b


def matrixdet(a):
    return a[0,0] * a[1,1] - a[1,0] * a[0,1]


def getones(n,k):
    a = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j - i == k:
                a[i,j] = 1.0
    return a