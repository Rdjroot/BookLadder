# -*- coding = utf-8 -*-
# @Time:2021/2/2517:57
# @Author:Linyu
# @Software:PyCharm
import re

matchStr = "Effective C++"
strin = ""
for mat in matchStr:
    if mat =='+':
        mat = '\+'
    strin =strin+mat
print(strin)
# matchStr = "dshgfajhg ds++"
pattern = re.compile(r'.*?'+strin+'.*?',re.S)
print(re.findall(pattern,"Effective C++"))