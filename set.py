# -*- coding: utf-8 -*-
# set的相关使用   防止不存在的元素
# 创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
print xrange(0, 10), range(0, 10)
s = set(['A', 'B', 'C'])
s2 = set(['A','wetertw', 'B', 'C',141241234])
# print	'A' in s
print s2
print len(s2)



weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
#再判断输入是否有效，只需要判断该字符串是否在set中：
x = 'MON' # 用户输入的字符串
if x in weekdays:
    print 'input ko'
else:
    print 'input error'



# for name in weekdays:
# 	print name


#add remove
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']

# for ll in L:
# 	if ll in s:
# 		s.remove(ll)
# 	else:
# 		s.add(ll)
# print s


xsum = 0
xsbl = []
for x in range(0,101):
	xsbl.append(x*x)
print sum(xsbl)