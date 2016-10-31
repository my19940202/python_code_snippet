# -*- coding: utf-8 -*-
# 斐波那契的生成
# 
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

# fib(6)


# 改进后的fib
def yfib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# b = yfib(6)
# print b


# 没有搞懂继续往下
# 
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3

o = odd()
o.next()
o.next()
o.next()
# 没有yield了 就停止了
o.next()
