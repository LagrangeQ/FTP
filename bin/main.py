#__Author__:  Wei Q
#Date:  2018/10/1
import sys,os
address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)
from core import menu
from core import Server
b = os.path.abspath(__file__)
print('1.开启客户端 2.开始服务器')
choice = input('输入您想打开的服务:').strip()

if choice == '1':
    menu.run()
if choice == '2':
    # assert Server.run() == os.system('start')
    for i in range(2):
        if i == 0:
            os.system('start %s'%b)
        else:
            os.system('cls')
            Server.run()


    # from bin import Client_start
# elif choice == 2:
#     os.system('start')
#     from core import Server


