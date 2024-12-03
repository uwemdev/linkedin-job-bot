from selenium.webdriver.common.by import By
import time

def search_jobs(driver, keywords, location):
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"
    driver.get(search_url)
    time.sleep(5)  # Wait for page to load
    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
    return jobs