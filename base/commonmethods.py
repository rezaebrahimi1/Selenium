from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchCookieException, ElementNotVisibleException
from selenium.webdriver.support.select import Select
import sys
import time
# ======================================================================================================================
class CommonMethods:

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":  # if we set link_text, element can't be finded!!!
            return By.LINK_TEXT
        else:
            print("getByType error: Locator type " + locator_type + "is not correct/supported")
            return False
# ======================================================================================================================

    def get_element(self, locator, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            by_type = self.get_by_type(locatortype)
            element = self.driver.find_element(by_type, locator)
            print(f"getElement msg: element found with locator: {locator} and locator type: {locatortype}")
        except:
            print(f"getElement error: element not found with locator: {locator} and locator type: {locatortype}")
        return element

# ======================================================================================================================

    def is_element_present(self, locator, locatortype="id"):
        try:
            element = self.get_element(locator, locatortype)
            if element is not None:
                print(f"isElementPresent msg: element found with locator: {locator} and locator type: {locatortype}")
                return True
            else:
                return False
        except:
            print(f"isElementPresent error: element not found with locator: {locator} and locator type: {locatortype}")
            return False

# ======================================================================================================================

    def element_presence_check(self, locator, by_type):
        try:
            elementlist = self.driver.find_elements(by_type, locator)
            if len(elementlist) > 0:
                print(f"elementPresenceCheck msg: element found with locator: {locator} and locator type: {by_type}'")
                return True
            else:
                return False
        except:
            print(f"elementPresenceCheck error: element not found with locator: {locator} and locator type: {by_type}'")
            return False

# ======================================================================================================================

    def element_click(self, locator, locatortype='id'):
        try:
            element = self.get_element(locator, locatortype)
            element.click()
            print(f'elementClick msg: click on the element with locator: {locator} and locator type: {locatortype}')
        except:
            print(f"elementClick error: Cannot click on the element with locator: {locator} and locator type: {locatortype}")
            # print_stack()

# ======================================================================================================================

    def send_keys(self, data, locator, locatortype="id"):  # don't use send_keys
        try:
            element = self.get_element(locator, locatortype)
            element.clear()
            element.send_keys(data)
            print(f'sendKeys msg: send keys to element with locator: {locator} and locator type: {locatortype}')
        except:
            print(f"sendKeys error: Cannot send keys to element with locator: {locator} and locator type: {locatortype}")
            # print_stack()

# ======================================================================================================================

    def dropdown_by_index(self, index, locator, locatortype="id"):
        try:
            dropdownelement = self.get_element(locator, locatortype)
            sel = Select(dropdownelement)
            sel.select_by_index(index)
            print(f'dropDownByindex msg: find dropdown element with locator: {locator} and locator type: {locatortype} and index: {index}')
        except:
            print(f"dropDownByindex error: Cannot find dropdown element with locator: {locator} and locator type: {locatortype} and index: {index}")
            # print_stack()

# ======================================================================================================================

    def dropdown_by_text(self, visible_text, locator, locatortype="id"):
        try:
            dropdownelement = self.get_element(locator, locatortype)
            sel = Select(dropdownelement)
            sel.select_by_visible_text(visible_text)
            print(f'dropDownByText msg: find dropdown element with locator: {locator} and locator type: {locatortype} and text: {visible_text}')
        except:
            print(f"dropDownByText error: Cannot find dropdown element with locator: {locator} and locator type: {locatortype} and text: {visible_text}")
            # print_stack()

# ======================================================================================================================

    def wait_for_element_frequency(self, locator, locatortype='id', timeout=10, pollfrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locatortype)
            print("waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[NoSuchCookieException, ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print(f"waitForElementFrequency msg: Element appeared on the web page with locator: {locator} and locatortype: {locatortype}")
        except:
            print(f"waitForElementFrequency error: Element not appeared on the web page with locator: {locator} and locatortype: {locatortype}")
            # print_stack()

        return element

# ======================================================================================================================

    def wait_for_element(self, locator, locator_type='id', wait_method='click', timeout=10):

        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout)
            if wait_method == "click":
                time.sleep(0.1)
                wait.until(EC.element_to_be_clickable((by_type, locator)))
                print("waiting for maximum : " + str(timeout) + " seconds for element to be clickable")
            elif wait_method == "visible":
                time.sleep(0.1)
                wait.until(EC.visibility_of_element_located((by_type, locator)))
                print("waiting for maximum : " + str(timeout) + " seconds for element to be visible")
            elif wait_method == "invisible":
                time.sleep(0.1)
                wait.until(EC.invisibility_of_element_located((by_type, locator)))
                print("waiting for maximum : " + str(timeout) + " seconds for element to be invisible")
            elif wait_method == "presence":
                wait.until(EC.presence_of_element_located((by_type, locator)))
                print("waiting for maximum : " + str(timeout) + " seconds for element to be present")

            print(f"waitForElement msg: Element appeares on the web page by locator: {locator} and locatortype: {locator_type}")
        except:
            print(f"waitForElement error: Element doesn't appear on the web page by locator: {locator} and locatortype: {locator_type}")
            # print_stack()

# ======================================================================================================================

    def title_contains(self, text, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.title_contains(text))

# ======================================================================================================================

    def title_is(self, text, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.title_is(text))

# ======================================================================================================================

    def table_split(self, locator, locator_type="xpath"):
        by_type = self.get_by_type(locator_type)
        if locator == "xpath":
            rows = self.driver.find_elements(by_type, locator + '//tr')
        else:
            rows = self.driver.find_element(by_type, locator)

        table = []
        try:
            for i in range(len(rows)):
                table.append([])
                cells = self.driver.find_elements_by_xpath(locator + "//tr[" + str(i + 1) + "]/td")
                for j in range(len(cells)):
                    table[i].insert(j, cells[j].text)
        except:
            print("."), sys.exc_info()[1]
        return table

# ======================================================================================================================

    def get_title(self):
        return self.driver.title

# ======================================================================================================================

    def element_is_displayed(self, locator, locator_type='id'):
        by_type = self.get_by_type(locator_type)
        elem_is_displayed = self.driver.find_element(by_type, locator).is_displayed()
        if elem_is_displayed == True:
            print(f"elementDisplayCheck msg: element with locator: {locator} and locator type: {by_type} is displayed.")
            return True
        else:
            print(f"elementDisplayCheck msg: element with locator: {locator} and locator type: {by_type} is not displayed.")
            return False
