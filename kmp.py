import numpy as np
import socket
import itertools
import functools


def digitsum(n):
    if n // 10 == 0:
        return n
    return digitsum(n % 10) + digitsum(n // 10)


def reversestring(s):
    if s == '':
        return ''
    return s[-1] + reversestring(s[:int(len(s))-1])


def ispalindrome(s):
    if len(s) == 1:
        return True
    else:
        for i in range(len(s)//2):
            if s[i] != s[-i - 1]:
                return False
    return True


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


def subpalindrome(s):
    a = ''
    maxlen = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if ispalindrome(s[i:j]):
                if len(s[i:j]) > maxlen:
                    a = s[i:j]
                    maxlen = len(s[i:j])
                elif j - i == maxlen:
                    if s[i:j] < a:
                        a = s[i:j]
    return a


def pascals():
    prev = []
    element = []
    for i in itertools.count():
        if i == 0:
            element = (1,)
        elif i == 1:
            element = (1, 1)
        else:
            element = [1]
            for k in range(len(prev) - 1):
                element.append(prev[k] + prev[k + 1])
            element += [1]
        prev = element
        yield tuple(element)


def fibonacci(n):
    return functools.reduce(lambda x, n: [x[1], x[0] + x[1]], range(n),
                            [0, 1])[0]


def spiral(n):
    i = 1
    a = [[0 for i in range(n)] for j in range(n)]
    for l in range(n):
        a[0][l] = i
        i += 1
    h1 = 1
    h2 = n - 1
    v1 = 0
    v2 = n - 1
    while i <= (n*n):
        # down
        for l in range(h2 - h1 + 1):
            a[h1 + l][v2] = i
            i += 1
        v2 -= 1

        # left
        for l in range(v2 - v1 + 1):
            a[h2][v2 - l] = i
            i += 1
        h2 -= 1

        # up
        for l in range(h2 - h1 + 1):
            a[h2 - l][v1] = i
            i += 1
        v1 += 1

        # right
        for l in range(v2 - v1 + 1):
            a[h1][v1 + l] = i
            i += 1
        h1 += 1
    return a


def brackets2(n, m):
    def bracket(n, m, prefix=''):
        strleft = prefix.count('(')
        strright = prefix.count(')')
        sqleft = prefix.count('[')
        sqright = prefix.count(']')
        straight = prefix.count('(') + prefix.count(')')
        square = prefix.count('[') + prefix.count(']')

        if straight == n*2 and square == m*2 and (strleft
                                                  - strright) == 0 and \
         (sqleft - sqright) == 0 and stack_check(prefix): #count object oh
            yield prefix
        else:
            for i in ['(', ')', '[', ']']:
                if (prefix + i).count('(') + \
                    (prefix + i).count(')') <= n * 2 and \
                     (prefix + i).count('[') + \
                      (prefix + i).count(']') <= m * 2 and \
                       ((prefix + i).count('(') - \
                        (prefix + i).count(')')) >= 0 and \
                         ((prefix + i).count('[') - \
                          (prefix + i).count(']')) >= 0:
                    yield from bracket(n, m, prefix + i)
    return bracket(n, m)


def stack_check(pref):
        stack = []
        for el in pref:
            n = len(stack)
            if n == 0:
                stack.append(el)
            elif stack[n - 1] == '(' and el == ')':
                stack.pop()
            elif stack[n - 1] == '['and el == ']':
                stack.pop()
            else:
                stack.append(el)
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10

    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'

    assert isIPv4('192.168.0.15')
    assert isIPv4('255.255.255.255')
    assert not isIPv4('555.555.555.555')
    assert not isIPv4('190+2.168.0.0')
    assert not isIPv4('abacaba')
    assert not isIPv4('')

    assert spiral(1) == [[1]]
    assert spiral(2) == [[1, 2],
                         [4, 3]]
    assert spiral(4) == [[1, 2, 3, 4],
                         [12, 13, 14, 5],
                         [11, 16, 15, 6],
                         [10, 9, 8, 7]]

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert list(brackets2(1, 0)) == ['()']
    assert list(brackets2(0, 1)) == ['[]']
    assert list(brackets2(1, 1)) == ['()[]', '([])', '[()]', '[]()']
    assert list(brackets2(3, 0)) == ['((()))', '(()())', '(())()', '()(())',
                                     '()()()']
    assert list(brackets2(2, 1)) == ['(())[]', '(()[])', '(([]))', '()()[]',
                                     '()([])', '()[()]', '()[]()', '([()])',
                                     '([]())', '([])()', '[(())]', '[()()]',
                                     '[()]()', '[](())', '[]()()']
