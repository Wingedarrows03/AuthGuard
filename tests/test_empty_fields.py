import pytest
import allure
from pages.login_page import LoginPage

EMPTY_FIELD_CASES = [
    ("", "somepassword", "empty username"),
    ("admin@juice-sh.op", "", "empty password"),
    ("", "", "both fields empty"),
]


@allure.feature("Login — Functional")
@allure.story("Empty Field Validation")
@allure.severity(allure.severity_level.NORMAL)
class TestEmptyFields:

    @pytest.mark.functional
    @pytest.mark.parametrize("username,password,case", EMPTY_FIELD_CASES)
    @allure.title("Empty fields prevent login — case: {case}")
    def test_empty_fields_block_login(self, driver, username, password, case):
        login = LoginPage(driver)

        with allure.step("Open login page"):
            login.open()

        with allure.step(f"Submit form with {case}"):
            login.login(username, password)

        with allure.step("Assert login was blocked (still on login page OR error shown)"):
            on_login = login.is_on_login_page()
            error = login.get_error_message()
            assert on_login or error != "", (
                f"Expected login to be blocked for case: '{case}', "
                f"but neither an error was shown nor the URL stayed on the login page."
            )
