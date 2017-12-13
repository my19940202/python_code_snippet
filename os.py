# -*- coding: utf-8 -*-
import os
# 合并目录用的 os.path.join
# *nix home/me/mywork
# windows home\me\mywork
print os.path.join("home", "me", "mywork")

# python python_code_snippet/os.py
# 输出 python_code_snippet
# python os.py
# 输出为空
print os.path.dirname(__file__)

# 输出完整path
print os.path.realpath(__file__)

# file name
print   __file__
print   __name__
print   __package__
