from selenium.webdriver.common.by import By
from .common import CommonOps

class LoginPage(CommonOps):

    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'login-button')
    ERROR_TEXT = (By.XPATH, '//h3[@data-test="error"]')
    
    def isDisplayed_username(self):
        return self.is_displayed(self.USERNAME_FIELD)
    
    def isDisplayed_password(self):
        return self.is_displayed(self.PASSWORD_FIELD)
    
    def isDisplayed_submit(self):
        return self.is_displayed(self.SUBMIT_BUTTON)

    def enter_username(self, username):
        self.wait_for(self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.PASSWORD_FIELD).send_keys(password)

    def click_submit(self):
        self.wait_for(self.SUBMIT_BUTTON).click()
    
    def isDisplayed_error(self):
        return self.is_displayed(self.ERROR_TEXT)

    def error_text(self):
        return self.wait_for(self.ERROR_TEXT).text