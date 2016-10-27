# -*- coding: utf-8 -*-
# 
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，
# 这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print add(-9,100,abs)

# 关于map reduce的相关使用
def f(x):
    return x * x

# map()函数接收两个参数，一个是函数，一个是序列，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce把一个函数作用在一个序列[x1, x2, x3...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 
print '###################reduce###################'
# 求和
x = range(0,101)
def myadd(x, y):
    return x + y
# 求积
def myplus(x, y):
    return x * y

print reduce(myadd, x)
print reduce(myplus, range(1,11))


print '###################'
# 练习题  名字规范化
testStr = ['adam', 'LISA', '']
def nameHandle(str):barT
    # for x in str:
    #     print x
    return str.title()

reStr = map(nameHandle, testStr)
print reStr



