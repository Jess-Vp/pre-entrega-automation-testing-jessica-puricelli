from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.LoginPage import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_inventory_validation():
    driver = webdriver.Chrome()

    try:
        login(driver)

        # Revisar el titulo de la página
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert title == "Products", "El título de la página no es correcto"

        # Check que los productos esten visibles
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos visibles"

        # Validacion del primer producto: nombre y precio
        first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        assert first_product_name != "", "El primer producto no tiene nombre"
        assert first_product_price.startswith("$"), "El precio del primer producto no tiene formato correcto"

        print(f"Primer producto: {first_product_name} - Precio: {first_product_price}")

        # Validacion presencia del filtro
        filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filter_dropdown.is_displayed(), "El filtro de productos no está visible"

        # Validacion opciones del filtro
        select = Select(filter_dropdown)
        filter_options = [option.text for option in select.options]

        expected_options = [
            "Name (A to Z)",
            "Name (Z to A)",
            "Price (low to high)",
            "Price (high to low)"
        ]

        assert filter_options == expected_options, "Las opciones del filtro no son correctas"

        # Validar funcionamiento del filtro Name Z to A
        select.select_by_visible_text("Name (Z to A)")

        sorted_products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_names = [product.text for product in sorted_products]

        assert product_names == sorted(product_names, reverse=True), \
            "El filtro Name (Z to A) no ordena correctamente los productos"
        

        wait = WebDriverWait(driver, 10)

        # Validar menu hamburguesa
        menu_button = wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        assert menu_button.is_displayed(), "El botón del menú hamburguesa no está visible"

        menu_button.click()


        # Validar que el menu se despliega
        menu_container = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap"))
        )
        assert menu_container.is_displayed(), "El menú hamburguesa no se abrió correctamente"


        # Validar opciones del menú
        expected_menu_options = ["All Items", "About", "Logout", "Reset App State"]
        menu_options = wait.until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "bm-item"))
        )
        menu_options_text = [option.text.strip() for option in menu_options if option.text != ""]
   
        print("Opciones esperadas:", expected_menu_options)
        print("Opciones capturadas:", menu_options_text) 


        # Cerrar el menú
        close_button = wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
        )
        close_button.click()

         
    finally:
        driver.quit()

        