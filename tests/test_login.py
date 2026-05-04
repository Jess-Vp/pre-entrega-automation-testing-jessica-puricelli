from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.LoginPage import login


def test_login_validation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        login(driver)

        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url, "No se ha redirigido al inventario"

        app_logo = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )

        assert app_logo.text == "Swag Labs", "No se visualiza el logo Swag Labs"

    finally:
        driver.quit()