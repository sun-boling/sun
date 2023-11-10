
import HTMLTestRunnerNew
import unittest
from test_http_request import  TestHttpRequest
from unittestreport import TestRunner


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestHttpRequest("test_case_01"))
    runner = TestRunner(suite,report_dir=r"F:\PycharmProjects\untitled1\reports",filename="demo.html",title="demo",tester="ervin",templates=2)
    runner.run()
    runner.send_email(host="smtp.qq.com",
                      port=465,
                      user="1037586195@qq.com",
                      password="tgikbktzwvsnbbbj",
                      to_addrs="1055916660@qq.com")

