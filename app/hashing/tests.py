from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FunctionalTestCase(TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        # options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("enable-automation")
        self.options.add_argument("--disable-infobars")
        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.browser.quit()

    def test_amazon_login(self):
        self.browser.get("https://auth.geeksforgeeks.org/")
        self.browser.get_screenshot_as_file("enteruser.png")
        print(self.browser.title)
        email=self.browser.find_element(By.ID,'luser')
        email.send_keys('xyz@gmail.com')
        pwd=self.browser.find_element(By.ID,'password')
        pwd.send_keys('xyz12345')
        self.browser.find_element(By.CLASS_NAME,"signin-button").click();
        time.sleep(15)
        self.browser.get_screenshot_as_file("enterpassword.png")



