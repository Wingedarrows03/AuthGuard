import os
from datetime import datetime

from utils.logger import get_logger

SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
logger = get_logger(__name__)


def capture_screenshot(driver, test_name: str) -> str:
    """
    Capture a full-page screenshot and save it to ``screenshots/``.

    Parameters
    ----------
    driver : selenium.webdriver.Remote
        The active WebDriver instance.
    test_name : str
        Used in the filename so the screenshot can be traced back to a test.

    Returns
    -------
    str
        Absolute path to the saved PNG file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = test_name.replace(" ", "_").replace("/", "-")
    filename = f"{safe_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(filepath)
    logger.info(f"Screenshot saved: {filepath}")
    return filepath
