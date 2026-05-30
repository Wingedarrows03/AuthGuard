import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Classic and common SQL injection payloads targeting login forms
SQL_PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "admin' --",
    "admin'/*",
    '" OR ""="',
    "1' ORDER BY 1--",
    "' UNION SELECT null --",
]


@allure.feature("Security Testing")
@allure.story("SQL Injection")
@allure.severity(allure.severity_level.CRITICAL)
class TestSQLInjection:

    @pytest.mark.security
    @pytest.mark.parametrize("payload", SQL_PAYLOADS)
    @allure.title("SQL injection payload is blocked: {payload}")
    def test_sql_injection_blocked(self, driver, payload):
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        with allure.step("Open the login page"):
            login.open()

        with allure.step(f"Submit SQL injection payload as username: {payload}"):
            login.login(payload, "anything")

        with allure.step("Assert the injection did NOT result in a successful login"):
            is_logged_in = dashboard.is_logged_in()
            assert not is_logged_in, (
                f"CRITICAL VULNERABILITY: SQL injection succeeded with payload: {payload}"
            )

        allure.attach(
            payload,
            name="Injection Payload Used",
            attachment_type=allure.attachment_type.TEXT,
        )
