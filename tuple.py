# -*- coding: utf-8 -*-
# 但是tuple一旦初始化就不能修改
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
# 指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# the tuple

t = (1,2,3,4,34,4634563)
print t
# have only one element
tt = (123123)
print tt
ttt = (1234132,)
print ttt
xsb = (12,1231,['AAA','BBBB'])
L = xsb[2]
print L
#update the tuple
L[0] = 1234123
L[1] =9090
print xsb
# can't change the tuple
Li = ['132','fuck you']
notch = (12,Li)
print    notch
Li.append('xijiawei')
print    notch

