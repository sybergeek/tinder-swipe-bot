from selenium import webdriver
from time import sleep
from credentials import *

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(8)

        accept_cook_btn = self.driver.find_element_by_xpath("//span[contains(text(),'I accept')]")
        accept_cook_btn.click()
        sleep(8)

        try:
            more_opt_btn = self.driver.find_element_by_xpath("//button[contains(text(),'More options')]")
            more_opt_btn.click()
            sleep(8)
        except:
            pass

        fb_btn = self.driver.find_element_by_xpath("//button[@aria-label='Login with Facebook']")
        fb_btn.click()
        sleep(8)

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(fb_username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(fb_password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(8)
        cont_btn = self.driver.find_element_by_xpath("//button[@value='Continue']")
        cont_btn.click()
        sleep(8)
        log_radio = self.driver.find_element_by_xpath("//span[contains(text(),'Log in with your Google account.')]")
        log_radio.click()
        cont_btn = self.driver.find_element_by_xpath("//button[@value='Continue']")
        cont_btn.click()
        sleep(8)
        login_google = self.driver.find_element_by_xpath("//button[contains(text(),'Log in to Google')]")
        login_google.click()

        # popup 2 for google login
        base_window2 = self.driver.window_handles[1]
        self.driver.switch_to_window(self.driver.window_handles[2])

        email_in = self.driver.find_element_by_xpath("//input[@type='email']")
        email_in.send_keys(google_username)
        nxt_btn = self.driver.find_element_by_xpath("//span[contains(text(),'Next')]")
        nxt_btn.click()
        sleep(8)
        pass_in = self.driver.find_element_by_xpath("//input[@type='password']")
        pass_in.send_keys(google_password)
        nxt_btn = self.driver.find_element_by_xpath("//span[contains(text(),'Next')]")
        nxt_btn.click()
        sleep(8)

        self.driver.switch_to_window(base_window2)
        ok_fb = self.driver.find_element_by_xpath("//input[@value='OK']")
        ok_fb.click()
        sleep(8)
        cont_btn = self.driver.find_element_by_xpath("//button[@value='Continue']")
        cont_btn.click()
        self.driver.switch_to_window(base_window)
        sleep(10)

        try:
            allow_location = self.driver.find_element_by_xpath("//span[contains(text(),'Allow')]")
            allow_location.click()
            sleep(8)
        except:
            pass
        try:
            disable_notif = self.driver.find_element_by_xpath("//span[contains(text(),'Not interested')]")
            disable_notif.click()
            sleep(8)
        except:
            pass
        try:
            no_passport = self.driver.find_element_by_xpath("//span[contains(text(),'No Thanks')]")
            no_passport.click()
        except:
            pass

    def swipe(self):
        while (True):
            try:
                no_passport = self.driver.find_element_by_xpath("//span[contains(text(),'No Thanks')]")
                no_passport.click()
                sleep(1)
            except:
                pass
            try:
                disable_notif = self.driver.find_element_by_xpath("//span[contains(text(),'Not interested')]")
                disable_notif.click()
                sleep(1)
            except:
                pass
            like_btn = self.driver.find_element_by_xpath("//button[@aria-label='Like']")
            like_btn.click()
            sleep(3)
