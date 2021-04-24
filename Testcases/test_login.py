import pytest
from selenium import webdriver
from Pageobjects.loginpage import Loginpage


class Test_001_Login:
    baseURL= 'https://demo.nopcommerce.com/login?returnUrl=%2F'
    username= 'umasankarp93@gmail.com'
    password= 'usp123'

    def test_homePageTitle(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        title=self.driver.title
        self.driver.close()
        if title=='nopCommerce demo store.Login':
            assert True
        else:
            assert False


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        title=self.driver.title
        self.driver.close()
        if title=='nopCommerce demo store. Register':
            assert True
        else:
            assert  False

























