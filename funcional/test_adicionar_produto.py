from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_adicionar_produtos_ao_carrinho():
    print("Iniciando o teste...")

    servico = Service("C:/WebDrivers/chromedriver.exe")
    driver = webdriver.Chrome(service=servico)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    print("Página carregada")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    print("Produtos adicionados ao carrinho")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    itens = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    nomes_dos_itens = [item.text for item in itens]

    print("Itens no carrinho:", nomes_dos_itens)

    assert "Sauce Labs Backpack" in nomes_dos_itens
    assert "Sauce Labs Bike Light" in nomes_dos_itens

    print("Teste concluído com sucesso!")
    driver.quit()

    print("Finalizando o teste...")
if __name__ == "__main__":
    test_adicionar_produtos_ao_carrinho()
    print("Teste executado com sucesso!")