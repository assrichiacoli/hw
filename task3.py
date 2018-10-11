import itertools
from functools import reduce
from operator import mul


def squares(a):
    for i in a:
        yield i ** 2


def repeatntimes(elems, n):
    for i in itertools.tee(elems, n):
        yield from i


def evens(x):
    for i in itertools.count(x):
        if i % 2 == 0:
            yield i


def digitsumdiv(p):
    for i in itertools.count(1):
        if sum(int(digit) for digit in str(i)) % p == 0:
            yield i


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.swapcase(), s)


def productif(elems, conds):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] is True else
                                          1, zip(elems, conds)), 1)
