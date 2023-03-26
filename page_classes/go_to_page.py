from base.commonmethods import CommonMethods
import time


class GoToPage(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

# == Locators ==========================================================================================================

    _storage_menu = "your-locator"
    _pool_link = "your-locator"

# == Methods ==========================================================================================================

    def click_storage_menu(self):
        # time.sleep(0.1)
        self.wait_for_element(self._storage_menu, locator_type="linktext", wait_method="click", timeout=20)
        self.element_click(self._storage_menu, locatortype="linktext")

    def click_pool_link(self):
        self.wait_for_element(self._pool_link, locator_type="linktext", wait_method="click", timeout=20)
        self.element_click(self._pool_link, locatortype="linktext")
        self.title_contains("Pool", 10)