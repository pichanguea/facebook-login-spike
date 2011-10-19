import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils import create_facebook_test_user
from django.test import TestCase
from django.conf import settings

class FacebookLoginTest(TestCase):
    def test_new_user_can_login_without_existing_facebook_session(self):
        facebook_user_name = 'Dexter Morgan'
        email, password = create_facebook_test_user(facebook_user_name)

        driver = webdriver.Chrome()

        driver.get(settings.SITE_URL)

        login_button = driver.find_element_by_class_name('fb_button_text')
        login_button.click()

        WebDriverWait(driver, 10).until(lambda d : len(d.window_handles) > 1)

        main_window_handler = driver.window_handles[0]
        facebook_popup_handler = driver.window_handles[-1]

        driver.switch_to_window(facebook_popup_handler)

        email_field = driver.find_element_by_name('email')
        email_field.send_keys(email)

        password_field = driver.find_element_by_name('pass')
        password_field.send_keys(password)

        password_field.submit()

        grant_button = driver.find_element_by_name('grant_clicked')
        time.sleep(2)
        grant_button.click()

        driver.switch_to_window(main_window_handler)
        time.sleep(3)
        
        full_name_container = driver.find_element_by_class_name('full_name')
        self.assertEqual(full_name_container.text, facebook_user_name)
        driver.close()
