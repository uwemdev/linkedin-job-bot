from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def init_driver():
    selenium_url = "http://localhost:4444/wd/hub"  # Connect to the Selenium server
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Use webdriver.Remote with options for Selenium 4
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=chrome_options
    )
    return driver