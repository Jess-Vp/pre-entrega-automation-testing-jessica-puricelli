from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.LoginPage import login


def test_inventory_validation():
    driver = webdriver.Chrome()

    try:
        login(driver)

        title = driver.find_element(By.CLASS_NAME, "title").text
        assert title == "Products", "El título de la página no es correcto"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos visibles"

        first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        assert first_product_name != "", "El primer producto no tiene nombre"
        assert first_product_price.startswith("$"), "El precio del primer producto no tiene formato correcto"

        print(f"Primer producto: {first_product_name} - Precio: {first_product_price}")

    finally:
        driver.quit()