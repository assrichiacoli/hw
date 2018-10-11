import itertools
from functools import reduce
from operator import mul


def filter(predicate, elements):
    for x in elements:
        if predicate(x):
            yield x


def squares(a):
    for i in a:
        yield i ** 2


def repeatntimes(elems, n):
    yield elems * n


def evens(x):
    for i in itertools.count(x):
        if i % 2 == 0:
            yield i


def digitsumdiv(p):
    for i in itertools.count(1):
        if sum(int(digit) for digit in str(i)) % p == 0:
            yield sum(int(digit) for digit in str(i))


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.swapcase(), s)


def productif(elems, conds):
    a = list(zip(elems, conds))
    b = list(filter(lambda x: x[1] is True, a))
    c = []
    for i in b:
        c.append(i[0])
    return reduce(mul, c, 1)
