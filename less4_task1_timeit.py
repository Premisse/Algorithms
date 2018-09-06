import timeit

def invert(number, rebmun=[]):
    while number > 0:
        rebmun.append(number % 10)
        number //= 10

    return rebmun

# результаты проверки через timeit

# 100 loops, best of 5: 1.23 usec per loop   --- invert(256)
# 100 loops, best of 5: 2.94 usec per loop   --- invert(5689754)
# 100 loops, best of 5: 8.35 usec per loop   --- invert(568975548792254)




