# Importing Statments
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException # for try/except block
import shutil

# Importing User/Methods File
import sys
import os
import inspect
directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(directory)
sys.path.insert(0, parent)

import user
import Methods

current = user.User(include_repo=True)
USERNAME = current.username
PASSWORD = current.password

if sys.argv[1] in current._repo:
    delete()
else: 
    print('You have no repository with the name of {}'.format(sys.argv[1]))

def delete():
    '''Commands Will be in the Method To reference it easilly into the if block'''
    # Delete The File
    shutil.rmtree("e:/projects/{}".format(sys.argv[1]), onerror=Methods.rmtree_onerror)

    # Delete Online Repository
    browser = webdriver.Chrome(ChromeDriverManager().install()) # installing the latest version of chrome driver
    browser.get("""https://github.com/{}/{}""".format(USERNAME, sys.argv[1]))

    PATH = '''body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.d-flex.flex-justify-between.flex-items-center.flex-auto > div.d-flex.flex-items-center.px-0.text-center.text-left > a.HeaderMenu-link.no-underline.mr-3'''
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
    elemnet.click()

    PATH = '''//*[@id="login_field"]'''
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
    elemnet.send_keys(USERNAME)

    PATH = '''//*[@id="password"]'''
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
    elemnet.send_keys(PASSWORD)

    PATH = '#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block'
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
    elemnet.click()

    PATH = '#js-repo-pjax-container > div.pagehead.repohead.hx_repohead.readability-menu.bg-gray-light.pb-0.pt-3 > nav > ul > li:nth-child(9) > a'
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
    elemnet.click()

    PATH = '#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > summary'
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
    elemnet.click()

    PATH = '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input'
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
    elemnet.send_keys("{}/{}".format(USERNAME, sys.argv[1]))

    PATH = '#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > details-dialog > div.Box-body.overflow-auto > form > button'
    elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
    elemnet.click()

    try:
        PATH = '''//*[@id="password"]'''
        elemnet = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located((By.XPATH, PATH)))
        
    except TimeoutException:
        browser.quit()

    else:
        PATH = '''//*[@id="password"]'''
        elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, PATH)))
        elemnet.send_keys(PASSWORD)

        PATH = '#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block'
        elemnet = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PATH)))
        elemnet.click()

        browser.quit()