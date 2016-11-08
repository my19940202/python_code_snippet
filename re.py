# -*- coding: utf-8 -*-
# Python的正则使用
import re
def main():
    str1 = 'j1k234k11234kl1423'
    # findall 使用较多
    numsPattern = re.compile(r'\d{3,8}$')
    nums = numsPattern.findall(str1)
    print nums

if __name__ == '__main__':
    main()