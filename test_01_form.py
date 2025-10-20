from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)

    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    test_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in test_data.items():
        field = driver.find_element(By.NAME, field_name)
        field.clear()
        if value:
            field.send_keys(value)

    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    submit_btn.click()

    wait.until(EC.url_contains("submitted"))
    assert "data-types-submitted.html" in driver.current_url

    driver.quit()
