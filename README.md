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

https://www.saucedemo.com

---

## 🚀 Technologies Used
- Python 3
- Selenium WebDriver
- Pytest
- ChromeDriver
- Git & GitHub

---

## 📂 Project Structure

```text
project/
│
├── tests/
│   ├── test_inventory.py
│   └── test_login.py
│
├── utils/
│   └── LoginPage.py
│
├── venv/
└── README.md
```

---


## Instalación de Dependencias

1. Clonar el repositorio: 
```bash
git clone https://github.com/Jess-Vp/pre-entrega-automation-testing-jessica-puricelli.git
cd pre-entrega-automation-testing-jessica-puricelli
```

2. Crear tu entorno virtual:  
```bash
python -m venv venv
```

3. Activar entorno virtual:
```bash

  - Mac/ Linux 

  source venv/bin/activate 

  - Windows

  venv\Scripts\activate 
  ```

4. Instalar dependencias 
```bash
pip install -r requirements.txt
```

--- 

## ▶️ Ejecución de Pruebas

Para Ejecutar los tests: 
```bash
pytest -v
```

Para generar reporte HTML:
```bash
pytest -v --html=reporte.html 
```

Ejecutar un test específico (función puntual):
```bash
pytest tests/NOMBRE DEL FILE A EJECUTAR
```
---


## 🧪 Casos de Prueba Implementados 

### Automatización de Login
- Navegación a la página de login
- Ingreso de credenciales válidas:
    Usuario: standard_user
    Contraseña: secret_sauce
- Validación de login exitoso verificando redirección a /inventory.html
- Validación del título "Products"
- Validación del logo "Swag Labs"


### Automatizacion del Inventory
- Validación del título de la pestaña del navegador:
  - Se espera que el título sea **"Swag Labs"**

- Validación de productos visibles:
  - Se verifica que exista al menos un producto en la página de inventario

- Validación del primer producto:
  - El nombre del producto no debe estar vacío
  - El precio debe comenzar con el símbolo `$`

- Validación del filtro de productos:
  - Se verifica que el filtro esté visible
  - Se validan las opciones disponibles:
    - Name (A to Z)
    - Name (Z to A)
    - Price (low to high)
    - Price (high to low)

- Validación de elementos de la interfaz:
  - Se verifica que el botón del menú hamburguesa esté visible
  - Se verifica que el filtro del catálogo esté visible

