from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_items(logged_in):
    driver = logged_in


    # Poczekaj, aż załadują się produkty
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    # Poczekaj, aż pojawią się przyciski "Add to cart"
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.btn_inventory"))
    )

    # Znajdź wszystkie przyciski Add to cart
    add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")

    # Znajdź wszystkie produkty
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Asercja
    assert len(add_to_cart_buttons) == len(products), (
        f"Oczekiwano {len(products)} przycisków, znaleziono {len(add_to_cart_buttons)}"
    )

    # Screenshot
    driver.save_screenshot('Screenshots/5_Add_to_cart_buttons.png')