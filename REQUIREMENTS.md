# Automated Login Security Testing Bot — Requirements & Dependencies

---

## Table of Contents

1. [Tech Stack Summary](#1-tech-stack-summary)
2. [Python Dependencies](#2-python-dependencies)
3. [System-Level Dependencies](#3-system-level-dependencies)
4. [Development Tools](#4-development-tools)
5. [requirements.txt (Copy-Ready)](#5-requirementstxt-copy-ready)
6. [Configuration Files](#6-configuration-files)
7. [Target Application Setup](#7-target-application-setup)
8. [Version Compatibility Matrix](#8-version-compatibility-matrix)

---

## 1. Tech Stack Summary

| Category | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core programming language |
| **Automation Framework** | Selenium 4.x | Browser automation & interaction |
| **Test Framework** | PyTest 7.x+ | Test discovery, execution, fixtures |
| **Reporting** | Allure Report + allure-pytest | Visual HTML test reports |
| **Driver Management** | WebDriver Manager | Auto-downloads browser drivers |
| **Logging** | Python `logging` (stdlib) | Execution, failure, and error logs |
| **Data Handling** | CSV (Python `csv` stdlib) | Test credential datasets |
| **Version Control** | Git + GitHub | Source control and collaboration |
| **Target App (Phase 1)** | OWASP Juice Shop (Docker) | Intentionally vulnerable test target |
| **Target App (Phase 2)** | Custom Flask/Node app | Self-built dummy auth website |
| **IDE** | VS Code / PyCharm | Development environment |
| **Containerization** | Docker | Running OWASP Juice Shop locally |

---

## 2. Python Dependencies

### Core Automation

| Package | Version | Purpose |
|---|---|---|
| `selenium` | `>=4.15.0` | Browser automation engine |
| `webdriver-manager` | `>=4.0.1` | Auto-manages ChromeDriver / GeckoDriver |

### Test Framework

| Package | Version | Purpose |
|---|---|---|
| `pytest` | `>=7.4.0` | Test runner, fixtures, parametrize |
| `pytest-html` | `>=4.0.0` | Basic HTML report (optional backup) |
| `pytest-xdist` | `>=3.3.1` | Parallel test execution (optional) |
| `pytest-rerunfailures` | `>=12.0` | Retry flaky tests (optional) |

### Reporting

| Package | Version | Purpose |
|---|---|---|
| `allure-pytest` | `>=2.13.2` | PyTest plugin for Allure integration |
| `allure-python-commons` | `>=2.13.2` | Allure decorators and step logging |

### Utilities

| Package | Version | Purpose |
|---|---|---|
| `Pillow` | `>=10.0.0` | Image processing for screenshots |
| `python-dotenv` | `>=1.0.0` | Load environment variables from `.env` |
| `requests` | `>=2.31.0` | HTTP requests for future API tests |
| `faker` | `>=19.0.0` | Generate fake/random test data |
| `openpyxl` | `>=3.1.2` | Read/write Excel test data (optional) |

### Code Quality (Dev Only)

| Package | Version | Purpose |
|---|---|---|
| `flake8` | `>=6.1.0` | Python linting |
| `black` | `>=23.0.0` | Code auto-formatter |
| `isort` | `>=5.12.0` | Import statement organizer |
| `pre-commit` | `>=3.4.0` | Git pre-commit hooks |

---

## 3. System-Level Dependencies

### Required: Java (for Allure CLI)

Allure Report's CLI tool requires Java to generate reports.

```bash
# macOS
brew install openjdk

# Ubuntu/Debian
sudo apt-get install default-jdk

# Windows
# Download from https://adoptium.net/
```

Verify:
```bash
java -version
# Should return: java version "17.x.x" or higher
```

### Required: Allure CLI

```bash
# macOS
brew install allure

# Windows (via Scoop)
scoop install allure

# Linux (manual)
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz
sudo ln -s allure-2.24.0/bin/allure /usr/bin/allure
```

Verify:
```bash
allure --version
# Should return: 2.24.0 or higher
```

### Required: Google Chrome (or Firefox)

The framework defaults to Chrome via ChromeDriver.

```bash
# Chrome version check
google-chrome --version     # Linux
# or check chrome://settings/help in browser
```

> `webdriver-manager` automatically downloads the matching ChromeDriver version.

### Required: Docker (for OWASP Juice Shop)

```bash
# Install Docker Desktop from https://www.docker.com/products/docker-desktop
docker --version
# Should return: Docker version 24.x.x or higher
```

---

## 4. Development Tools

### Python Environment

```bash
# Python 3.10 or higher required
python --version

# pip (package manager)
pip --version

# Virtual environment (recommended)
python -m venv venv
```

### IDE Setup

**VS Code** — Recommended extensions:
- Python (Microsoft)
- Pylance
- pytest (LittleFoxTeam)
- GitLens

**PyCharm** — Built-in Python and pytest support, no additional plugins needed.

### Git & GitHub

```bash
git --version
# Should return: git version 2.40.x or higher
```

Configure Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## 5. requirements.txt (Copy-Ready)

Create this file at the root of your project (`LoginSecurityTestingBot/requirements.txt`):

```
# ─── Core Automation ──────────────────────────────────────
selenium>=4.15.0
webdriver-manager>=4.0.1

# ─── Test Framework ───────────────────────────────────────
pytest>=7.4.0
pytest-html>=4.0.0
pytest-xdist>=3.3.1
pytest-rerunfailures>=12.0

# ─── Allure Reporting ─────────────────────────────────────
allure-pytest>=2.13.2
allure-python-commons>=2.13.2

# ─── Utilities ────────────────────────────────────────────
Pillow>=10.0.0
python-dotenv>=1.0.0
requests>=2.31.0
faker>=19.0.0
openpyxl>=3.1.2

# ─── Code Quality (Dev) ───────────────────────────────────
flake8>=6.1.0
black>=23.0.0
isort>=5.12.0
pre-commit>=3.4.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 6. Configuration Files

### `pytest.ini`

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

markers =
    functional: Functional login tests
    security: Security-oriented tests
    regression: Regression test suite
    smoke: Smoke tests (quick sanity)

addopts =
    -v
    --tb=short
    --alluredir=reports/allure-results

log_cli = true
log_cli_level = INFO
log_file = logs/pytest.log
log_file_level = DEBUG
log_file_format = %(asctime)s [%(levelname)s] %(name)s: %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```

### `.env` (Environment Variables)

```env
# Target application
BASE_URL=http://localhost:3000

# Browser configuration
BROWSER=chrome
HEADLESS=false
IMPLICIT_WAIT=10
PAGE_LOAD_TIMEOUT=30

# Test credentials
VALID_EMAIL=admin@juice-sh.op
VALID_PASSWORD=admin123

# Brute force config
BRUTE_FORCE_ATTEMPTS=10

# Screenshot path
SCREENSHOT_DIR=screenshots

# Log path
LOG_DIR=logs
```

### `.gitignore`

```
# Virtual environment
venv/
.venv/
env/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Allure results (generated on run)
reports/allure-results/
reports/allure-report/

# Screenshots (generated on failure)
screenshots/

# Logs
logs/

# IDE
.vscode/
.idea/
*.iml

# Environment
.env

# OS
.DS_Store
Thumbs.db
```

---

## 7. Target Application Setup

### Phase 1: OWASP Juice Shop (Docker)

OWASP Juice Shop is an intentionally insecure web application designed for security testing practice.

```bash
# Pull the latest image
docker pull bkimminich/juice-shop

# Run the container
docker run -d \
  --name juice-shop \
  -p 3000:3000 \
  bkimminich/juice-shop

# Verify it is running
docker ps

# Access the application
# Open: http://localhost:3000
```

**Login endpoint:** `http://localhost:3000/#/login`  
**Default admin credentials:** `admin@juice-sh.op` / `admin123`

Stop/restart:
```bash
docker stop juice-shop
docker start juice-shop
docker rm juice-shop       # Remove container completely
```

### Phase 2: Custom Authentication Website (Optional)

A minimal Flask app can serve as a Phase 2 test target:

```bash
pip install flask
```

```python
# app.py — minimal dummy auth server
from flask import Flask, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "test_secret"
USERS = {"testuser": "testpass123"}
LOGIN_HTML = """..."""  # minimal login form HTML

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")
        if USERS.get(u) == p:
            session["user"] = u
            return redirect("/dashboard")
        return "Invalid credentials", 401
    return render_template_string(LOGIN_HTML)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

```bash
python app.py
# Access: http://localhost:5000/login
```

---

## 8. Version Compatibility Matrix

| Component | Minimum Version | Recommended | Notes |
|---|---|---|---|
| Python | 3.10 | 3.11 or 3.12 | f-strings, match/case support |
| Selenium | 4.15.0 | Latest 4.x | Selenium 4 uses W3C WebDriver |
| PyTest | 7.4.0 | Latest 7.x | Required for modern fixtures |
| allure-pytest | 2.13.2 | Latest 2.x | Must match allure-python-commons |
| webdriver-manager | 4.0.1 | Latest | Supports Chrome, Firefox, Edge |
| Allure CLI | 2.24.0 | Latest 2.x | Java 8+ required |
| Java (JDK/JRE) | 8 | 17 (LTS) | Required only for Allure CLI |
| Google Chrome | 114+ | Latest stable | Must match ChromeDriver version |
| Docker | 20.10+ | Latest | For running Juice Shop |
| Git | 2.35+ | Latest | Standard VCS |

---

## Quick Install Checklist

```
[ ] Python 3.10+ installed
[ ] pip upgraded: pip install --upgrade pip
[ ] Virtual environment created and activated
[ ] pip install -r requirements.txt
[ ] Java 17+ installed (for Allure CLI)
[ ] Allure CLI installed and verified (allure --version)
[ ] Google Chrome installed (latest)
[ ] Docker installed and running
[ ] OWASP Juice Shop container pulled and started
[ ] .env file created with correct BASE_URL
[ ] pytest.ini configured
[ ] Verify setup: pytest --collect-only
```

---

*Document Version: 1.0 | Project: Automated Login Security Testing Bot*
