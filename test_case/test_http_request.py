import unittest
from ddt import ddt,data
from auto_test_api.common.http_request import HttpRequest
from auto_test_api.common.do_excel import DoExcel
import pymysql
import reports
import logging

db = pymysql.connect(host="localhost", user="root", password="admin",database= "guest", charset= "utf8")
cursor = db.cursor()
cursor.execute("select * from data2")

data = cursor.fetchall()
for i in data:
    print("ddt 分解出来的数据是：{0}".format(i))

# test_data = DoExcel(r"F:\PycharmProjects\untitled1\sunzong.xlsx", "Sheet1").do_excel()

# @ddt

class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        pass


    # test_data=[{"url":"http://150.109.156.47:8000/api/get_event_list","param":{"eid":"1"},"method":"get"},
    #            {"url":"http://150.109.156.47:8000/api/get_event_list","param":{"eid":"2"},"method":"get"},
    #            {"url":"http://150.109.156.47:8000/api/get_event_list","param":{"eid":"3"},"method":"get"}]
    # @data(*test_data)
    # def test_case_01(self,data_item):
    #     print("*******************************************************")
    #     print("ddt 分解传递出来的参数是：{0}".format(data_item))
    #
    #     res=HttpRequest(data_item["url"],data_item["param"]).http_request(data_item['method'])
    #     print(res)
    #     print("第1条 测试用例的执行结果是：{0}".format(res.json()))
    def test_case_01(self):
        # logging.basicConfig(filename='log.txt',
        #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
        #                     level=logging.INFO)
        print("*******************************************************")
        for i in data:
            id = i[0]
            method = i[2]
            url = i[3]
            param = i[4]

            res=HttpRequest(url,eval(param)).http_request(method)

            print(res)
            print("第1条 测试用例的执行结果是：{0}".format(res.json(),id))



        try:
            self.assertEqual(res.json()["status"],10200)
            sql = f"UPDATE `data2` SET test_result = 'pass' where case_id={id}"
            cursor.execute(sql)
            db .commit()
            print("测试结果写入完毕!")

        except AssertionError as e:
            print("执行接口测试出错，错误是{o}".format(e))
            sql = f"UPDATE `data2` SET test_result = 'fail' where case_id={id}"
            cursor.execute(sql)
            db.commit()
            print("测试结果写入完毕!")

        finally:
            pass

        logging.getLogger().setLevel(logging.INFO)
        logging.info(
            f"case:添加发布会，eid为空\n请求地址：{res.url}\t请求方式:{res.request.method}\n请求头：{res.request.headers}\n请求正文：响应头：{res.headers}\n响应正文：{res.text}\n")

    def tearDown(self) -> None:
        cursor.close()
        db.close()
        print("测试结束")

if __name__ == '__main__':
    unittest.main()