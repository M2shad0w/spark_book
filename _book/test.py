from collections import Counter
x = { 'apple': 1, 'banana': 2 }
y = { 'banana': 10, 'pear': 11 }
def f():
    i = 0
    while 1:
        if i == 10000:
            break
        for k, v in y.items():
            if k in x.keys():
                x[k] += v
            else:
                x[k] = v
        i += 1


def g():
    i = 0
    while 1:
        if i == 10000:
            break
        X,Y = Counter(x), Counter(y)
        z = X+Y
        i += 1

if __name__ == "__main__":
    import timeit
    tf = timeit.timeit(f, "from __main__ import f", number=10)
    tg = timeit.timeit(g, "from __main__ import g", number=10)
    print "f: %s\ng: %s" % (tf, tg)
