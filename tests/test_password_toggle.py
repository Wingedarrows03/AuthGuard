import allure
import pytest
from pages.login_page import LoginPage


@allure.feature("Login — Functional")
@allure.story("Password Visibility Toggle")
@allure.severity(allure.severity_level.MINOR)
class TestPasswordToggle:

    @pytest.mark.functional
    @allure.title("Password field toggles between masked and visible states")
    def test_password_visibility_toggle(self, driver):
        """
        Confirm that the eye-icon toggle:
          - Starts in masked state (type='password')
          - Switches to visible (type='text') after first click
          - Reverts to masked (type='password') after second click
        """
        login = LoginPage(driver)

        with allure.step("Open login page"):
            login.open()

        with allure.step("Type a value into the password field"):
            login.enter_password("TestPassword123")

        with allure.step("Assert password is masked by default (type='password')"):
            assert login.get_password_input_type() == "password", (
                "Password field should be masked (type='password') before toggling."
            )

        with allure.step("Click the show-password toggle"):
            login.toggle_password_visibility()

        with allure.step("Assert password is now visible (type='text')"):
            assert login.get_password_input_type() == "text", (
                "Password field should be visible (type='text') after first toggle."
            )

        with allure.step("Click the toggle again to re-mask the password"):
            login.toggle_password_visibility()

        with allure.step("Assert password is masked again (type='password')"):
            assert login.get_password_input_type() == "password", (
                "Password field should be masked again after the second toggle."
            )
