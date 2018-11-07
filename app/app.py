# 这里是接口方法
from jsonrpc import  dispatcher

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs['name'] + kwargs['age']
