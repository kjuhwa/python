# import mymodule as my
#from mymodule import hap, gop
from mymodule import *

# import sys
# py, pyc, pyd(확장파이썬,C)
# python -m py_compile mymodule.py
# mymodule.pyc

# sys.path.append(r'D:\\python\\mylib')
# print(sys.path)

# rst = my.hap(10,20)
# print(rst)
# rst = my.gop(10,20)
# print(rst)

rst = hap(10,20)
print(rst)
rst = gop(10,20)
print(rst)
