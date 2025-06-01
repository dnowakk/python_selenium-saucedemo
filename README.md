# Python Selenium – Saucedemo Test Suite

An automated end-to-end test suite for the [SauceDemo](https://www.saucedemo.com/) application using **Selenium WebDriver**, **pytest**, **pytest-html** and **webdriver-manager**. This project demonstrates skills in web application testing using Python.

---

## Project Description

The goal of this project is to automate test scenarios for the [SauceDemo](https://www.saucedemo.com/) application.

The tests are written in Python using Selenium for browser interaction and pytest for test structure and execution.

---

## Requirements

- Python version 3.10 or newer
- Google Chrome browser (latest version recommended)
- All libraries listed in `requirements.txt`

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dnowakk/python_selenium-saucedemo.git
   cd python_selenium-saucedemo
   
2. **Install dependencies:**

pip install -r requirements.txt

3. **Run tests:** 

To run all tests and generate an HTML report:
pytest --html=reports/report.html
After test execution, the report will be available in the reports directory as report.html.


