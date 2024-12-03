import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Disable sandboxing
    options.add_argument("--disable-dev-shm-usage")  # Fix potential issues in containerized environments
    options.add_argument("--remote-debugging-port=9222")  # For debugging
    
    # Initialize the driver
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver, username, password):
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    print("Opening LinkedIn login page...")

    # Wait for login elements to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Enter credentials and log in
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    print("Entering login credentials...")
    password_field.send_keys(Keys.RETURN)

    print("Clicking the sign-in button...")
    
    # Wait for login to complete (e.g., check for the redirect)
    WebDriverWait(driver, 10).until(EC.url_changes("https://www.linkedin.com/login"))
    
    current_url = driver.current_url
    print(f"Current URL after waiting: {current_url}")
    
    # Check if login failed and handle it
    if "checkpoint" in current_url:
        print("Login failed. Please complete the login challenge manually if prompted.")
        return False
    return True

def search_jobs(driver):
    try:
        # Navigate to the job search page
        driver.get("https://www.linkedin.com/jobs/")
        print("Navigating to job search page...")

        # Wait for the job search input field to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search by title')]")))

        # Locate the search box and input a job title
        search_box = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search by title')]")
        search_box.send_keys("Software Engineer")
        search_box.send_keys(Keys.RETURN)
        print("Performing job search...")

        # Wait for search results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list")))
        print("Job search completed.")

    except Exception as e:
        print(f"Error locating the search box: {str(e)}")

def main():
    # Initialize WebDriver
    print("Initializing the WebDriver...")
    driver = init_driver()

    # Login to LinkedIn
    username = "your_email@example.com"
    password = "your_password"
    
    print("Opening LinkedIn login page...")
    if not login(driver, username, password):
        driver.quit()
        return

    # Perform job search
    print("Navigating to job search page...")
    search_jobs(driver)

    # Close the browser
    print("Closing the browser...")
    driver.quit()

if __name__ == "__main__":
    main()
