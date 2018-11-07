
class ApiTestConfig(object):
    """
    测试的url、GET、POST请求体！
    """
    URL = "http://127.0.0.1/testapi"
    # URL = "http://127.0.0.1:8080/testapi" # 未开代理下测试！
    HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic bWFibzptYWJV',
        }
    GET_PARAMS = [{"method": "foobar", "name": 'zxx', "age": '12'}]
    POST_DATA = [
        {
            "method": "foobar",
            "params": {
                "name": 'zxx',
                "age": '12'
            },
            "jsonrpc": "2.0",
            "id": "0"
         },  
    ]