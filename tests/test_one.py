from main import ui
from pages import home_page
from pages.home_page import Homepage
from settings import BASE_URL


def test_valid_login():
    ui.go_to(BASE_URL)
    Homepage().click_sign_in_button()
