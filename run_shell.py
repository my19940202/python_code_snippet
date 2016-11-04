# -*- coding: utf-8 -*-
# python 运行shell命令
import os
today = 'date'
print today
output = os.popen(today).read()
print 'time is', output

uname = 'uname -a'
output = os.popen(uname).read()
print 'uname is', output
