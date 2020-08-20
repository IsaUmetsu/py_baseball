from selenium.common.exceptions import NoSuchElementException

from selector import getSelector

class Util:
    def __init__(self, driver):
        self.driver = driver

    def getText(self, selector):
        try:
            return self.driver.find_element_by_css_selector(getSelector(selector)).text
        except NoSuchElementException:
            return ""
    
    def getElems(self, selector):
        try:
            return self.driver.find_elements_by_css_selector(getSelector(selector))
        except NoSuchElementException:
            return []

    def getSpecifyText(self, elem, selector):
        try:
            return elem.find_element_by_css_selector(selector).text
        except NoSuchElementException:
            return ""

    def getSpecifyClass(self, elem, selector):
        try:
            return elem.find_element_by_css_selector(selector).get_attribute("class")
        except NoSuchElementException:
            return ""

    def getSpecifyElems(self, elem, selector):
        try:
            return elem.find_elements_by_css_selector(selector)
        except NoSuchElementException:
            return []

    def getTeamText(self, homeAway, selector):
        try:
            fullSelector = getSelector(homeAway) + " " + getSelector(selector)
            return self.driver.find_element_by_css_selector(fullSelector).text
        except NoSuchElementException:
            return ""

    def getTeamElems(self, homeAway, selector):
        try:
            fullSelector = getSelector(homeAway) + " " + getSelector(selector)
            return self.driver.find_elements_by_css_selector(fullSelector)
        except NoSuchElementException:
            return []
