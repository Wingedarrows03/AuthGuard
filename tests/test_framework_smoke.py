"""
Temporary smoke test — confirms PyTest and conftest fixtures work.

Safe to remove after real login tests exist (Step 3.x).
"""

import pytest


@pytest.mark.smoke
def test_base_url_loaded(base_url):
    """BASE_URL from .env is available to all tests."""
    assert base_url.startswith("http")


@pytest.mark.smoke
def test_credentials_loaded(valid_email, valid_password):
    """Test credentials from .env are available."""
    assert "@" in valid_email
    assert len(valid_password) > 0
