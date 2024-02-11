from selenium.webdriver.common.by import By
from .common import CommonOps

class ProductsPage(CommonOps):

    CONTAINER_HEADER_TEXT = (By.XPATH, '//span[@class="title"][text()="Products"]')
    
    def isDisplayed_container_header(self):
        return self.is_displayed(self.CONTAINER_HEADER_TEXT)