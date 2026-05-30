import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)


def get_driver(browser: str = None) -> webdriver.Remote:
    """
    Initialise and return a Selenium WebDriver instance.

    Parameters
    ----------
    browser : str, optional
        ``"chrome"`` or ``"firefox"``; falls back to the ``BROWSER`` env var
        (default ``"chrome"``).

    Returns
    -------
    webdriver.Remote
        A fully configured, maximised WebDriver instance.
    """
    browser = (browser or os.getenv("BROWSER", "chrome")).lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    logger.info(f"Initializing {browser.upper()} driver (headless={headless})")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
    else:
        raise ValueError(
            f"Unsupported browser: '{browser}'. Use 'chrome' or 'firefox'."
        )

    driver.implicitly_wait(int(os.getenv("IMPLICIT_WAIT", 10)))
    driver.set_page_load_timeout(int(os.getenv("PAGE_LOAD_TIMEOUT", 30)))
    driver.maximize_window()
    logger.info("Driver initialized successfully.")
    return driver
