#__Author__:  Wei Q
#Date:  2018/10/1
import sys,os
address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)

import hashlib
passwd = 'chen89726'
hl = hashlib.md5()
hl.update(passwd.encode(encoding='utf8'))

print(hl.hexdigest())
print(__file__)
t = '3'
print(passwd.endswith(t))