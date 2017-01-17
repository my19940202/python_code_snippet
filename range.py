# -*- coding: utf-8 -*-
# range函数的使用

#代表从1到5(不包含5)
print range(5) #[0, 1, 2, 3, 4]
print range(1,5) #[1, 2, 3, 4]
print range(10,20) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
print range(0,100,10) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

L = []
#生成[1x1, 2x2, 3x3, ..., 10x10]
"""
for x in ra:
	L.append(x*x)
"""
# 可以简化为 
L = [x * x for x in range(1, 11)]
print L

# 全部一样的元素
L0 = [0 for x in range(1, 11)]
print L0

# 同理可以搞出
M = []
for x in 'ABC':
	for n in 'xyz':
		M.append(x+n)
# 可以简化为 [m + n for m in 'ABC' for n in 'XYZ']
print M
