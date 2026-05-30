"""
main.py — Programmatic entry point for the AuthGuard test suite.

Usage examples
--------------
Run all tests:
    python main.py

Run only security tests:
    python main.py security

Run only functional tests:
    python main.py functional

For standard CLI execution, prefer:
    pytest tests/ --alluredir=reports/allure-results -v
"""

import subprocess
import sys


def run_tests(marker: str = None) -> int:
    """
    Invoke pytest programmatically.

    Parameters
    ----------
    marker : str, optional
        A pytest marker expression (e.g. ``"security"``, ``"functional"``).
        When omitted, all tests are collected and run.

    Returns
    -------
    int
        The pytest exit code (0 = all passed, non-zero = failures/errors).
    """
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "tests/",
        "--alluredir=reports/allure-results",
        "-v",
        "--tb=short",
    ]
    if marker:
        cmd += ["-m", marker]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    marker_arg = sys.argv[1] if len(sys.argv) > 1 else None
    exit_code = run_tests(marker_arg)
    sys.exit(exit_code)
