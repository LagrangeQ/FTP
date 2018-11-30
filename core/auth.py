#__Author__:  Wei Q
#Date:  2018/10/4
import os
from conf import setting

address = setting.Base_dir+'\db\\all_account\\'
# print(address)
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None,
    'local_info':''
}

remove_conncert = False


def login_required(func):
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("用户没有登陆")
    return wrapper

def acc_login(accout,passwd):
    accout_path = os.path.join(address,accout)
    accout_path = accout_path+'.txt'
    if accout_path:
        with open(accout_path,'r') as f:
            dict_acc = eval(f.read())
            # accout,file = accout.split('.')
            if accout == dict_acc['id']:
                if passwd == dict_acc['passwd']:
                    print('登陆成功!')
                    user_data['is_authenticated'] = True
                    user_data['account_id'] = accout
                    return True

            else:
                    print('账号或者密码错误')


# acc_login('qiu.txt','123')
# print(user_data)