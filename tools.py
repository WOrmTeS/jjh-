import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import time
import random

def load_targets():
    with open("targets.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def load_accounts():
    with open("accounts.txt", "r") as f:
        return [tuple(line.strip().split(":")) for line in f.readlines()]

def log_report(target, status):
    with open("report_log.txt", "a") as log:
        log.write(f"{target} => {status}\n")

def random_sleep(a=3, b=7):
    time.sleep(random.uniform(a, b))

def login(username, password):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = uc.Chrome(options=options)
    
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")

    user_input.send_keys(username)
    pass_input.send_keys(password)
    
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(7)
    
    return driver

def report_target(driver, username, reason="scam"):
    try:
        driver.get(f"https://www.instagram.com/{username}/")
        random_sleep(4,6)
        
        options_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Options')]")
        options_btn.click()
        random_sleep()

        report_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Report')]")
        report_btn.click()
        random_sleep()

        if reason == "scam":
            driver.find_element(By.XPATH, "//button[contains(text(), 'Report Account')]").click()
            random_sleep()
            driver.find_element(By.XPATH, "//button[contains(text(), 'It’s pretending to be someone else')]").click()
            random_sleep()
            driver.find_element(By.XPATH, "//button[contains(text(), 'A business or organization')]").click()
        
        elif reason == "hate":
            driver.find_element(By.XPATH, "//button[contains(text(), 'Report Account')]").click()
            random_sleep()
            driver.find_element(By.XPATH, "//button[contains(text(), 'Posting hate speech or symbols')]").click()

        elif reason == "impersonation":
            driver.find_element(By.XPATH, "//button[contains(text(), 'Report Account')]").click()
            random_sleep()
            driver.find_element(By.XPATH, "//button[contains(text(), 'It’s pretending to be someone else')]").click()
            random_sleep()
            driver.find_element(By.XPATH, "//button[contains(text(), 'Me')]").click()

        log_report(username, "Reported")
        print(f"[+] {username} reported.")
    
    except Exception as e:
        log_report(username, "Failed")
        print(f"[-] Failed to report {username}: {str(e)}")

if __name__ == "__main__":
    targets = load_targets()
    accounts = load_accounts()
    
    for user, pwd in accounts:
        print(f"\n[>] Logging in as {user}")
        driver = login(user, pwd)
        for target in targets:
            report_target(driver, target, reason="scam")
            random_sleep(5, 10)
        driver.quit()
        print(f"[=] Finished reports with {user}")
        time.sleep(10)