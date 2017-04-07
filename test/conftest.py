import os
import pytest
import time
import string
import urlparse

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException

from constants import (
    BASE_USERNAME,
    BASE_URL,
    BASE_PASSWORD,
    LOGIN_EMAIL_NAME,
    LOGIN_PASSWD_NAME,
    LOGIN_BUTTON_XPATH,
    HEADER_USERID_XPATH,
    MAIN_PAGE_CONTENT_PANE_ID,
    BASE_TITLE,
    LEADS_NAVI_ID,
    LEADS_PROFILE_EDIT_BTN_XPATH,
    LEADS_PROFILE_STATUS_XPATH,
    LEADS_NEW_REMOVE_XPATH,
    LEADS_NEW_CONFIRM_REMOVE_XPATH,
    LEADS_NEW_BUTTON_XPATH,
    LEADS_NEW_FNAME_XPATH,
    LEADS_NEW_LNAME_XPATH,
    LEADS_NEW_COMPANY_XPATH,
    LEADS_NEW_TITLE_XPATH,
    LEADS_NEW_EMAIL_XPATH,
    LEADS_NEW_MOBILE_XPATH,
    LEADS_NEW_PHONE_XPATH,
    LEADS_NEW_STREET_XPATH,
    LEADS_NEW_CITY_XPATH,
    LEADS_NEW_ZIP_XPATH,
    LEADS_NEW_REGION_XPATH,
    LEADS_NEW_COUNTRY_XPATH,
    LEADS_NEW_COUNTRY_INPUT_XPATH,
    LEADS_NEW_STATUS_XPATH ,
    LEADS_NEW_STATUS_INPUT_XPATH ,
    LEADS_NEW_OWNER_XPATH,
    LEADS_NEW_OWNER_INPUT_XPATH,
    LEADS_NEW_SOURCE_XPATH,
    LEADS_NEW_SOURCE_INPUT_XPATH,
    LEADS_NEW_INDUSTRY_XPATH,
    LEADS_NEW_INDUSTRY_INPUT_XPATH,
    LEADS_NEW_TAGS_XPATH,
    LEADS_NEW_SAVE_BUTTON_XPATH,
    DDMENU_SETTINGS_XPATH,
    SETTINGS_LEADS_XPATH,
    SETTINGS_LEADS_STATUS_XPATH,
    TEST_USER_PROFILE
)







BASIC_TIMEOUT=5

@pytest.fixture(scope='session', autouse=True)
def timeout():
    return BASIC_TIMEOUT
	
def login_as_user( driver, username, password, timeout=timeout()):
        driver.find_element_by_name(LOGIN_EMAIL_NAME).send_keys(username)
        driver.find_element_by_name(LOGIN_PASSWD_NAME).send_keys(password)
        time.sleep(timeout)
        driver.find_element_by_xpath(LOGIN_BUTTON_XPATH).click()
        WebDriverWait(driver, 12*timeout).until(expected_conditions.presence_of_element_located((By.ID, MAIN_PAGE_CONTENT_PANE_ID)))

def logged_in_as(driver):
        try:
            userId = driver.find_element_by_xpath(HEADER_USERID_XPATH)
            res = userId.text
        except (NoSuchElementException, WebDriverException):
            res = None
        finally:
            return res

def add_new_lead(driver):
    driver.find_element_by_id(LEADS_NAVI_ID).click()
    time.sleep(5)
    driver.find_element_by_xpath(LEADS_NEW_BUTTON_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_FNAME_XPATH).send_keys(TEST_USER_PROFILE['first_name'])
    driver.find_element_by_xpath(LEADS_NEW_LNAME_XPATH).send_keys(TEST_USER_PROFILE['last_name'])
    driver.find_element_by_xpath(LEADS_NEW_COMPANY_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_TITLE_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_EMAIL_XPATH).send_keys('a@a.pl')
    driver.find_element_by_xpath(LEADS_NEW_MOBILE_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_PHONE_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_STREET_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_CITY_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_ZIP_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_REGION_XPATH).send_keys('a')
    driver.find_element_by_xpath(LEADS_NEW_COUNTRY_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_COUNTRY_INPUT_XPATH).send_keys("Poland")
    driver.find_element_by_xpath(LEADS_NEW_COUNTRY_INPUT_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_STATUS_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_STATUS_INPUT_XPATH).send_keys("New")
    driver.find_element_by_xpath(LEADS_NEW_STATUS_INPUT_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_OWNER_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_OWNER_INPUT_XPATH).send_keys("Mateusz Bochenek")
    driver.find_element_by_xpath(LEADS_NEW_OWNER_INPUT_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_SOURCE_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_SOURCE_INPUT_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_INDUSTRY_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_INDUSTRY_INPUT_XPATH).send_keys("Banks")
    driver.find_element_by_xpath(LEADS_NEW_INDUSTRY_INPUT_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_TAGS_XPATH).click()
    driver.find_element_by_xpath(LEADS_NEW_TAGS_XPATH).send_keys('test_tag')
    driver.find_element_by_xpath(LEADS_NEW_TAGS_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_TAGS_XPATH).send_keys('test_tag2')
    driver.find_element_by_xpath(LEADS_NEW_TAGS_XPATH).send_keys(u'\ue007')
    driver.find_element_by_xpath(LEADS_NEW_SAVE_BUTTON_XPATH).click()
    return driver
    
def change_lead_status_name(driver, oldStatus, newStatus):
    driver.find_element_by_xpath(HEADER_USERID_XPATH).click()
    driver.find_element_by_xpath(DDMENU_SETTINGS_XPATH).click()
    time.sleep(10)
    driver.find_element_by_xpath(SETTINGS_LEADS_XPATH).click()
    driver.find_element_by_xpath(SETTINGS_LEADS_STATUS_XPATH).click()
    driver.find_element_by_xpath("//div[@class='control-group item'][.//h4[text()='"+oldStatus+"']]//button[@class='btn btn-mini edit']").click()
    driver.find_element_by_xpath("//fieldset[.//input[@data-current-value='"+oldStatus+"']]//input").clear()
    driver.find_element_by_xpath("//fieldset[.//input[@data-current-value='"+oldStatus+"']]//input").send_keys(newStatus)
    driver.find_element_by_xpath("//fieldset[.//input[@data-current-value='"+oldStatus+"']]//button[@class='btn btn-primary save']").click()
    return driver

def drop_new_lead(driver):
    driver.find_element_by_id(LEADS_NAVI_ID).click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[text()='"+TEST_USER_PROFILE['first_name'] +" "+TEST_USER_PROFILE['last_name'] +"']").click()
    time.sleep(3)
    driver.find_element_by_xpath(LEADS_PROFILE_EDIT_BTN_XPATH).click()
    time.sleep(3)
    driver.find_element_by_xpath(LEADS_NEW_REMOVE_XPATH).click()
    time.sleep(3)
    driver.find_element_by_xpath(LEADS_NEW_CONFIRM_REMOVE_XPATH).click()
    return driver
    
    
    
    
@pytest.fixture
def as_baseuser( driver, url, baseuser, baseuser_password, timeout):
    if logged_in_as(driver) != baseuser:
        time.sleep(timeout)
        login_as_user(driver, baseuser, baseuser_password)
    return driver
		
@pytest.fixture(scope='session')
def path():
    os.environ['PATH']='./drivers/geckodriver/'+os.pathsep+os.environ['PATH']


@pytest.fixture(scope='session')
def driver(request, timeout):
    a = webdriver.Firefox()
    def _finalizer():
        a.quit()
    
    request.addfinalizer(_finalizer)
    return a




@pytest.fixture(scope='session')
def url():
    return BASE_URL


@pytest.fixture(scope='session')
def baseuser():
    return BASE_USERNAME

@pytest.fixture(scope='session')
def baseuser_password():
    return BASE_PASSWORD
