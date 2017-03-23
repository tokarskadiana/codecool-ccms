# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from model.mentor import  Mentor


class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_student(self, username):
        print('\tlogin START')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin SUCCESS')

    def logout(self):
        print('\tlogout START')
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="homepage"]/aside/div[1]/div/div/a').click()
        print('\tlogout SUCCESS')

    def check_attendance_stats(self):
        print('\tcheck attendance stats START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Show student statistics").click()
        print('\t\tcheck if attendance stats exist START')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[3]') == '100.0'
        except:
            raise ValueError('there is no stats')
        print('\t\tcheck if attendance stats exist SUCCESS')
        print('\tcheck attendance stats SUCCESS')

    def submit_assignment(self):
        print('\tsubmit assignment START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[2]/a').click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div[1]/a').click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div[1]/form/textarea').clear()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div[1]/form/textarea').send_keys('test')
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div[1]/form/input').click()
        print('\t\tcheck if content of assignment is exist START')
        if driver.find_element_by_xpath(
                '//*[@id="homepage"]/section/div[1]/div[3]/p') == "You don't submit this assignment yet":
            raise ValueError('there is no content')
        print('\t\tcheck if content of assignment is exist SUCCESS')
        print('\tsubmit assignment SUCCESS')

    def check_assignment(self):
        print('\tcheck assignment START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[2]/a').click()
        print('\t\tcheck if content of team assignment is exist START')
        if driver.find_element_by_xpath(
                '//*[@id="homepage"]/section/div[1]/div[3]/p') == "You don't submit this assignment yet":
            raise ValueError('there is no content')
        print('\t\tcheck if content of team assignment is exist SUCCESS')
        print('\tcheck assignment SUCCESS')

    def check_grade(self):
        print('\tcheck grade START')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Show student statistics").click()
        print('\t\tcheck if grade stats exist START')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[2]') == '5.0'
        except:
            raise ValueError('there is no stats')
        print('\t\tcheck if grade stats exist SUCCESS')
        print('\tcheck grade SUCCESS')

    # ----------TESTS-----------


    def test_login(self):
        print('test login')
        Student.login_student(self, "piotr.gurdek")

    def test_view_attendance_stats(self):
        print('test view attendance stats')
        Mentor.login_mentor(self)
        Mentor.attendance(self)
        Mentor.logout(self)
        Student.login_student(self, "piotr.gurdek")
        Student.check_attendance_stats(self)

    def test_submit_assignment_as_individual(self):
        print('test submit assignment')
        Mentor.login_mentor(self)
        Mentor.add_assignments(self)
        Mentor.logout(self)
        Student.login_student(self, "piotr.gurdek")
        Student.submit_assignment(self)
        Student.logout(self)
        Mentor.login_mentor(self)
        Mentor.remove_assignments(self)

    def test_submit_assignment_as_a_team(self):
        print('test submit assignment as a team')
        Mentor.login_mentor(self)
        Mentor.add_assignments(self, group=True)
        Mentor.add_team(self)
        Mentor.add_student_to_team(self)
        Mentor.logout(self)
        Student.login_student(self, "piotr.gurdek")
        Student.submit_assignment(self)
        Student.logout(self)
        Student.login_student(self, "monika.plocica")
        Student.check_assignment(self)
        Student.logout(self)
        Mentor.login_mentor(self)
        Mentor.remove_assignments(self)

    def test_check_grades(self):
        print('test submit assignment')
        Mentor.login_mentor(self)
        Mentor.add_assignments(self)
        Mentor.logout(self)
        Student.login_student(self, "piotr.gurdek")
        Student.submit_assignment(self)
        Student.logout(self)
        Mentor.login_mentor(self)
        Mentor.grade_assignments(self)
        Mentor.logout(self)
        Student.login_student(self, "piotr.gurdek")
        Student.check_grade(self)
        Student.logout(self)
        Mentor.login_mentor(self)
        Mentor.remove_assignments(self)

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
