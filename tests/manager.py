# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Manager(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_manager(self):
        print('\tlogin manager start')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("jurek.mardaus")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin manager success')

    def add_mentor(self):
        print('\tadd mentor start')
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
        print('\t\tcheck if test mentor exist start')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[2]/td[2]').text == 'test test'
        except:
            raise ValueError('there is no test mentor')
        print('\t\tcheck if test mentor exist success')
        print('\tadd mentor success')

    def edit_mentor(self):
        print('\tedit mentor start')
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
        print('\t\t check if edited mentor exist start')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[2]/td[2]') == "edited edited"
        except:
            raise ValueError('there is no edited mentor')
        print('\t\t check if edited mentor exist success')
        print('\tedit mentor success')

    def remove_mentor(self):
        print('\tremove mentor start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[2]/td[7]/a/i").click()
        print('\tremove mentor success')

    def list_mentors(self):
        print('\tlist mentor start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List mentors").click()
        print('\tlist mentor success')

    def list_students(self):
        print('\tlist student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        print('\tlist student success')

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
