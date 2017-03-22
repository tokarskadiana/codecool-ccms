# -*- coding: utf-8 -*-
import unittest, time, re
from tests.user import User

class Assistant(User):

    def login_assistant(self):
        print('\tlogin test START')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("miriam.rej")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin SUCCESS')

    def list_students(self, test_student=False):
        print('\tlist student START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        students = [{'name':'Piotr Gurdek'},{'name':'Monika Plocica'}]
        for i in range(2):
            print('\t\tcheck if test student name:{} exist START'.format(students[i]['name']))
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[{}]/td[2]'.format(i+1)).text == students[i]['name']
            except:
                raise ValueError('there is no test student')
            print('\t\tcheck if test student name:{} exist SUCCESS'.format(students[i]['name']))
        if test_student:
            print('\t\tcheck if test student exist START')
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[3]/td[2]').text == "test test"
            except:
                raise ValueError('there is no test student')
            print('\t\tcheck if test student exist SUCCESS')
        print('\tlist student SUCCESS')

    # ----------TESTS-----------

    def test_login(self):
        print('test login')
        Assistant.login_assistant(self)

    def test_list_students(self):
        print('test list students')
        Assistant.login_assistant(self)
        Assistant.list_students(self)

if __name__ == "__main__":
    unittest.main()
