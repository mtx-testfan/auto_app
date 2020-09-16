'''
需要从外部去导入模块，而不是继承的
'''
import time

from mobileUtil.baseOperate import OperateElement
from mobileUtil.baseDriver import BaseDriver
from mobileUtil.inihelper import IniHelper


class LoginPage:
    # 获取登录页面的所有页面元素信息
    def __init__(self, i):
        # 实例化operateElement self.driver 随便取的名字，叫什么都行
        self.driver = OperateElement(BaseDriver().android_driver(i))
        self.source = IniHelper()

    # 点击账号密码登录
    # 没操作一个步骤  都要sleep一下
    def click_username_login(self):
        self.driver.click(self.source.get_value('doubanPage.ini','Button','帐号密码登录'))
        time.sleep(10)

    # 输入用户名
    def input_username(self,username):
        self.driver.type(self.source.get_value('doubanPage.ini','TextInput','用户名'),username)
        time.sleep(3)
    # 输入密码
    def input_password(self, password):
        self.driver.type(self.source.get_value('doubanPage.ini', 'TextInput', '密码'), password)
        time.sleep(3)
    # 点击登录
    def click_login_button(self):
        self.driver.click(self.source.get_value('doubanPage.ini', 'Button', '登录按钮'))
        time.sleep(3)

    # 为了断言  点击我的
    def click_me(self):
        self.driver.click(self.source.get_value('doubanPage.ini', 'Button', '我的'))
        time.sleep(3)
    # 获取page_source

    @property
    def get_page_source(self):
        return self.driver.page_source
    # 退出
    def quit_driver(self):
        self.driver.quit_driver()


    # 组合业务方法
    def login_pass(self,username,password):
        ## 点击账号密码登录
        self.click_username_login()
        # 用户名
        self.input_username(username)
        # 密码
        self.input_password(password)
        # 点击登录
        self.click_login_button()