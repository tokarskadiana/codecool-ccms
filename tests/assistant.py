# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Assistant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_assistant(self):
        print('\tlogin test start')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("miriam.rej")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin success')

    def list_students(self, test_student=False):
        print('\tlist student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        students = [{'name':'Piotr Gurdek'},{'name':'Monika Plocica'}]
        for i in range(2):
            print('\tcheck if test student name:{} exist start'.format(students[i]['name']))
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[{}]/td[2]'.format(i+1)).text == students[i]['name']
            except:
                raise ValueError('there is no test student')
            print('\tcheck if test student name:{} exist success'.format(students[i]['name']))
        if test_student:
            print('\tcheck if test student exist start')
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[3]/td[2]').text == "test test"
            except:
                raise ValueError('there is no test student')
            print('\tcheck if test student exist success')
        print('\tlist student success')

    # ----------TESTS-----------

    def test_login(self):
        print('test login')
        Assistant.login_assistant(self)

    def test_list_students(self):
        print('test list students')
        Assistant.login_assistant(self)
        Assistant.list_students(self)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
