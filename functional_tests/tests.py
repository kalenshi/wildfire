import time

from django.urls import resolve
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestNewVisitor(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_see_the_navigation_bar(self) -> None:
        # Visitor navigates to the main page and is greeted by top bar menu with the following items
        # About, Resume, Projects, Blog, login, signup
        self.browser.get(self.live_server_url)
        main_nav = self.browser.find_element(By.ID, "idMainNav")
        nav_elements = ("About", "Resume", "Projects", "Blog", "login", "Register")
        for nav in nav_elements:
            self.assertIn(nav, main_nav.text)
        time.sleep(5)

    # def test_can_see_a_photo_on_the_main_page(self) -> None:
    #     # Visitor notices a photo of Kalenshi on the front page
    #     photo = self.browser.find_element(By.ID, "idMainPhoto")

    # def test_can_navigate_to_see_a_resume(self) -> None:
    #     # Visitor navigates to Resume and finds information about Kalenshi
    #     ...
    #
    def test_can_navigate_to_about_page(self) -> None:
        # Visitor navigates to about where there's a
        # brief description of what Kalenshi is into.
        self.browser.get(self.live_server_url)
        about = self.browser.find_element(By.LINK_TEXT, "About")
        about.send_keys(Keys.ENTER)
        time.sleep(5)
        location = self.browser.current_url
        self.assertEqual(location, f"{self.live_server_url}/about")

    def test_can_navigate_to_register_page(self) -> None:
        # Visitor navigates to register
        self.browser.get(self.live_server_url)
        register = self.browser.find_element(By.LINK_TEXT, "Register")
        register.send_keys(Keys.ENTER)
        time.sleep(5)
        location = self.browser.current_url
        self.assertEqual(location, f"{self.live_server_url}/register")

    # def test_user_can_create_an_account_and_is_redirected_to_home_page(self) -> None:
    #     """
    #     Tests the user can create an account using email and is
    #     redirected to home page showing user is logged in.
    #     """
    #     self.browser.get(f"{self.live_server_url}/register")
    #     register_form = self.browser.find_element(By.ID, "idRegister")
    #     register.send_keys(Keys.Enter)
    # def test_redirects_to_login_page_after_comment(self) -> None:
    #     # Visitor sees a reply box, types in his contribution, but is redirected to log/register in page
    #     ...
    # # Upon successful account creation, Visitor is redirected to the blog page containing the article he wished
    # # to contribute to.
    # # Visitor successfully adds the contribution to the article
    # # Visitor satisfied by the sight, closes it the web browser
