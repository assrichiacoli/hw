def unique(e):
    a = []
    for i in e:
        if i not in a:
            a.append(i)
            a.sort()
    return a


def transposeDict(d):
    a = d.keys()
    b = d.values()
    new = dict(zip(b, a))
    return new


def mex(e):
    k = 1
    while k in e:
        k += 1
    else:
        return(k)


def frequencyDict(s):
    a = []
    b = []
    for i in s:
        if i not in a:
            a.append(i)
    for j in a:
        c = s.count(j)
        b.append(c)
    new = dict(zip(a, b))
    return new


if __name__ == '__main__':
    assert unique([1, 2, 1, 3]) == [1, 2, 3]
    assert unique({5, 1, 3}) == [1, 3, 5]
    assert unique('adsfasdf') == ['a', 'd', 'f', 's']
    assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}
    assert transposeDict({1: 1}) == {1: 1}
    assert transposeDict({}) == {}
    assert mex([1, 2, 3]) == 4
    assert mex(['asdf', 123]) == 1
    assert mex([0, 0, 1, 0]) == 2
    assert frequencyDict('') == {}
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1}
    print('Tests were executed successfully')

