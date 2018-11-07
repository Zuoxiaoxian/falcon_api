# 启动接口服务！
import sys
sys.path.append(r"E:\zxx\zxx_projects\falcon_api")
from api.api import api

import waitress




if __name__ == '__main__':
    waitress.serve(api, listen='*:8080') # 可在IPv4和IPv6上运行！
    # waitress.serve(api, host='0.0.0.0', port=8080)