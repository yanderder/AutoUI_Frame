# -*- coding: utf-8 -*-

'''
@Time    : 2021/2/1 21:26
@Author  : YAN
@FileName: test.py
@Software: PyCharm
 
'''
import shlex
import subprocess

cmd=shlex.split("scrcpy --record ./ tmp.mp4")
print(cmd)
# p=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# print(p)