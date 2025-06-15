from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_com_sucesso():
    # Configurações do Appium
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator-5554",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appium:automationName": "UiAutomator2",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

         # Verificar se foi redirecionado para a tela de produtos
    produto_titulo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"))).text

    assert "Products" in produto_titulo

    
    # Abrir menu lateral
    menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV"))
    )
    menu.click()

    # Clicar em "Login"
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemTV"))
    )
    login.click()

    # Preencher nome e senha
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"))).send_keys("bob@example.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET"))).send_keys("10203040")

    # Clicar em Login
    botao_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn"))
    )
    botao_login.click()

   
  


 
