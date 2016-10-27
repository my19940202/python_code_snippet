# -*- coding: utf-8 -*-
# 加了上面这句注释 python 才会支持 u'''中文的输出'''
# 
#this is a comment of single line
'''

this a comment of a multical line

'''
print    r'\(~_~)/ \(~_~)/'
print    "fuck you all the time"

# unicode string
print u'''草泥马哟'''
print u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''



#整数相除还是整数   和c基本一样吧
print 2.5 + 10 / 4
print 2.5 + 10 / 4.0
#关于布尔值
a = 'python'
print 'hello,', a or 'world'
b = ''
print 'hello,', b or 'world'

b = True
print b and 'a=T' or 'a=F'

# list 这种数据类型
# l(-1) l(-2) refer to the last one and the one next to last 
l = ["fuck  you", True, 12341341]
print	l
#append()
l.append('my name is last')
print l
l.insert(0,'my name is first')
print l
#the same to the pop() the push()
#  pop(index)  delete the select element of the index

 
