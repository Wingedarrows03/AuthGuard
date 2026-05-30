import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
LOGIN_URL = f"{BASE_URL}/#/login"


class LoginPage:
    """
    Page Object for the OWASP Juice Shop login page.

    Encapsulates all locators and interactions so test code stays clean
    and locator changes only need to be updated in one place.
    """

    # ── Locators ──────────────────────────────────────────────────────────
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'mat-error') or contains(@class,'error')]",
    )
    PASSWORD_TOGGLE = (
        By.XPATH,
        "//mat-icon[contains(text(),'visibility') or contains(text(),'visibility_off')]",
    )
    FORGOT_PASSWORD = (
        By.XPATH,
        "//a[contains(text(),'Forgot') or contains(@href,'forgot')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ── Navigation ────────────────────────────────────────────────────────

    def open(self):
        """Navigate directly to the login URL."""
        logger.info(f"Navigating to: {LOGIN_URL}")
        self.driver.get(LOGIN_URL)

    # ── Field interactions ─────────────────────────────────────────────────

    def enter_username(self, username: str):
        """Clear and type into the email/username field."""
        logger.info(f"Entering username: {username}")
        field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password: str):
        """Clear and type into the password field (value redacted in logs)."""
        logger.info("Entering password: [REDACTED]")
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        """Click the login / submit button."""
        logger.info("Clicking login button")
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        btn.click()

    def login(self, username: str, password: str):
        """Convenience: fill both fields and click login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Assertions / getters ───────────────────────────────────────────────

    def get_error_message(self) -> str:
        """Return the visible error message text, or an empty string if absent."""
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            msg = el.text.strip()
            logger.info(f"Error message found: {msg}")
            return msg
        except Exception:
            logger.warning("No error message element found.")
            return ""

    def toggle_password_visibility(self):
        """Click the eye-icon toggle to show/hide the password."""
        logger.info("Toggling password visibility")
        btn = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_TOGGLE))
        btn.click()

    def get_password_input_type(self) -> str:
        """Return the ``type`` attribute of the password input (``'password'`` or ``'text'``)."""
        field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        return field.get_attribute("type")

    def click_forgot_password(self):
        """Click the 'Forgot Password' link."""
        logger.info("Clicking Forgot Password link")
        link = self.wait.until(EC.element_to_be_clickable(self.FORGOT_PASSWORD))
        link.click()

    def is_on_login_page(self) -> bool:
        """Return True when the current URL contains 'login'."""
        return "login" in self.driver.current_url.lower()
