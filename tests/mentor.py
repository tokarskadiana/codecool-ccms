# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Mentor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_mentor(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("mateusz.ostafil")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()

    def list_students(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()

    def add_assignments(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_id("main-form-title").clear()
        driver.find_element_by_id("main-form-title").send_keys("test")
        driver.find_element_by_id("main-form-desc").clear()
        driver.find_element_by_id("main-form-desc").send_keys("test")
        driver.find_element_by_id("main-form-date").send_keys("10/10/2012")
        driver.find_element_by_id("main-sub-button").click()

    def remove_assignments(self):
        pass

    def attendance(self):
        print('\tattendance test start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Check attendance").click()
        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_xpath(
            "//body[@id='homepage']/section/form/div/table/tbody/tr/td[2]/label/span").click()
        driver.find_element_by_id("1-yes").click()
        driver.find_element_by_xpath(
            "//body[@id='homepage']/section/form/div/table/tbody/tr[2]/td[2]/label/span").click()
        driver.find_element_by_id("2-yes").click()
        driver.find_element_by_id("attendance-sub-button").click()
        print('\tttendance test PASS')

    def add_student(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys("test")
        driver.find_element_by_name("last-name").clear()
        driver.find_element_by_name("last-name").send_keys("test")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("test@test.test")
        driver.find_element_by_name("phone-number").clear()
        driver.find_element_by_name("phone-number").send_keys("123456789")
        driver.find_element_by_name("submition").click()

    def remove_student(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[3]/td[7]/a/i").click()

    def edit_student(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[3]/td[6]/a/i").click()
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys("edited")
        driver.find_element_by_name("last-name").clear()
        driver.find_element_by_name("last-name").send_keys("edited")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("edited")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("edited@edited.com")
        driver.find_element_by_name("submition").click()

    def add_team(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("test")
        driver.find_element_by_css_selector("input.main-button").click()

    def remove_team(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("i.fa.fa-trash").click()

    def edit_team(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("i.fa.fa-pencil-square-o").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("edit")
        driver.find_element_by_css_selector("input.main-button").click()

    # ------------ TESTS -----------


    def test_login(self):
        print('test login')
        Mentor.login_mentor(self)

    def test_list_students(self):
        print('test list students')
        Mentor.login_mentor(self)
        Mentor.list_students(self)

    def test_add_assignments(self):
        print('test add assignemts')
        Mentor.login_mentor(self)
        Mentor.add_assignments(self)

    # def test_attendance(self):
    #     print('test attendance')
    #     Mentor.login_mentor(self)
    #     Mentor.attendance(self)

    def test_add_student(self):
        print('test add student')
        Mentor.login_mentor(self)
        Mentor.add_student(self)
        Mentor.remove_student(self)

    def test_edit_student(self):
        print('test edit student')
        Mentor.login_mentor(self)
        Mentor.add_student(self)
        Mentor.edit_student(self)
        Mentor.remove_student(self)

    def test_remove_student(self):
        print('test remove student')
        Mentor.login_mentor(self)
        print('add')
        Mentor.add_student(self)
        print('remove')
        Mentor.remove_student(self)

    def test_add_team(self):
        print('test add team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.remove_team(self)

    def test_edit_team(self):
        print('test edit team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.edit_team(self)
        Mentor.remove_team(self)

    def test_remove_team(self):
        print('test remvoe team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.remove_team(self)



    #
    # def test_add_student_to_team(self):
    #     Mentor.test_login(self)
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_link_text("List teams").click()
    #     driver.find_element_by_css_selector("input.sub-right.main-button").click()
    #     driver.find_element_by_name("name").clear()
    #     driver.find_element_by_name("name").send_keys("test")
    #     driver.find_element_by_css_selector("input.main-button").click()
    #     driver.get(self.base_url + "/list-teams")
    #     driver.find_element_by_link_text("List students").click()
    #     driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[2]/td[6]/a/i").click()
    #     Select(driver.find_element_by_name("team")).select_by_visible_text("test")
    #     driver.find_element_by_name("submition").click()

    # def test_checkpoint(self):
    #     Manager.test_login(self)
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_link_text("List checkpoints").click()
    #     driver.find_element_by_css_selector("input.sub-right.main-button").click()
    #     driver.find_element_by_id("main-form-title").clear()
    #     driver.find_element_by_id("main-form-title").send_keys("test")
    #     driver.find_element_by_id("main-form-date").clear()
    #     driver.find_element_by_id("main-form-date").send_keys("10/10/2012")
    #     driver.find_element_by_id("main-sub-button").click()
    #     driver.find_element_by_css_selector("i.fa.fa-pencil-square-o").click()
    #     Select(driver.find_element_by_name("checkpoint-grade[]")).select_by_visible_text("Red")
    #     Select(driver.find_element_by_name("checkpoint-grade[]")).select_by_visible_text("Yellow")
    #     Select(driver.find_element_by_xpath("(//select[@name='checkpoint-grade[]'])[2]")).select_by_visible_text(
    #         "Green")
    #     driver.find_element_by_css_selector("button[type=\"submit\"]").click()
    #     # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
    #     driver.find_element_by_id("command-button-pick").click()

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
