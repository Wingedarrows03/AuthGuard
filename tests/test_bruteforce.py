import time

import allure
import pytest
from pages.login_page import LoginPage

ATTEMPT_COUNT = 10
TARGET_EMAIL = "admin@juice-sh.op"


@allure.feature("Security Testing")
@allure.story("Brute Force Simulation")
@allure.severity(allure.severity_level.CRITICAL)
class TestBruteForce:

    @pytest.mark.security
    @allure.title("Repeated failed logins trigger lockout, CAPTCHA, or warning")
    def test_brute_force_lockout(self, driver):
        """
        Submit ATTEMPT_COUNT wrong passwords in succession and check whether
        the application responds with any protective mechanism.

        NOTE: OWASP Juice Shop intentionally has *no* brute-force protection
        (it is a deliberately vulnerable app).  If no protection is found,
        the test is marked xfail so the finding is recorded without causing a
        hard failure — this is a documented security gap, not a test bug.
        """
        login = LoginPage(driver)
        login.open()

        lockout_detected = False
        captcha_detected = False
        warning_detected = False

        for attempt in range(1, ATTEMPT_COUNT + 1):
            with allure.step(f"Attempt {attempt}: submit wrong password"):
                login.enter_username(TARGET_EMAIL)
                login.enter_password(f"wrongpass_{attempt}")
                login.click_login()
                time.sleep(0.5)  # brief pause to allow server response

                error = login.get_error_message().lower()
                page_src = driver.page_source.lower()

                if any(
                    kw in error
                    for kw in ["locked", "too many", "blocked", "suspended"]
                ):
                    lockout_detected = True
                    break
                if "captcha" in page_src or "recaptcha" in page_src:
                    captcha_detected = True
                    break
                if "warning" in error or "unusual" in error:
                    warning_detected = True

        result_summary = (
            f"Lockout detected  : {lockout_detected}\n"
            f"CAPTCHA detected  : {captcha_detected}\n"
            f"Warning detected  : {warning_detected}\n"
            f"Attempts made     : {ATTEMPT_COUNT}"
        )
        allure.attach(
            result_summary,
            name="Brute Force Detection Result",
            attachment_type=allure.attachment_type.TEXT,
        )

        if not (lockout_detected or captcha_detected or warning_detected):
            pytest.xfail(
                f"No brute-force protection detected after {ATTEMPT_COUNT} attempts "
                "— this is a known Juice Shop vulnerability (intentional design)."
            )
