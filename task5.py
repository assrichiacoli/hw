def permutations(n):
    def gen_perm(n, prefix=[]):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for i in range(1, n + 1):
                if i not in prefix:
                    yield from gen_perm(n, prefix + [i])
    return list(gen_perm(n))


def correctbracketsequences(n):
    def bracket(n, prefix=''):
        if len(prefix) == 2 * n and (prefix.count('(')
                                     - prefix.count(')')) == 0:
            yield str(prefix)
        else:
            for i in ['(', ')']:
                if len(prefix + i) <= n * 2 and ((prefix + i).count('(') -
                                                 (prefix + i).count(')')) >= 0:
                    yield from bracket(n, prefix + i)
    return list(bracket(n))


def combinationswithrepeats(n, k):
    def gen_comb(n, k, prefix=[]):
        if len(prefix) == k:
            yield tuple(prefix)
        else:
            x = prefix[-1] if len(prefix) > 0 else 1
            for i in range(1, n + 1):
                if i >= x:
                    yield from gen_comb(n, k, prefix + [i])
    return list(gen_comb(n, k))


def unorderedpartitions(n):
    def genpart(n, prefix=[]):
        if sum(prefix) == n:
            yield tuple(prefix)
        else:
            x = prefix[-1] if len(prefix) > 0 else 1
            for i in range(1, n + 1):
                if sum(prefix + [i]) <= n and i >= x:
                    yield from genpart(n, prefix + [i])
    return list(genpart(n))
