from pages.login import LoginPage
from pages.products import ProductsPage
import time
    
def test_login_elements(driver):
    login = LoginPage(driver)

    assert login.isDisplayed_username() == True
    assert login.isDisplayed_password() == True
    assert login.isDisplayed_submit() == True

def test_login_valid(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_submit()

    assert products.isDisplayed_container_header() == True
    
def test_login_invalid(driver):
    login = LoginPage(driver)
    expected_error_text = 'Epic sadface: Username and password do not match any user in this service'

    login.enter_username('standard_user')
    login.enter_password('basic_sauce')
    login.click_submit()

    assert login.isDisplayed_error() == True
    assert login.isDisplayed_username() == True
    assert login.isDisplayed_password() == True
    assert login.isDisplayed_submit() == True
    assert login.error_text() == expected_error_text
    
def test_login_locked_out(driver):
    login = LoginPage(driver)
    expected_error_text = 'Epic sadface: Sorry, this user has been locked out.'

    login.enter_username('locked_out_user')
    login.enter_password('secret_sauce')
    login.click_submit()

    assert login.isDisplayed_error() == True
    assert login.isDisplayed_username() == True
    assert login.isDisplayed_password() == True
    assert login.isDisplayed_submit() == True
    assert login.error_text() == expected_error_text