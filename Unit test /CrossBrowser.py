import unittest
import time
import locators as lc
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get(lc.test_url)
        driver_chrome.maximize_window()
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.vis)))
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath(lc.name)
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_chrome.find_element_by_xpath(lc.email)
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_chrome.find_element_by_xpath(lc.message)
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_chrome.find_element(By.ID, lc.submit).submit()
        driver_chrome.implicitly_wait(4)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, lc.go_back))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_chrome.find_element(By.XPATH, lc.go_back).click()
        driver_chrome.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img1)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img2)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img3)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img4)))

        driver_chrome.implicitly_wait(8)

        assert "California Real Estate" in driver_chrome.title
        print("After clicking 'Go back' button we're back to the right page:", driver_chrome.title)
        time.sleep(1)

    def test_chrome_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get(lc.test_url)
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.vis)))
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath(lc.name)
        search_name.clear()
        search_email = driver_chrome.find_element_by_xpath(lc.email)
        search_email.clear()
        search_message = driver_chrome.find_element_by_xpath(lc.message)
        search_message.clear()
        driver_chrome.find_element(By.XPATH, lc.name).send_keys("Pavel Bulgakov")
        driver_chrome.find_element(By.XPATH, lc.email).send_keys("pavelpavelb@gmail.com")
        driver_chrome.find_element(By.XPATH, lc.message).send_keys(
            "This my first CrossBrowser test")
        driver_chrome.find_element(By.ID, lc.submit).submit()
        driver_chrome.implicitly_wait(4)
        html = driver_chrome.find_element_by_tag_name('html')

        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        # html.send_keys(Keys.PAGE_UP)
        # html.send_keys(Keys.PAGE_UP)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        html.find_element(By.XPATH, lc.go_back).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img1)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img2)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img3)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img4)))
        driver_chrome.implicitly_wait(4)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("After clicking 'Go back' button we're back to the right page:", driver_chrome.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


class FireFoxTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fire_fox(self):
        driver_firefox = self.driver
        driver_firefox.get(lc.test_url)
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.vis)))
        time.sleep(1)

        assert "California Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

        search_name = driver_firefox.find_element_by_xpath(lc.name)
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_firefox.find_element_by_xpath(lc.email)
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_firefox.find_element_by_xpath(lc.message)
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_firefox.find_element(By.ID, lc.submit).submit()
        driver_firefox.implicitly_wait(4)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, lc.go_back))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_firefox.find_element(By.XPATH, lc.go_back).click()
        driver_firefox.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img1)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img2)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img3)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img4)))

        assert "California Real Estate" in driver_firefox.title
        print("After clicking 'Go back' button we're back to the right page:", driver_firefox.title)
        time.sleep(1)

    def test_fire_fox_default_1250x850_window(self):
        driver_firefox = self.driver
        driver_firefox.get(lc.test_url)
        driver_firefox.set_window_size(1250, 850)
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.vis)))
        time.sleep(1)

        assert "California Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

        search_name = driver_firefox.find_element_by_xpath(lc.name)
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_firefox.find_element_by_xpath(lc.email)
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_firefox.find_element_by_xpath(lc.message)
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_firefox.find_element(By.ID, lc.submit).submit()
        driver_firefox.implicitly_wait(4)

        html = driver_firefox.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, lc.go_back))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_firefox.find_element(By.XPATH, lc.go_back).click()
        driver_firefox.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img1)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img2)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img3)))
        wait.until(EC.visibility_of_element_located((By.XPATH, lc.img4)))

        assert "California Real Estate" in driver_firefox.title
        print("After clicking 'Go back' button we're back to the right page:", driver_firefox.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
