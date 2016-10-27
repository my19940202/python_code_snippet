# -*- coding: utf-8 -*-
# str slice
# 从索引0开始取，直到索引3为止，
# 但不包括索引3。即索引0，1，2，正好是3个元素。
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack', 'Funk', 'Zara']
print len(L)
print L[0:3]
print L[:3]
print L[1:3]
print L[2:3]

print '支持倒数的截取'
print L[-1]
print L[-2:]
print L[-2:-1]

print '#########################'

M = range(100)
print M
print M[:10]
print M[-10:]
print M[10:20]
print '前10个 每两个取一次'
print M[:10:2]
#[0, 2, 4, 6, 8]
print 'all numbers get per 5'
print M[::5]

print 'copy the list'
print M[:]

print '#########################'
# tuple 和 string 也可以像上面一样操作
s = 'asdkaad8798asd79asdjnm1b3mn1b3iu'
print s[:], s[::5]
tu = (12,3,4,5234,123,12,124,5)
print tu[:], tu[::2]
