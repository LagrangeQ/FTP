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


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('并发服务器启动..')
        while True:
            conn = self.request
            print(self.client_address)
            if str(data, 'utf8') == 'cd ..':

                # print(path_add)
                if path_add.endswith(accout_id):
                    path_add = '.\\' + accout_id + '\\'

                len_q = bytes(str(len(path_add)), 'gbk')
                result = bytes(path_add, 'utf8')
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
            if str(data, 'utf8') == 'ok':
                obj = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)
                cmd_result = obj.stdout.read()
                print(type(cmd_result))
                result_len = bytes(str(len(cmd_result)), 'gbk')
                conn.sendall(result_len)
                a = conn.recv(1024)
                # print(a)
                conn.sendall(result)
                continue



            while True:
                accout_id = str(conn.recv(1024), 'utf8')
                # conn.sendall(bytes('', 'utf8'))
                # accout_local = str(conn.recv(1024), 'utf8')
                path_add = os.path.join(setting.accout_addr, accout_id)
                print(path_add)
                data = conn.recv(1024)
                if not data: break


                choice = str(data, 'utf8')


                print(str(data, 'utf8'))
                obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
                result = obj.stdout.read()
                len_re = bytes(str(len(result)), 'gbk')
                conn.sendall(len_re)
                a = conn.recv(1024)
                conn.sendall(result)
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(setting.Address_ip_point_Server,MyServer)
    server.serve_forever()


