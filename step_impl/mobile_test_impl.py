from appium import webdriver
from getgauge.python import step, before_scenario, Messages
import os
@step("do a mobile conf")
def do_a_mobile_conf():
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = '4f819e1a'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/OpsForce_5.7-debug1.apk'))
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

