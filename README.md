# QA_Manual_Testing_TrainingGround

This project shows manual QA testing skills using the demo website [https://automationexercise.com](https://automationexercise.com).

## 🔍 What is tested?

- Registration form
- Login form
- Form validation (positive and negative cases)
- Error messages and field behavior

## 📁 Structure

- `test_cases/` — test cases in Markdown
- `bug_reports/` — bug reports with steps and actual results
- `security_checks/` — optional Python tools for basic security checks (headers, redirects)
- `logs/` — results of script runs (created automatically)

## 🧪 Example Test Case

| ID   | Scenario               | Steps                              | Expected Result                 |
|------|------------------------|-------------------------------------|----------------------------------|
| TC01 | Successful Registration | Go to Signup → enter valid data     | Account is created successfully |
| TC02 | Empty Login Fields     | Click login without input           | Error message appears            |

## 🛠 Tools (optional)

If you use Python tools from `security_checks/`, install dependencies:

