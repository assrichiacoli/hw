def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def recurrent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n % 2 == 0:
        return recurrent(n/2)
    return recurrent((n - 1)/2) + recurrent(((n - 1)/2)+1)


def digitsum(n):
    if n // 10 == 0:
        return n  
    return digitsum(n % 10) + digitsum(n//10)


def reversestring(s):
    if s == '':
        return ''
    return s[-1] + reversestring(s[:int(len(s))-1])


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


def drawborders(n):
    if n == 1:
        return ['+']
    elif n == 2:
        return ['++', '++']
    o = '-'
    b = o * (n - 2)
    c = ['+' + b + '+']
    new = ['|' + i + '|' for i in drawborders(n - 2)]
    return c + new + c


def genbinarystrings(n):
    def gen(n, prefix =''):
        if len(prefix) == n:
            yield prefix
        else:
            for i in range(2):
                yield from gen(n, prefix + str(i))
    return list(gen(n))


def istwopower(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif n % 2 != 0:
        return False
    return istwopower(n / 2)


def abacaba(n):
    if n == 1:
        return [1]
    return abacaba(n-1) + [n] + abacaba(n-1)
    
    
def parentheses(s):
    if len(s) <= 2:
        return '(' + s + ')' 
    return '(' + s[0] + parentheses(s[1:-1]) + s[-1] + ')'   
 

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
if __name__ == '__main__':
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24
    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    assert recurrent(2) == 1
    assert recurrent(3) == 2
    assert recurrent(5) == 3
    assert recurrent(7) == 3
    assert digitsum(0) == 0
    assert digitsum(123) == 6
    assert digitsum(192837465) == 45
    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') == 'fdsa'
    assert reversestring('abacaba') == 'abacaba'
    assert ackermann(0, 10) == 11
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(2, 5) == 13
    assert ackermann(3, 3) == 61
    assert drawborders(1) == ['+']    
    assert drawborders(2) == ['++', '++']
    assert drawborders(3) == ['+-+', '|+|', '+-+']                   
    assert drawborders(4) == ['+--+', '|++|', '|++|', '+--+']                   
    assert drawborders(5) == ['+---+', '|+-+|', '||+||', '|+-+|', '+---+']
    assert genbinarystrings(0) == ['']
    assert genbinarystrings(1) == ['0', '1']
    assert genbinarystrings(2) == ['00', '01', '10', '11']
    assert genbinarystrings(3) == ['000', '001', '010', '011', '100', '101', 
    '110', '111']
    assert istwopower(-5) == False
    assert istwopower(0) == False
    assert istwopower(1) == True
    assert istwopower(2) == True
    assert istwopower(4) == True
    assert istwopower(67) == False
    assert istwopower(1024) == True
    assert abacaba(1) == [1]
    assert abacaba(2) == [1, 2, 1]
    assert abacaba(3) == [1, 2, 1, 3, 1, 2, 1]
    assert abacaba(4) == [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    assert parentheses('example') == '(e(x(a(m)p)l)e)'
    assert parentheses('odd') == '(o(d)d)'
    assert parentheses('even') == '(e(ve)n)'
    assert gcd(1, 5) == 1
    assert gcd(4, 6) == 2
    assert gcd(18, 12) == 6
    assert gcd(283918822, 595730520) == 22
