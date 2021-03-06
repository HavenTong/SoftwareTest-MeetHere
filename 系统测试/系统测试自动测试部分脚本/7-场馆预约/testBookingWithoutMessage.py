# Generated by Selenium IDE
import unittest
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestBookingWithoutMessage(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testBookingWithoutMessage(self):
    self.driver.get("http://localhost:8002/#/")
    self.driver.set_window_size(1536, 835)
    self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/section/form/div[2]/div/div/input").send_keys("xmfnnj@outlook.com")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/section/form/div[3]/div/div/input").send_keys("yuechen")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys(Keys.ENTER)
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/ul/li[3]/div").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/ul/li[3]/ul/li").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/button/span").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div[2]/div/div[4]/div/div[2]/div[2]/button").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".el-notification")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(4) .el-dialog__close").click()
    self.driver.close()
  
