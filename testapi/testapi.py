# unittest
import unittest
import requests
import json
from testconfig import ApiTestConfig
apitestconfig = ApiTestConfig()

class ApiTest(unittest.TestCase):
    """XX接口自动化测试"""
    def setUp(self):
        self.url = apitestconfig.URL
        self.headers = apitestconfig.HEADERS
        self.get_params = apitestconfig.GET_PARAMS
        self.post_data = apitestconfig.POST_DATA

    def test_get(self):
        """GET测试！"""
        for params in self.get_params:
            r = requests.get(self.url, params=params)
            status = r.status_code
            result = r.json()
            print("GET", result)
            self.assertEqual(status, 200)
            # self.assertEqual(result['result'], 'ZXX')

    def test_post(self):
        """POST测试"""
        headers = self.headers
        for data in self.post_data:
            r = requests.post(
                url=self.url, data=json.dumps(data), headers=headers
            )
            result = r.json()
            status = r.status_code
            print("POST:", result)
            self.assertEqual(status, 200)
            # self.assertEqual(result['result'], None)

    def tearDown(self):
        """
        测试用例的结束执行，
        """
        pass

if __name__ == '__main__':
    unittest.main()