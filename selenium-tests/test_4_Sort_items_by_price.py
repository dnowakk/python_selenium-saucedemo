from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium.webdriver.support.ui import Select


def test_sort_by_price(logged_in):
    driver = logged_in
    driver.implicitly_wait(8)

    # Znajdź <select> (czyli dropdown)
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Utwórz Select
    select = Select(sort_dropdown)

    # Wybierz opcję po wartości
    select.select_by_value("lohi")
    
    # Pobierz wszystkie elementy cen
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    # Wyciągnij wartości jako float
    prices = []
    for price_el in price_elements:
        price_text = price_el.text.replace("$", "").strip()
        prices.append(float(price_text))

    # Walidacja: czy lista jest posortowana rosnąco?
    assert prices == sorted(prices), f"Ceny nie są posortowane rosnąco: {prices}"
    print(sorted(prices))

    driver.implicitly_wait(3)
    
    driver.save_screenshot('Screenshots/4_sort_items_by_price.png')
 
