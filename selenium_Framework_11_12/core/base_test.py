import unittest
import logging
from core.browser_manager import BrowserManager

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserManager.get_driver()
        self.driver.get('https://hunkemoller.by')
        logging.info("Browser opened and navigated to https://hunkemoller.by")

    def tearDown(self):
        self.driver.quit()
        logging.info("Browser closed")
