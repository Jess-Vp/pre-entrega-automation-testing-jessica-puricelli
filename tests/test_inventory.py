import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.LoginPage import login


# Fixture para iniciar sesión antes de cada test y cerrar el navegador después de cada test
@pytest.fixture
def driver_logged():
    driver = webdriver.Chrome()
    login(driver)
    yield driver
    driver.quit()


# Test nº 1: Validar el titulo de la pestaña del inventario
def test_inventory_title(driver_logged):
    title = driver_logged.title
    assert title == "Swag Labs", "El título del navegador no es correcto"


# Test nº 2: Validar que haya productos visibles en el inventario
def test_products_visible(driver_logged):
    products = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No se encontraron productos en la pagina de inventario"


# Test nº 3: Validar que el primer producto tenga nombre y precio válido
def test_first_product_details(driver_logged):
    products = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")

    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    assert first_product_name != "", "El primer producto no tiene nombre"
    assert first_product_price.startswith("$"), "El precio del primer producto no tiene formato correcto"

    print(f"Primer producto: {first_product_name} - Precio: {first_product_price}")


# Test nº 4: Validar que el filtro esté visible y tenga las opciones correctas
def test_filter_options(driver_logged):
    filter_dropdown = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_dropdown.is_displayed(), "El filtro de productos no está visible"

    select = Select(filter_dropdown)
    filter_options = [option.text for option in select.options]

    expected_options = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)"
    ]

    assert filter_options == expected_options, "Las opciones del filtro no son correctas"


# Test nº 5: Validar que el botón del menú hamburguesa sea visible  
def test_ui_elements(driver_logged):
    #Validacion de si existe el menu hamburguesa
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")

    #Funcion del driver que me permite ver si hay elementos visibles en la pagina, devuelve un booleano
    assert menu.is_displayed(), "El icono del menu no está presente en la pagina "
    assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"
