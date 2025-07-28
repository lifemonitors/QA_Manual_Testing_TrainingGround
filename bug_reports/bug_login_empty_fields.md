# 🐞 Bug Report: Login with Empty Fields Does Not Show Error

- **Bug ID:** BUG001
- **Module:** Login Page
- **Severity:** Medium
- **Priority:** High
- **Environment:** https://automationexercise.com

## 📝 Description:

When the login form is submitted without entering any email or password, the system accepts the request but does not show any error message to the user.

---

## 🔁 Steps to Reproduce:

1. Open https://automationexercise.com
2. Click on "Signup / Login"
3. Leave both **email** and **password** fields empty
4. Click on **Login**

---

## ✅ Expected Result:

- A validation message should appear, such as:  
  `"Email is required"` or `"Please enter your email and password"`

---

## ❌ Actual Result:

- The page reloads, but **no error message** appears
- The user does not know what went wrong

---

## 📸 Screenshot:

_(Add screenshot here if available)_
