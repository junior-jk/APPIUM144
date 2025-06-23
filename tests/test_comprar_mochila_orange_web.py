from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_comprar_mochila():
    # Inicia o navegador (usa Chrome por padrão)
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verifica que está na tela de produtos
    titulo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products"

    # Clica no produto "Sauce Labs Backpack"
    driver.find_element(By.ID, "item_4_title_link").click()

    # Verifica que está na tela de detalhes
    titulo_detalhes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))
    )
    assert titulo_detalhes.text == "Sauce Labs Backpack"

    # Clica em "Add to cart"
    driver.find_element(By.ID, "add-to-cart").click()

    # Vai para o carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verifica se o produto está no carrinho
    item_no_carrinho = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    assert item_no_carrinho.text == "Sauce Labs Backpack"

    # Vai para checkout
    driver.find_element(By.ID, "checkout").click()

    # Verifica que está na tela de checkout
    titulo_checkout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo_checkout.text == "Your Cart"

    # Fecha o navegador
    driver.quit()
