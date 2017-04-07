import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException
from constants import (
    BASE_TITLE,
    LEADS_NAVI_ID,
    LEADS_PROFILE_STATUS_XPATH,
    TEST_USER_PROFILE
)

from conftest import logged_in_as,change_lead_status_name, add_new_lead, drop_new_lead

class TestBaseLeadStatus(object):

    

    def test_get(self, driver, url):
        driver.get(url)
        assert BASE_TITLE in driver.title

    def test_login(self, as_baseuser, baseuser):
        assert logged_in_as(as_baseuser) == TEST_USER_PROFILE['abbrv']
    
    def test_add_new_lead(self,driver, timeout):
        add_new_lead(driver)
        time.sleep(15)

    def test_change_lead_status_name(self, driver, oldStatus='New', newStatus='TestStatus'):
        change_lead_status_name(driver, oldStatus, newStatus)
        driver.find_element_by_id(LEADS_NAVI_ID).click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[text()='"+TEST_USER_PROFILE['first_name'] +" "+TEST_USER_PROFILE['last_name'] +"']").click()
        time.sleep(10)
        assert driver.find_element_by_xpath(LEADS_PROFILE_STATUS_XPATH).text == newStatus
        
    def test_cleanup_settings(self, driver, oldStatus='New', newStatus='TestStatus'):
        change_lead_status_name(driver, newStatus, oldStatus)
        time.sleep(5)
        drop_new_lead(driver)

        
        
        

    
