# -*- coding: utf-8 -*-
# 记录一些常用的函数

# 数学相关
print abs(-110)
print round(23.331233, 2)

# 类型转化
print int(23.331233)
print float(23)
print str(241234.1123)


# 是否是数字
str0 = '14124'
str1 = '141.24'
str2 = '12afd389ad'
print str0, 'isdigit', str0.isdigit()
print str1, 'isdigit', str1.isdigit()
print str2, 'isdigit', str2.isdigit()


# 变量类型
va = [1,2,3,4]
vb = (12,'123',[123,123,90])
vc = set(['A', 'B', 'C'])
vd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print type(va)
print type(vb)
print type(vc)
print type(vd)
