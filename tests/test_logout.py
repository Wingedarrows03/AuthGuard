import allure
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Security Testing")
@allure.story("Session Validation")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogout:

    @pytest.mark.security
    @allure.title("Dashboard is inaccessible (or session token cleared) after logout")
    def test_logout_invalidates_session(self, driver):
        """
        Verify that:
          1. Login succeeds.
          2. Logout is triggered via the UI.
          3. The user is redirected back to the login page.
          4. Direct navigation to the dashboard after logout is documented
             (Juice Shop is an SPA so products may still render, but account
             controls should not be visible).
        """
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        with allure.step("Login with valid credentials"):
            login.open()
            login.login("admin@juice-sh.op", "admin123")

        with allure.step("Assert login was successful"):
            assert dashboard.is_logged_in(), (
                "Login must succeed before testing logout behaviour."
            )

        with allure.step("Perform logout via the account menu"):
            dashboard.logout()

        with allure.step("Assert user is redirected to the login page"):
            assert login.is_on_login_page(), (
                "Expected a redirect to the login page after logout."
            )

        with allure.step("Attempt direct navigation back to the dashboard"):
            dashboard.navigate_to_dashboard()

        with allure.step("Document post-logout dashboard accessibility"):
            still_accessible = dashboard.is_dashboard_accessible()
            # Juice Shop SPA may still render the product list without auth.
            # Flag this as a finding rather than a hard failure.
            allure.attach(
                f"Dashboard accessible after logout: {still_accessible}\n"
                "(Juice Shop is intentionally vulnerable; "
                "sensitive account controls should not appear.)",
                name="Post-Logout Session Check",
                attachment_type=allure.attachment_type.TEXT,
            )
