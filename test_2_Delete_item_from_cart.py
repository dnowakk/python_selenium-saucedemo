from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


#Odwołanie do conftest.py
def test_delete_items(logged_in):
    driver = logged_in

    # Kliknij "Add to cart"
    add_cart = driver.find_element(By.CLASS_NAME, "btn_primary")
    add_cart.click()

    # Kliknij ikonę koszyka
    open_cart = driver.find_element(By.ID, "shopping_cart_container")
    open_cart.click()

    # Pobierz ilość z koszyka
    quantity_element = driver.find_element(By.CSS_SELECTOR, ".cart_quantity")
    quantity_text = quantity_element.text.strip()

    # Wypisz i sprawdź
    print(f"Quantity in cart: {quantity_text}")
    assert float(quantity_text) == 1, f"Oczekiwano ilości 1, ale było {quantity_text}"

    #Usuń z koszyka
    remove = driver.find_element(By.CSS_SELECTOR, ".btn_secondary.cart_button")
    remove.click()

    keep_shopping = driver.find_element(By.CSS_SELECTOR, ".btn_secondary")
    keep_shopping.click()

    #Sprawdź czy widoczny jest tytuł
    title = driver.find_element(By.CLASS_NAME, "product_label")
    title_text = title.text.strip()
    assert(title_text) == "Products"
    
    driver.save_screenshot('Screenshots/2_continue_shopping.png')