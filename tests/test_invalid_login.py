import pytest
import allure
from pages.login_page import LoginPage

INVALID_CREDENTIALS = [
    ("wrong@test.com", "wrongpass"),
    ("admin@juice-sh.op", "wrongpass"),
    ("notauser@fake.com", "123456"),
]


@allure.feature("Login — Functional")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
class TestInvalidLogin:

    @pytest.mark.functional
    @pytest.mark.parametrize("username,password", INVALID_CREDENTIALS)
    @allure.title("Invalid credentials show error and keep user on login page")
    def test_invalid_login_shows_error(self, driver, username, password):
        login = LoginPage(driver)

        with allure.step("Open login page"):
            login.open()

        with allure.step(f"Enter invalid credentials — user: {username}"):
            login.login(username, password)

        with allure.step("Assert an error message is displayed"):
            error = login.get_error_message()
            assert error != "", (
                f"Expected an error message but got none for user: {username}"
            )

        with allure.step("Assert the page is still the login page"):
            assert login.is_on_login_page(), (
                "Should remain on the login page after a failed login attempt."
            )
