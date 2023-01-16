from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By


# An employer has been looking for a developer and hears of Kalenshi
# Kalenshi tells the employer that he has a website where the employer can find detailed information about him
# so the employer visits the website at the url provided by Kalenshi

class TestNewVisitor(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_see_kalenshi_in_title(self) -> None:
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.ID, "idWelcome")
        self.assertIn("Welcome", header)
