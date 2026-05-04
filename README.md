# 🧪 Pre-Entrega - Automatización QA

## 📌 Description
Este proyecto tiene como objetivo automatizar pruebas funcionales básicas sobre el sitio SauceDemo, utilizando Selenium con Python.

Se validan flujos clave como:

- Login de usuario
- Navegación a inventario
- Visualización de productos

El propósito es aplicar los conocimientos adquiridos hasta la Clase 8 del curso, enfocándose en buenas prácticas de automatización QA.

---
## 🌐 Sitio Utilizado

- https://www.saucedemo.com

---

## 🚀 Technologies Used
- Python 3
- Selenium WebDriver
- Pytest
- ChromeDriver
- Git & GitHub

---

## 📂 Project Structure
project/
│
├── tests/
│ └── test_inventory.py
│ └── test_login.py
│
├── utils/
│ └── LoginPage.py
│
├── venv/
└── README.md

---

## ⚙️ Instalación de Dependencias

1. Clonar el repositorio 
git clone https://github.com/Jess-Vp/pre-entrega-automation-testing-jessica-puricelli.git
cd pre-entrega-automation-testing-jessica-puricelli

2. Crear tu entorno virtual 
python -m venv venv

3. Activar entorno virtual:

Mac/ Linux 
source venv/bin/activate 

Windows
venv\Scripts\activate 

4. Instalar dependencias 
pip install -r requirements.txt

--- 

## ▶️ Ejecución de Pruebas

- Para Ejecutar los tests 

pytest -v

- Para generar reporte HTML:
pytest -v --html=reporte.html 

- Ejecutar un test específico (función puntual):
pytest tests/NOMBRE DEL FILE A EJECUTAR


---


## 🧪 Casos de Prueba Implementados 

# Automatización de Login
- Navegación a la página de login
- Ingreso de credenciales válidas:
    Usuario: standard_user
    Contraseña: secret_sauce
- Validación de login exitoso verificando redirección a /inventory.html
- Validación del título "Products"
- Validación del logo "Swag Labs"

# Automatizacion del Inventory
- - Validación del título de la página **"Products"**
- Validación de que existan productos visibles en el inventario
    - Validación del primer producto:
        - El nombre del producto no debe estar vacío
        - El precio debe comenzar con el símbolo `$`
- Validación de la presencia del filtro de productos
- Validación de las opciones disponibles en el filtro:
  - Name (A to Z)
  - Name (Z to A)
  - Price (low to high)
  - Price (high to low)
- Validación del funcionamiento del filtro **Name (Z to A)**
- Validación de que el menú hamburguesa esté visible
- Validación de que el menú hamburguesa se pueda abrir correctamente
- Validación de opciones del menú:
  - All Items
  - About
  - Logout
  - Reset App State
- Cierre del menú hamburguesa

