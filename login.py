from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import ddt
from time import sleep
import HTMLTestRunnerNew

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.driver.get("http://192.168.2.89:8000/")
    def test_001_err(self):
        login_name = self.driver.find_element(By.ID, "inputUsername")
        login_name.clear()
        login_name.send_keys("admin")
        # 登录密码
        login_pwd = self.driver.find_element(By.ID, "inputPassword")
        login_pwd.clear()
        login_pwd.send_keys("admin")
        # 登录按钮
        ele = self.driver.find_element(By.XPATH, '/html/body/div/form/button')
        ele.click()
        self.assertIn("username or password error",self.driver.page_source)

        """
         错误密码登录失败
         登录名

        """
    def test_002_suc(self):
        login_name = self.driver.find_element(By.ID,"inputUsername")
        login_name.clear()
        login_name.send_keys("admin")
        # 登录密码
        login_pwd = self.driver.find_element(By.ID,"inputPassword")
        login_pwd.clear()
        login_pwd.send_keys("admin123456")
        #登录按钮
        login_ddd= self.driver.find_element(By.XPATH,'/html/body/div/form/button')
        login_ddd.click()

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
        suite=unittest.TestSuite()
        suite.addTest(TestLogin("def test_001_err"))
        suite.addTest(TestLogin("def test_002_suc"))
        with open("login_report.html","wb") as file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title="login Test report",description="test report")
            runner.run(suite)
