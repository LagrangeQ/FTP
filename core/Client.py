#__Author__:  Wei Q
#Date:  2018/10/2
import sys,os,time
address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)
import socket
from conf import setting
from core import auth

sk = socket.socket()
sk.connect(setting.Address_ip_point_Client)

move_conncert = False

while True:
    # print(auth.user_data['account_id'])
    sk.sendall(bytes(auth.user_data['account_id'],'utf8'))#发送用户id信息
    # accout_test = str(sk.recv(1024), 'utf8')
    # sk.sendall(bytes(auth.user_data['local_info'],'utf8'))
    cmd_path = str(sk.recv(1024),'utf8')#接收当前服务端地址
    # print(cmd_path)
    inp_cmd = input('<<<:')
    while '|' not in inp_cmd:
        print('您的输入格式错误!请输入:命令|命令')
        print('命令为')
        inp_cmd = input('<<<:')
    cmd,inp_cmd = inp_cmd.split('|')
    # print(cmd,inp_cmd)
    if cmd == 'move':#发送remove_conncert值
        # global remove_conncert
        move_conncert = True
        sk.sendall(bytes(str(move_conncert),'utf8'))
        file_path = os.path.join(cmd_path,inp_cmd)
        file_name = os.path.basename(file_path)
        file_size = os.stat(file_path).st_size
        file_info = 'move|%s|%s'%(file_name,file_size)
        sk.sendall(bytes(file_info,'utf8'))
        try:
            with open(file_path,'rb') as fh:
                has_send = 0
                while has_send != file_size:
                    data_r = fh.read(1024)
                    sk.sendall(data_r)
                    has_send += len(data_r)
                    print('进度:'+str(has_send/file_size)+'\r')
            print(file_path)
            print(cmd_path)
            sk.sendall(bytes(file_path,'utf8'))
        except IOError:
            print('此目录不存在该文件!')
            continue
    else:
        sk.sendall(bytes(str(move_conncert), 'utf8'))

    # else:
    #     # inp_cmd = cmd
    #     print(inp_cmd)

    if inp_cmd == 'exit': break
    sk.sendall(bytes(inp_cmd,'utf8'))#发送指令
    time.sleep(0.5)
    # recv_module()#接收指令回复
    cmd_len = int(str(sk.recv(1024), 'gbk'))
    sk.sendall(bytes(inp_cmd,'utf8'))
    data = bytes()
    while len(data) != cmd_len:
        revc = sk.recv(1024)
        data += revc
    print(str(data, 'gbk'))




sk.close()

