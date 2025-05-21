from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_sorting_low_to_high(logged_in):
    driver = logged_in
    driver.implicitly_wait(8)

    # Znajdź dropdown i wybierz opcję "Price (low to high)"
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(sort_dropdown)
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

    # Zapisz zrzut ekranu (opcjonalnie)
    driver.save_screenshot("sorted_prices_validation.png")