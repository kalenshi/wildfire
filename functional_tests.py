from selenium import webdriver
import unittest


# An employer has been looking for a developer and hears of Kalenshi
# Kalenshi tells the employer that he has a website where the employer can find detailed information about him
# so the employer visits the website at the url provided by Kalenshi

class TestNewVisitor(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_see_kalenshi_in_title(self) -> None:
        self.browser.get("http://localhost:8000")
        assert "Kalenshi" in self.browser.title


if __name__ == "__main__":
    unittest.main()
