# -*- coding: utf-8 -*-
# 各种类型数据的遍历
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key, d[key]

print '#########################'
# Python内置的enumerate函数可以把一个list变成索引-元素对
# 这样就可以在for循环中同时迭代索引和元素本身
li = ['a', 'b', 'c', 'd', 'e']
for i, value in enumerate(li):
	print i, value


print '循环中 引用2变量'
tu = [(1,2),(90,98),(78,65)]
for x,y in tu:
	print x,y
	