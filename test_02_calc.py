from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        driver.get(url)

        delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        actual_result = result_element.text
        assert actual_result == "15"
    finally:
        driver.quit()
