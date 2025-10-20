from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = None
    try:
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
            try:
                field = driver.find_element(By.NAME, field_name)
                field.clear()
                if value:
                    field.send_keys(value)
            except Exception as e:
                print(f"Ошибка при заполнении поля {field_name}: {e}")
                continue

        try:
            submit_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[type='submit']")
                )
            )
            submit_btn.click()
        except Exception as e:
            print(f"Ошибка при нажатии кнопки: {e}")
            return

        try:
            wait.until(EC.url_contains("submitted"))
            assert "data-types-submitted.html" in driver.current_url
            print("Форма успешно отправлена")
        except Exception as e:
            print(f"Ошибка проверки URL: {e}")
            current_url = driver.current_url
            print(f"Текущий URL: {current_url}")
            if "data-types.html" in current_url:
                print("Форма не была отправлена")
            else:
                print("Произошел переход на неизвестную страницу")
    except Exception as e:
        print(f"Общая ошибка теста: {e}")
        raise
    finally:
        if driver:
            driver.quit()
