#__Author__:  Wei Q
#Date:  2018/10/8#__Author__:  Wei Q
#Date:  2018/10/2
import sys,os
address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)
import subprocess
import socketserver
from conf import setting
from core import auth

move_conncert = False

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('并发服务器启动..')
        while True:
            i = 0
            conn = self.request #客户端连接id
            print(self.client_address) #打印客户端地址

            while True:

                accout_id = str(conn.recv(1024), 'utf8')# 接收用户id信息
                # conn.sendall(bytes('', 'utf8'))
                # accout_local = str(conn.recv(1024), 'utf8')
                if i == 0:
                        path_add = os.path.join(setting.accout_addr, accout_id)
                        print(path_add)
                        os.chdir(path_add)
                i += 1
                conn.sendall(bytes(os.getcwd(),'utf8'))#发送当前地址

                move_conncert = str(conn.recv(1024),'utf8')#接收确认move
                if move_conncert == 'True':
                        data = conn.recv(1024)
                        cmd,file_name,file_size = str(data,'utf8').split('|')
                        # choice_path = input('选择您要存放的文件夹:\n'
                        #                     '1.Data\n'
                        #                     '2.Home\n').strip()
                        # choice_path = '1'
                        # if choice_path == '1':
                        file_path = os.getcwd() + '\data'
                        # if choice_path == '2':
                        #     file_path = os.getcwd() + '\home'
                        file_patha = os.path.join(file_path,file_name)

                        file_size = int(file_size)
                        print(file_patha,file_size)
                        with open(file_patha,'ab') as f:
                            has_receive = 0
                            while has_receive != file_size:
                                data_r = conn.recv(1024)
                                f.write(data_r)
                                has_receive += len(data_r)
                            print('移动成功!')
                        file_origin_address = str(conn.recv(1024),'utf8')
                        print(file_origin_address)
                        os.remove(file_origin_address)
                data = conn.recv(1024)#接收
                if not data: break

                if str(data, 'utf8') == 'cd ..':

                        # print(path_add)
                        # if path_add.endswith(accout_id):
                        #     path_add = '.\\' + accout_id + '\\'
                        #
                        # len_q = bytes(str(len(path_add)), 'gbk')
                        # result = bytes(path_add, 'utf8')
                        # conn.sendall(len_q)
                        # a = conn.recv(1024)
                        # conn.sendall(result)

                        os.chdir(path_add)
                        print(os.getcwd())
                        len_q = bytes(str(len(os.getcwd())), 'gbk')
                        result = bytes(os.getcwd(), 'utf8')
                        conn.sendall(len_q)
                        a = conn.recv(1024)
                        conn.sendall(result)
                        print('@')
                        continue

                if str(data, 'utf8') == 'cd -h':
                        str_help = '进入文件夹:\n' \
                                   '例如:cd \home'
                        len_q = bytes(str(len(str_help)), 'gbk')
                        result = bytes(str_help, 'utf8')
                        conn.sendall(len_q)
                        a = conn.recv(1024)
                        conn.sendall(result)
                        continue

                if str(data, 'utf8') == 'cd home':
                        # if path_add.endswith(accout_id):
                        #     path_add = '.\\'+accout_id +'\home\\'
                        os.chdir(path_add + '\home')
                        print(os.getcwd())
                        len_q = bytes(str(len(os.getcwd())), 'gbk')
                        result = bytes(os.getcwd(), 'utf8')
                        conn.sendall(len_q)
                        a = conn.recv(1024)
                        conn.sendall(result)
                        # auth.user_data['local_info'] = 'home'

                        continue
                if str(data, 'utf8') == 'll':
                        file_list = str(os.listdir(path_add))
                        print(file_list)

                        len_q = bytes(str(len(file_list)), 'gbk')
                        result = bytes(file_list, 'utf8')
                        conn.sendall(len_q)
                        a = conn.recv(1024)
                        conn.sendall(result)
                        continue
                if str(data, 'utf8') == '':
                    obj = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)
                    cmd_result = obj.stdout.read()
                    print(type(cmd_result))
                    result_len = bytes(str(len(cmd_result)), 'gbk')
                    conn.sendall(result_len)
                    a = conn.recv(1024)
                    # print(a)
                    conn.sendall(result)
                    continue

                    # choice = str(data, 'utf8')


                print('客户端输入的指令为:',str(data, 'utf8'))
                obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
                result = obj.stdout.read()
                len_re = bytes(str(len(result)), 'gbk')
                conn.sendall(len_re)
                a = conn.recv(1024)
                conn.sendall(result)

            conn.close()
def run():
    print('服务器等待响应...')
    server = socketserver.ThreadingTCPServer(setting.Address_ip_point_Server, MyServer)
    server.serve_forever()

if __name__ == '__main__':
    run()