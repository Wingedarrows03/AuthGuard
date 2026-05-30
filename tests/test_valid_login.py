import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Login — Functional")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.BLOCKER)
class TestValidLogin:

    @allure.title("Valid credentials result in successful login")
    @pytest.mark.functional
    def test_valid_login_success(self, driver):
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        with allure.step("Open login page"):
            login.open()

        with allure.step("Enter valid credentials"):
            login.login("admin@juice-sh.op", "admin123")

        with allure.step("Assert dashboard is accessible after login"):
            assert dashboard.is_logged_in(), (
                "Expected dashboard to load after valid login."
            )
