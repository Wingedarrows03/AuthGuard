"""
conftest.py — Shared PyTest fixtures and hooks for AuthGuard.

Provides:
  - ``driver`` fixture  : per-test WebDriver lifecycle
  - Screenshot capture  : automatic on test failure, attached to Allure report
  - Folder creation     : ensures logs / screenshots / allure-results exist
"""

import os
from pathlib import Path

import allure
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from utils.logger import get_logger
from utils.screenshot import capture_screenshot

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")

logger = get_logger("conftest")


def pytest_configure(config):
    """Create output folders before the test run begins."""
    for folder in (
        PROJECT_ROOT / "logs",
        PROJECT_ROOT / "screenshots",
        PROJECT_ROOT / "reports" / "allure-results",
    ):
        folder.mkdir(parents=True, exist_ok=True)


# ── Session-scoped environment fixtures ───────────────────────────────────────

@pytest.fixture(scope="session")
def base_url():
    """Target application URL (OWASP Juice Shop by default)."""
    return os.getenv("BASE_URL", "http://localhost:3000").rstrip("/")


@pytest.fixture(scope="session")
def browser_name():
    """Browser to use: chrome or firefox (from .env)."""
    return os.getenv("BROWSER", "chrome").lower()


@pytest.fixture(scope="session")
def headless():
    """Run browser without a visible window when true."""
    return os.getenv("HEADLESS", "false").lower() == "true"


@pytest.fixture(scope="session")
def implicit_wait():
    """Default wait time in seconds for element lookups."""
    return int(os.getenv("IMPLICIT_WAIT", "10"))


@pytest.fixture(scope="session")
def page_load_timeout():
    """Maximum seconds to wait for a page to load."""
    return int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))


@pytest.fixture(scope="session")
def valid_email():
    """Known-good Juice Shop admin email from .env."""
    return os.getenv("VALID_EMAIL", "admin@juice-sh.op")


@pytest.fixture(scope="session")
def valid_password():
    """Known-good Juice Shop admin password from .env."""
    return os.getenv("VALID_PASSWORD", "admin123")


@pytest.fixture(scope="session")
def screenshot_dir():
    """Folder where failure screenshots are saved."""
    path = PROJECT_ROOT / os.getenv("SCREENSHOT_DIR", "screenshots")
    path.mkdir(parents=True, exist_ok=True)
    return path


@pytest.fixture(scope="session")
def log_dir():
    """Folder where execution log files are saved."""
    path = PROJECT_ROOT / os.getenv("LOG_DIR", "logs")
    path.mkdir(parents=True, exist_ok=True)
    return path


# ── Per-test WebDriver fixture ─────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver():
    """
    Launch a browser, yield it to the test, then quit it regardless of outcome.
    Screenshots on failure are handled by ``pytest_runtest_makereport`` below.
    """
    logger.info("=== TEST START: Launching browser ===")
    drv = get_driver()
    yield drv
    logger.info("=== TEST END: Closing browser ===")
    drv.quit()


# ── Failure screenshot hook ────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot and attach it to the Allure report on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            path = capture_screenshot(drv, item.name)
            with open(path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=f"FAILURE: {item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
            logger.error(f"Test FAILED: {item.name} — screenshot: {path}")
