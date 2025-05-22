from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time



def test_add_item_to_cart(logged_in):
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

    checkout = driver.find_element(By.CSS_SELECTOR, ".btn_action.checkout_button")
    checkout.click()

    #Wypełnij formularz i zatwierdź
    name = driver.find_element(By.ID, "first-name")
    name.send_keys("John")

    surname = driver.find_element(By.ID, "last-name")
    surname.send_keys("Smith")

    poastal = driver.find_element(By.ID, "postal-code")
    poastal.send_keys("EC2Y")

    conti = driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button")
    conti.click()
    driver.implicitly_wait(3)

    #Checkout
    summary = driver.find_element(By.CSS_SELECTOR, ".summary_info")
    summary_text = summary.text.strip()
    filtered_lines = [
    line for line in summary_text.splitlines()
    if line.strip() not in ["CANCEL", "FINISH", "FREE PONY EXPRESS DELIVERY!"]
]
    cleaned_summary = "\n".join(filtered_lines)
    print(cleaned_summary)

    finish = driver.find_element(By.CSS_SELECTOR, ".btn_action.cart_button")
    finish.click()

    message = driver.find_element(By.CSS_SELECTOR, ".complete-header")
    final_message = message.text.strip()
    print("Has your order been placed: " + final_message)

    
    
    driver.save_screenshot("add_to_cart_result.png")

    
   
    
    
    
    
