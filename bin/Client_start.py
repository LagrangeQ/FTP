#__Author__:  Wei Q
#Date:  2018/10/2
import sys,os

address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)
print('开启客户端:')
from core import Client