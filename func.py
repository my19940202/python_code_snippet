# -*- coding: utf-8 -*-
import math
def funcxsb(a,b,c):
	d = a + b + c 
	return d
# print funcxsb(1,2,333)


# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# print fact(5)

# 空函数
def fuck(log):
	pass
	# print(log)
# fuck('dict.py')



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print my_abs('123123')


# xy坐标点的移动
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 1.4142, -math.pi / 4);
# print x,y


# 求解一个一元二次方程
# ax2 + bx + c = 0
def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return x1, x2

# print quadratic(1, 3, -4)


# 求x 的 n次方  还有默认参数的使用
def power(x, n = 10):
	product = 1
	while n > 0:
		product = product * x
		n = n - 1
	return product

# print power(2,10), power(2,20), power(2)


def enroll(name, gender, age=6, city='Beijing'):
    print	'name:', name
    print	'gender:', gender
    print	'age:', age
    print	'city:', city

# enroll('xsb', 'F')


# 默认参数的一个坑

def add_end(L=[]):
    L.append('END')
    return L
print add_end()
print add_end()
print add_end()

# 解决办法
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print	add_end2()
print	add_end2()
print	add_end2()
