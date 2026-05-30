import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")


class DashboardPage:
    """
    Page Object for the OWASP Juice Shop main dashboard / product listing page.

    Used primarily to verify that a login succeeded and to perform logout,
    as well as to check post-logout session behaviour.
    """

    # ── Locators ──────────────────────────────────────────────────────────
    ACCOUNT_MENU = (By.ID, "navbarAccount")
    LOGOUT_BUTTON = (By.ID, "navbarLogoutButton")
    PRODUCT_ITEM = (By.CLASS_NAME, "mat-card")
    SEARCH_BOX = (By.ID, "searchQuery")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ── Status checks ──────────────────────────────────────────────────────

    def is_logged_in(self) -> bool:
        """Return True when the account menu (only visible after login) appears."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_MENU))
            logger.info("Dashboard loaded — user is logged in.")
            return True
        except Exception:
            logger.warning("Dashboard not detected — login may have failed.")
            return False

    def is_dashboard_accessible(self) -> bool:
        """Return True when the product grid is visible (page rendered)."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ITEM))
            return True
        except Exception:
            return False

    # ── Actions ────────────────────────────────────────────────────────────

    def logout(self):
        """Click the account menu then the logout button."""
        logger.info("Attempting logout")
        self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        logger.info("Logout action performed.")

    def navigate_to_dashboard(self):
        """Navigate directly to the shop home page."""
        logger.info(f"Navigating directly to: {BASE_URL}/#/")
        self.driver.get(f"{BASE_URL}/#/")
