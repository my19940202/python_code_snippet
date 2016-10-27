# -*- coding: utf-8 -*-
# 

ra = range(1,11)
print ra

#生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
"""
for x in ra:
	L.append(x*x)
"""
# 可以简化为  [x * x for x in range(1, 11)]
L = [x * x for x in range(1, 11)]
L0 = [0 for x in range(1, 11)]
print L
print L0

# 同理可以搞出
M = []
for x in 'ABC':
	for n in 'xyz':
		M.append(x+n)

# 可以简化为 [m + n for m in 'ABC' for n in 'XYZ']

print M
