from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_products(login_in_driver):
    driver = login_in_driver

    #Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME,"btn_inventory")[0].click()

    #Verificar contador del carrito
    counter_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    assert counter_cart.text == "1", "El producto no se agregó al carrito correctamente"

    #Obtener el nombre del primer producto enlistado en la pagina de inventario
    product_name = driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text

    # Verificar que el producto en el carrito sea el mismo que se agregó por medio del nombre 
    assert cart_item == product_name, "El producto en el carrito no coincide con el producto agregado"