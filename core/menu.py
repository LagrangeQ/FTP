#__Author__:  Wei Q
#Date:  2018/10/4
import os,sys
address = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(address)
from conf import setting
from core import auth
import hashlib



def interactive():
    print(setting.menu_look)
    if auth.user_data['is_authenticated'] == True:
        # print(auth.user_data['account_id'])
        from core import Client
    else:
        print('您还未登陆账号')
        run()



def run():
    accout = input('请输入您的账号:').strip()
    passwd = input('请输入您的密码:').strip()
    hl = hashlib.md5()
    hl.update(passwd.encode(encoding='utf8'))
    passwd = hl.hexdigest()
    if auth.acc_login(accout,passwd):
        interactive()

if __name__ == '__main__':
    run()