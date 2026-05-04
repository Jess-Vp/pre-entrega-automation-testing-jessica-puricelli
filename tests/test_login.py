from selenium import webdriver
from utils.LoginPage import login


def test_login_validation():
    driver = webdriver.Chrome()

    try:
        login(driver)

        assert "/inventory.html" in driver.current_url, "No se ha redirigido al inventario"

    finally:
        driver.quit()