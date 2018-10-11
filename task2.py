def listToString(a):
    return str(a)


def addBorder(a):
    if a == []:
        return print('Can\'t add border to an empty list!')
    else:
        o = '-'
        b = o * int(len(a[1]))
        border = ['+' + b + '+']
        for i in a:
            border.append('|' + i + '|')
        border.append('+' + b + '+')
    return border


def shorting(e):
    a = []
    for i in e:
        if len(i) <= 10:
            a.append(i)
        else:
            a.append(i[0] + str(int(len(i) - 2)) + i[-1])
    return a


def competition(e, k):
    a = []
    for ind, i in enumerate(e):
        if ind <= k:
            a.append(i)
        elif i == a[-1]:
            a.append(i)
    b = []
    for item in a:
        if item != 0:
            b.append(item)
    return len(b)


def goodPairs(a, b):
    n = []
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                s = i ** 2 + j ** 2
                n.append(s)
    a = list(set(n))
    a.sort()
    return a


def makeShell(n):
    a = []
    o = [0]
    k = 1
    while k <= n:
        a.append(o*k)
        k += 1
    m = n - 1
    while m <= n and m > 0:
        a.append(o*m)
        m -= 1
        assert listToString([]) == "[]"
    return a


if __name__ == '__main__':
    assert listToString([1, 2, 3]) == "[1, 2, 3]"
    assert listToString([-5]) == "[-5]"
    assert competition([5, 4, 3, 2, 1], 2) == 3
    assert competition([1, 0, 0, 0], 3) == 1
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6
    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180]
    assert goodPairs([2], [2]) == [8]
    assert goodPairs([7, 8, 9], [5, 3, 2]) == []
    assert makeShell(1) == [[0]]
    assert makeShell(2) == [[0], [0, 0], [0]]
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]]
    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+']
    assert shorting(['word', 'localization', 'internationalization',
                     'pneumonoultramicroscopicsilicovolcanoconiosis'])\
        == ['word', 'l10n', 'i18n', 'p43s']
    print('All tests were executed successfully!')
