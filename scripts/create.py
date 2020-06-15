# Importing Statments
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Importing User File
import sys
import os
import inspect
directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(directory)
sys.path.insert(0, parent)

import user


current = user.User(include_repo=True)
USERNAME = current.username
PASSWORD = current.password

browser = webdriver.Chrome(ChromeDriverManager().install()) # installing the latest version of chrome driver
browser.get("https://github.com/login")

# PATH var can be XPATH, CSS Selector, id, Class
'''
PATH = ''
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By., PATH)))
'''


PATH = '''//*[@id="login_field"]'''
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
elemnet.send_keys(USERNAME)

PATH = '''//*[@id="password"]'''
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
elemnet.send_keys(PASSWORD)

PATH = '#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block'
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
elemnet.click()

PATH = 'body > div.position-relative.js-header-wrapper > header > div:nth-child(6) > details > summary > svg'
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
elemnet.click()

PATH = '/html/body/div[1]/header/div[6]/details/details-menu/a[1]'
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
elemnet.click()

PATH = '//*[@id="repository_name"]'
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
elemnet.send_keys(sys.argv[1])
time.sleep(3.5)

PATH = '#new_repository > div.js-with-permission-fields > button'
elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
elemnet.click()

current.save([sys.argv[1]], datetime.datetime.now(), browser.current_url)
current.close(include_repo=True)
