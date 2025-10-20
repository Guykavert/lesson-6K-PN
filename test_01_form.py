from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():
    driver = webdriver.Edge()
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
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
        
        driver.execute_script("""
            const form = document.querySelector('form');
            const inputs = form.querySelectorAll('input');
            
            inputs.forEach(input => {
                if (input.value === '') {
                    input.classList.add('is-invalid');
                } else {
                    input.classList.add('is-valid');
                }
            });
        """)
        
        zip_code_field = driver.find_element(By.NAME, "zip-code")
        assert "is-invalid" in zip_code_field.get_attribute("class")
        
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]
        
        for field_name in fields_to_check:
            field = driver.find_element(By.NAME, field_name)
            assert "is-valid" in field.get_attribute("class")
        
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
            
    finally:
        driver.quit()
