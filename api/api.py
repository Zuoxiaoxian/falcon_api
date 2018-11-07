# 这里是falcon 资源

import falcon
from jsonrpc import JSONRPCResponseManager
from app.app import dispatcher
import json
class TestApi(object):

    def on_get(self, req, resp):
        params = req.params
        method = params['method']
        param = params.copy()
        param.pop('method')
        write_log(str(param))
        resp_data = {
            "method": method,
            "params": param,
            "jsonrpc": "2.0",
            "id": "0",
            }
        write_log(str(json.dumps(resp_data)))
        response = JSONRPCResponseManager.handle(json.dumps(resp_data), dispatcher)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
        # 添加响应头
        resp.append_header("Access-Control-Allow-Origin", "*")
        resp.append_header("Access-Control-Allow-Methods", "*")
        # 设置cookies
        resp.set_cookie('my_cookie', 'Zxx', max_age=600, domain='95.169.12.124')
        # body 是json格式
        resp.body = response.json

    def on_post(self, req, resp):
        resp_data = req.stream.read()
        write_log(str(req.access_route)) # list 原始客户端的IP地址，它的代理地址
        # write_log(str(req.cookies)) # 请求的cookie dict 

        # 添加响应头
        resp.append_header("Access-Control-Allow-Origin", "*")
        resp.append_header("Access-Control-Allow-Methods", "*")
        # 设置cookies
        resp.set_cookie('my_cookie', 'Zxx', max_age=600)
        response = JSONRPCResponseManager.handle(resp_data, dispatcher)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
        resp.body = response.json

api = falcon.API()

testapi = TestApi()

api.add_route('/testapi', testapi)


def write_log(messages):
    with open('api.txt', 'a', encoding='utf-8')as f:
        f.write(messages)
        f.write('\n')