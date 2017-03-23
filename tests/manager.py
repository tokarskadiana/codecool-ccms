# -*- coding: utf-8 -*-
from tests.user import User
import unittest, time, re


class Manager(User):
    def login_manager(self):
        print('\tlogin manager START')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("jurek.mardaus")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin manager SUCCESS')

    def add_mentor(self):
        print('\tadd mentor START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("test")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("test")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("test@test.test")
        driver.find_element_by_name("salary").clear()
        driver.find_element_by_name("salary").send_keys("10")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test")
        driver.find_element_by_name("phone_number").clear()
        driver.find_element_by_name("phone_number").send_keys("123456789")
        driver.find_element_by_name("submition").click()
        print('\t\tcheck if test mentor exist START')
        xpaths_values = {'//*[@id="homepage"]/section/div/table/tbody/tr[2]/td[2]': 'test test'}
        self.match_data(xpaths_values, massage='there is no test mentor')
        print('\t\tcheck if test mentor exist SUCCESS')
        print('\tadd mentor SUCCESS')

    def edit_mentor(self):
        print('\tedit mentor START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[2]/td[6]/a/i").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("edited")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("edited")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("edited@edited.com")
        driver.find_element_by_name("salary").clear()
        driver.find_element_by_name("salary").send_keys("100")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("edited")
        driver.find_element_by_name("submition").click()
        print('\t\t check if edited mentor exist START')
        xpaths_values = {'//*[@id="homepage"]/section/div/table/tbody/tr[2]/td[2]': "edited edited"}
        self.match_data(xpaths_values, massage='there is no edited mentor')
        print('\t\t check if edited mentor exist SUCCESS')
        print('\tedit mentor SUCCESS')

    def remove_mentor(self):
        print('\tremove mentor START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[2]/td[7]/a/i").click()
        print('\tremove mentor SUCCESS')

    def list_mentors(self):
        print('\tlist mentor START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        print('\tlist mentor SUCCESS')

    def list_students(self):
        print('\tlist student START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        print('\tlist student SUCCESS')

    # --------- TESTS ----------

    def test_login_manager(self):
        print('test login manager')
        Manager.login_manager(self)

    def test_add_mentor(self):
        print('test add mentor')
        Manager.login_manager(self)
        Manager.add_mentor(self)
        Manager.remove_mentor(self)

    def test_edit_mentor(self):
        print('test edit mentor')
        Manager.login_manager(self)
        Manager.add_mentor(self)
        Manager.edit_mentor(self)
        Manager.remove_mentor(self)

    def test_remove_mentor(self):
        print('test remove mentor')
        Manager.login_manager(self)
        Manager.add_mentor(self)
        Manager.remove_mentor(self)

    def test_list_mentors(self):
        print('test list mentors')
        Manager.login_manager(self)
        Manager.list_mentors(self)

    def test_list_students(self):
        print('test list students')
        Manager.login_manager(self)
        Manager.list_students(self)


if __name__ == "__main__":
    unittest.main()
