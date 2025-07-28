# QA_Manual_Testing_TrainingGround

This project demonstrates manual QA testing skills using the demo website [https://automationexercise.com](https://automationexercise.com).  
It includes test cases, bug reports, and basic Python tools to practice web form and security testing.

---

##  Project Goals

- Practice structured manual testing (positive and negative cases)
- Create clear and professional bug reports
- Use Python for technical testing (headers, redirects, forms)
- Show QA and security skills in a public GitHub portfolio

---

##  Tested Website

- **URL:** [https://automationexercise.com](https://automationexercise.com)
- **Focus:** Signup/login pages, forms, input validation
- **Platform:** Desktop browser

---

##  Project Structure

QA_Manual_Testing_TrainingGround/
├── README.md
├── requirements.txt
├── test_cases/
│ └── registration.md
├── bug_reports/
│ └── bug_login_empty_fields.md
├── security_checks/
│ ├── check_headers.py
│ ├── check_redirects.py
│ ├── form_tester.py
│ ├── form_login_tester.py
│ └── logger.py
└── logs/ ← created automatically


##  Useful Project Files

- [📝 Registration Test Cases](test_cases/registration.md)
- [🐞 Bug Report: Login with Empty Fields](bug_reports/bug_login_empty_fields.md)
- [🛡 Check Headers Script](security_checks/check_headers.py)
- [🔁 Check Redirects Script](security_checks/check_redirects.py)
- [🔍 Form Analyzer Script](security_checks/form_tester.py)
- [🔐 Login Form Tester Script](security_checks/form_login_tester.py)

---

##  Sample Test Case

| ID   | Scenario               | Steps                              | Expected Result                 |
|------|------------------------|-------------------------------------|----------------------------------|
| TC01 | Successful registration | Go to Signup → enter valid data     | Account is created successfully |
| TC02 | Email already used     | Use same email again                | Error message appears            |
| TC03 | Empty login fields     | Submit without email or password    | Validation error                 |

---

##  Example Log Output

Example from `check_headers.py` run against https://automationexercise.com:

[14:02:17] https://automationexercise.com → MISSING header: Content-Security-Policy
[14:02:17] https://automationexercise.com → OK: X-Content-Type-Options
[14:02:17] https://automationexercise.com → MISSING header: Strict-Transport-Security




These logs are saved to `/logs/` automatically.

---

## 🧾 Installation

To run Python tools, install dependencies:

```bash
pip install -r requirements.txt
```

Author
Aleksei Kozhevnikov
Manual QA Tester | Cybersecurity Beginner
Austin, Texas
GitHub: lifemonitors 
