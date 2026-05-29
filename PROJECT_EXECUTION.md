# Automated Login Security Testing Bot — Project Execution Guide

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Project Architecture](#2-project-architecture)
3. [Phase-wise Execution Plan](#3-phase-wise-execution-plan)
4. [Environment Setup Workflow](#4-environment-setup-workflow)
5. [Component Development Workflow](#5-component-development-workflow)
6. [Test Execution Workflow](#6-test-execution-workflow)
7. [Test Scenarios & Execution Flow](#7-test-scenarios--execution-flow)
8. [Reporting & Evidence Workflow](#8-reporting--evidence-workflow)
9. [Logging Workflow](#9-logging-workflow)
10. [CI/CD & Version Control Workflow](#10-cicd--version-control-workflow)
11. [Bot Execution Flow Diagram](#11-bot-execution-flow-diagram)

---

## 1. Project Overview

The **Automated Login Security Testing Bot** is a Python-based automation framework that validates login security workflows and authentication-related functionalities of a web application. It merges QA Automation best practices with Cybersecurity testing concepts to provide a comprehensive, professional-grade test suite.

**Target Application (Phase 1):** OWASP Juice Shop  
**Target Application (Phase 2):** Self-built dummy authentication website

---

## 2. Project Architecture

```
LoginSecurityTestingBot/
│
├── tests/
│   ├── test_valid_login.py          # Valid credential login tests
│   ├── test_invalid_login.py        # Invalid credential tests
│   ├── test_sql_injection.py        # SQL injection security tests
│   ├── test_empty_fields.py         # Empty field validation tests
│   ├── test_password_toggle.py      # Password visibility toggle tests
│   ├── test_logout.py               # Logout & session validation tests
│   └── test_bruteforce.py           # Brute force simulation tests
│
├── pages/
│   ├── login_page.py                # Page Object: Login Page
│   └── dashboard_page.py            # Page Object: Dashboard Page
│
├── test_data/
│   └── credentials.csv              # Test credentials dataset
│
├── utils/
│   ├── driver_setup.py              # WebDriver initialization & config
│   ├── logger.py                    # Logging utility
│   └── screenshot.py                # Screenshot capture utility
│
├── screenshots/                     # Auto-captured failure screenshots
├── reports/                         # Allure report output
├── logs/                            # Execution log files
│
├── conftest.py                      # PyTest fixtures & hooks
├── pytest.ini                       # PyTest configuration
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── main.py                          # Entry point for manual execution
```

---

## 3. Phase-wise Execution Plan

### Phase 1 — Foundation & Setup

| Step | Task | Output |
|------|------|--------|
| 1.1 | Set up virtual environment | Isolated Python environment |
| 1.2 | Install all dependencies | All packages ready |
| 1.3 | Configure `pytest.ini` and `conftest.py` | Framework skeleton ready |
| 1.4 | Implement `driver_setup.py` | Browser launches correctly |
| 1.5 | Implement `logger.py` | Log files generated |
| 1.6 | Implement `screenshot.py` | Screenshots on failure |
| 1.7 | Verify OWASP Juice Shop is running | Target app accessible |

### Phase 2 — Page Object Model Implementation

| Step | Task | Output |
|------|------|--------|
| 2.1 | Inspect login page elements (DevTools) | Locators identified |
| 2.2 | Build `login_page.py` POM | Reusable login actions |
| 2.3 | Inspect dashboard page elements | Locators identified |
| 2.4 | Build `dashboard_page.py` POM | Reusable dashboard actions |

### Phase 3 — Test Development

| Step | Task | Output |
|------|------|--------|
| 3.1 | Write `test_valid_login.py` | Baseline functional test |
| 3.2 | Write `test_invalid_login.py` | Error message validation |
| 3.3 | Write `test_empty_fields.py` | Field validation tests |
| 3.4 | Write `test_sql_injection.py` | Security vulnerability tests |
| 3.5 | Write `test_bruteforce.py` | Lockout/CAPTCHA detection |
| 3.6 | Write `test_logout.py` | Session security tests |
| 3.7 | Write `test_password_toggle.py` | UI feature tests |

### Phase 4 — Reporting & Integration

| Step | Task | Output |
|------|------|--------|
| 4.1 | Configure Allure with pytest | Allure markers working |
| 4.2 | Run full test suite | Results collected |
| 4.3 | Generate Allure HTML report | Visual report accessible |
| 4.4 | Review logs and screenshots | Evidence collected |

### Phase 5 — (Optional) Self-built Auth Website

| Step | Task | Output |
|------|------|--------|
| 5.1 | Build a minimal Flask/Node login page | Custom test target live |
| 5.2 | Add intentional vulnerabilities | Richer test scenarios |
| 5.3 | Extend test suite for new target | Full coverage |

---

## 4. Environment Setup Workflow

```
Step 1: Clone/create the repository
    git init LoginSecurityTestingBot
    cd LoginSecurityTestingBot

Step 2: Create a virtual environment
    python -m venv venv
    source venv/bin/activate          # macOS/Linux
    venv\Scripts\activate             # Windows

Step 3: Install dependencies
    pip install -r requirements.txt

Step 4: Verify Allure CLI is installed
    allure --version

Step 5: Start OWASP Juice Shop (Docker)
    docker pull bkimminich/juice-shop
    docker run -d -p 3000:3000 bkimminich/juice-shop

Step 6: Confirm target is accessible
    Open browser → http://localhost:3000
```

---

## 5. Component Development Workflow

### 5.1 Driver Setup (`utils/driver_setup.py`)

- Use `webdriver-manager` to auto-download the correct ChromeDriver/GeckoDriver.
- Accept browser name as parameter for multi-browser support.
- Configure implicit waits and window maximize by default.
- Return the driver instance to be used across all tests.

### 5.2 Logger (`utils/logger.py`)

- Initialize a named logger with both file and console handlers.
- Log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`.
- Each test run appends to a timestamped log file under `logs/`.

### 5.3 Screenshot Utility (`utils/screenshot.py`)

- Accept driver and test name as parameters.
- Save PNG files with a timestamp to `screenshots/`.
- Invoked automatically from `conftest.py` on test failure via a PyTest hook.

### 5.4 Page Objects (`pages/`)

**`login_page.py`** exposes:
- `open()` — navigates to the login URL
- `enter_username(username)` — locates and fills the username field
- `enter_password(password)` — locates and fills the password field
- `click_login()` — submits the login form
- `get_error_message()` — returns visible error text
- `toggle_password_visibility()` — clicks the show/hide icon
- `click_forgot_password()` — navigates to the forgot password page

**`dashboard_page.py`** exposes:
- `is_logged_in()` — asserts presence of a post-login element
- `logout()` — triggers the logout action
- `is_dashboard_accessible()` — checks if the dashboard URL loads after logout

### 5.5 Test Data (`test_data/credentials.csv`)

CSV format:
```
username,password,expected_result
admin@juice-sh.op,admin123,success
wronguser@test.com,wrongpass,failure
' OR '1'='1,anything,blocked
admin' --,anything,blocked
,admin123,error
admin@juice-sh.op,,error
,, error
```

---

## 6. Test Execution Workflow

### Running All Tests

```bash
pytest tests/ --alluredir=reports/allure-results -v
```

### Running a Specific Test File

```bash
pytest tests/test_sql_injection.py --alluredir=reports/allure-results -v
```

### Running by Marker

```bash
pytest -m security --alluredir=reports/allure-results -v
pytest -m functional --alluredir=reports/allure-results -v
```

### Generating the Allure Report

```bash
allure serve reports/allure-results
```

---

## 7. Test Scenarios & Execution Flow

### A. Valid Login Test (`test_valid_login.py`)

```
Open Login Page
  → Enter valid username
  → Enter valid password
  → Click Login button
  → Assert: Dashboard/home page is loaded
  → Assert: Welcome message or user avatar is visible
  → PASS / FAIL + Screenshot on FAIL
```

### B. Invalid Login Test (`test_invalid_login.py`)

```
Open Login Page
  → Enter wrong username / wrong password
  → Click Login button
  → Assert: Error message is displayed
  → Assert: Still on login page
  → PASS / FAIL + Screenshot on FAIL
```

### C. Empty Fields Test (`test_empty_fields.py`)

Three sub-cases run in a parametrized loop:
```
Sub-case 1: Empty username, valid password
Sub-case 2: Valid username, empty password
Sub-case 3: Both fields empty

Each sub-case:
  → Clear / leave field empty
  → Click Login
  → Assert: Appropriate validation message shown
  → PASS / FAIL
```

### D. SQL Injection Test (`test_sql_injection.py`)

Inputs from CSV/list: `' OR '1'='1`, `admin' --`, `" OR ""="`, `1' ORDER BY 1--`
```
For each SQL payload:
  → Enter payload in username field
  → Enter any value in password field
  → Click Login
  → Assert: Login does NOT succeed
  → Assert: Error or "Invalid credentials" shown
  → PASS (injection blocked) / FAIL (injection succeeded — critical vulnerability)
```

### E. Brute Force Simulation (`test_bruteforce.py`)

```
For N attempts (configurable, e.g. 10):
  → Enter invalid credentials
  → Click Login
  → Check response after each attempt

Assert any of:
  → Account lockout message appears
  → CAPTCHA challenge triggered
  → Delay/throttling behaviour observed
  → Warning message shown
```

### F. Session / Logout Test (`test_logout.py`)

```
Login with valid credentials
  → Assert: Dashboard is accessible
  → Click Logout
  → Assert: Redirected to login page
  → Attempt to navigate back to dashboard URL
  → Assert: Access denied / Redirected to login
  → PASS / FAIL
```

### G. Password Toggle Test (`test_password_toggle.py`)

```
Open Login Page
  → Enter a password string
  → Assert: Input type = "password" (text is masked)
  → Click the show/hide password toggle button
  → Assert: Input type = "text" (text is visible)
  → Click toggle again
  → Assert: Input type = "password" (masked again)
  → PASS / FAIL
```

---

## 8. Reporting & Evidence Workflow

```
Test Suite Completes
      ↓
PyTest collects results → reports/allure-results/
      ↓
On any FAIL → screenshot.py saves PNG → screenshots/
      ↓
Run: allure serve reports/allure-results
      ↓
Allure opens browser dashboard showing:
  - Overall pass/fail ratio (pie chart)
  - Test category breakdown
  - Execution timeline
  - Per-test steps, logs, and attached screenshots
  - Severity and feature tags
```

**Allure Decorators used in test files:**

```python
@allure.feature("Login Security")
@allure.story("SQL Injection")
@allure.severity(allure.severity_level.CRITICAL)
def test_sql_injection_username():
    ...
```

---

## 9. Logging Workflow

Every test execution writes to a log file in `logs/` with the format:

```
logs/test_run_YYYY-MM-DD_HH-MM-SS.log
```

Log entries follow this pattern:

```
[2025-06-01 10:23:45] [INFO]    test_valid_login.py :: Starting valid login test
[2025-06-01 10:23:46] [INFO]    login_page.py :: Navigated to http://localhost:3000/#/login
[2025-06-01 10:23:47] [INFO]    login_page.py :: Entered username: admin@juice-sh.op
[2025-06-01 10:23:48] [INFO]    login_page.py :: Clicked login button
[2025-06-01 10:23:49] [INFO]    test_valid_login.py :: Login successful — dashboard visible
[2025-06-01 10:23:50] [ERROR]   test_sql_injection.py :: INJECTION SUCCEEDED — vulnerability detected!
[2025-06-01 10:23:51] [INFO]    screenshot.py :: Screenshot saved: screenshots/test_sql_injection_2025-06-01_10-23-51.png
```

---

## 10. CI/CD & Version Control Workflow

### Git Branching Strategy

```
main             → stable, tested code
dev              → active development
feature/<name>   → individual feature branches
```

### Commit Convention

```
feat: add SQL injection test cases
fix: resolve screenshot path issue on Windows
test: add brute force simulation test
docs: update README with setup instructions
refactor: improve login_page POM locators
```

### GitHub Actions (Optional CI)

Add `.github/workflows/test.yml` to run tests automatically on push:

```yaml
name: Run Security Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ --alluredir=reports/allure-results -v
```

---

## 11. Bot Execution Flow Diagram

```
┌─────────────────────────────────────────────┐
│                  START TEST                  │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│         conftest.py: Setup Fixture           │
│   driver_setup.py → Launch Browser          │
│   logger.py       → Initialize Log File     │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│         Open Target Login Page               │
│   login_page.py → open()                    │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│         Execute Test Scenario                │
│   (Valid Login / SQL Injection /             │
│    Brute Force / Empty Fields / etc.)        │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│           Validate Result                    │
│   Assert expected vs actual outcome          │
└──────────┬──────────────────────┬───────────┘
           │ PASS                 │ FAIL
           ↓                      ↓
┌──────────────────┐   ┌──────────────────────┐
│  Log: PASSED     │   │  Log: FAILED          │
│  Allure: ✅ Pass │   │  screenshot.py → PNG  │
└──────────────────┘   │  Allure: ❌ Fail      │
                       │  Attach screenshot    │
                       └──────────────────────┘
                                 ↓
┌─────────────────────────────────────────────┐
│         conftest.py: Teardown Fixture        │
│   driver.quit() → Close Browser             │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│       Generate Allure Report                 │
│   allure serve reports/allure-results        │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│                   END                        │
└─────────────────────────────────────────────┘
```

---

*Document Version: 1.0 | Project: Automated Login Security Testing Bot*
