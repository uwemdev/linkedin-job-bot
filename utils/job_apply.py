from selenium.webdriver.common.by import By
import time

def apply_to_job(driver, job):
    job.click()
    time.sleep(3)  
    try:
        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        apply_button.click()
        time.sleep(5)  
       
        submit_button = driver.find_element(By.XPATH, '//button[@data-control-name="submit_unify"]')
        submit_button.click()
        time.sleep(5)  # Wait for submission
    except Exception as e:
        print(f"Error applying to job: {e}")
