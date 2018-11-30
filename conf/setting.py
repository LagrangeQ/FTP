#__Author__:  Wei Q
#Date:  2018/10/2
import os
import sys

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

accout_addr = Base_dir + '\db\\'

Address_ip_point_Server = ('127.0.0.1',8000)
Address_ip_point_Client = ('127.0.0.1',8000)

def db_path(name):
    db_path = 'Base_dir'+name
    return db_path


Disk_Capacity = {
    'First':'200000000‬',
    'Second':'1200000000‬',
    'Third':'50000000‬'
}

menu_look = '欢迎使用CMD版本FTP!\n' \
            '功能如下:\n' \
            '查看您的文件\n' \
            '下载或上传文件\n' \
            '' \
            ''

menu_all = {
    1:'',
    2:'',
    3:'',
    4:'',

}


