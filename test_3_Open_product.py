from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time



def test_add_item_to_cart(logged_in):
    driver = logged_in
    select_item = driver.find_element(By.ID, "item_5_title_link")
    select_item.click()
    
    driver.implicitly_wait(3)
    
    

    driver.save_screenshot("selected_item.png")

    
