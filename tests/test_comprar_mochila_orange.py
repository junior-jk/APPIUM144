from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_comprar_mochila_orange():
    # Configurações do Appium (iguais ao anterior)
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator5554",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appium:automationName": "UiAutomator2",
        "browserName": "",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Verifica que está na tela de produtos
    lblSecao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "title"))
    )
    assert lblSecao.text == "Products"

    # Clica na mochila orange (segunda imagem)
    imgMochilaOrange = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='Product Image'])[3]")
        )
    )
    imgMochilaOrange.click()

    # Aguarda a tela de detalhes abrir e valida o nome
    lblNomeProduto2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
        )
    )
    assert lblNomeProduto2.text == "Sauce Labs Backpack (orange)"


    # Valida preço do produto
    lblPrecoProduto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
        )
    )
    assert lblPrecoProduto.text == "$ 29.99"

    # Seleciona cor
    sltCor = WebDriverWait(driver, 12).until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Unknown color")
        )
    )
    sltCor.click()

    # Define quantidade
    txtQuantidade = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV")
        )
    )
    txtQuantidade.click()

    # Adiciona ao carrinho
    btnAdicionarNoCarrinho = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
        )
    )
    btnAdicionarNoCarrinho.click()

    # Acessa o carrinho
    lblCarrinho = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR,
             "new UiSelector().className(\"android.widget.ImageView\").instance(3)")
        )
    )
    lblCarrinho.click()

    # Scroll no carrinho (igual ao anterior)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(530, 1993)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(541, 1202)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    # Encerra a sessão
    driver.quit()
