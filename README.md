#  AuthGuard – Automated Login Security Testing Framework

AuthGuard is a **cybersecurity-focused automation testing framework** designed to validate the **security, reliability, and functionality of web authentication systems**. Built using **Python, Selenium, PyTest, and Allure Report**, the framework automates authentication workflows and security validation scenarios to identify vulnerabilities and functional issues in login systems.

This project bridges **QA Automation Testing** and **Cybersecurity** by combining traditional login testing with security-oriented validations such as **SQL Injection testing**, **brute-force simulations**, and **session validation**.

---

##  Features

### Functional Testing

 Valid Login Testing
 Invalid Login Testing
 Empty Field Validation
 Forgot Password Workflow Testing
 Password Visibility Toggle Testing
 Logout Validation

### Security Testing

 SQL Injection Input Testing
 Brute Force Login Attempt Simulation
 Authentication Error Handling
 Session Security Verification

### Reporting & Monitoring

Allure Report Integration
 Screenshot Capture on Failure
 Execution Logs for Debugging
 Test Result Tracking

---

##  Tech Stack

| Technology        | Purpose                  |
| ----------------- | ------------------------ |
| Python            | Programming Language     |
| Selenium          | Web Automation           |
| PyTest            | Test Execution Framework |
| Allure Report     | Test Reporting           |
| WebDriver Manager | Driver Management        |
| CSV               | Test Data Management     |

---

## 📂 Project Structure

```plaintext
AuthGuard/
│── tests/
│   ├── test_valid_login.py
│   ├── test_invalid_login.py
│   ├── test_sql_injection.py
│   ├── test_empty_fields.py
│   ├── test_password_toggle.py
│   ├── test_logout.py
│   └── test_bruteforce.py
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── utils/
│   ├── driver_setup.py
│   ├── logger.py
│   └── screenshot.py
│
├── test_data/
│   └── credentials.csv
│
├── screenshots/
├── reports/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AuthGuard.git
cd AuthGuard
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Install Allure

### Windows (Chocolatey)

```bash
choco install allure-commandline
```

### Windows (Scoop)

```bash
scoop install allure
```

Verify installation:

```bash
allure --version
```

---

##  Running Tests

Run all test cases:

```bash
pytest
```

Run with Allure reporting:

```bash
pytest --alluredir=reports
```

Generate and open report:

```bash
allure serve reports
```

---

##  Test Scenarios

| Test Case       | Description                         |
| --------------- | ----------------------------------- |
| Valid Login     | Verify successful authentication    |
| Invalid Login   | Verify invalid credentials handling |
| Empty Fields    | Validate form input restrictions    |
| SQL Injection   | Test malicious login inputs         |
| Password Toggle | Verify password visibility feature  |
| Forgot Password | Validate reset workflow             |
| Logout Test     | Verify session termination          |
| Brute Force     | Simulate repeated failed attempts   |

---

##  Reporting

AuthGuard generates:

* **Detailed Allure Reports**
* **Execution Logs**
* **Failure Screenshots**
* **Pass/Fail Test Summary**

---

##  Project Objective

The goal of AuthGuard is to provide a practical framework for testing **authentication security mechanisms** while applying **automation testing principles** and **cybersecurity concepts** in a real-world environment.

---

##  Future Enhancements

* Cross-browser testing
* Parallel test execution
* API authentication testing
* CI/CD integration with GitHub Actions
* Expanded security validation modules

---

##  Author

**Ashit Mallick**
Cybersecurity & QA Automation Enthusiast
