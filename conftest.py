"""
AuthGuard — shared PyTest configuration and fixtures.

Runs automatically before tests. Loads .env, ensures output folders exist,
and exposes session settings used by driver and page objects (added in later steps).
"""

import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent

load_dotenv(PROJECT_ROOT / ".env")


def pytest_configure(config):
    """Create log, screenshot, and Allure folders before the test run."""
    for folder in (
        PROJECT_ROOT / "logs",
        PROJECT_ROOT / "screenshots",
        PROJECT_ROOT / "reports" / "allure-results",
    ):
        folder.mkdir(parents=True, exist_ok=True)


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
