# Unified Web Services - QA Engineer Practical Assessment

## Candidate Name
Swetha Durairaj

---

# Tools Used

## Manual Testing
- Microsoft Excel

## Automation Testing
- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager

## API Testing
- Postman

## Load Testing
- k6 / Postman Performance Runner

## Version Control
- Git
- GitHub

---

# Tasks Completed

## Task 1 - OrangeHRM Manual Testing
Created detailed manual test cases for:
- Login
- Dashboard
- Employee Management (PIM)
- Leave Management
- Admin/User Management
- Edge cases
- Common test scenarios

---

## Task 2 - SauceDemo Automation Testing

### Flow 1 - Valid Login and Checkout
- Login with valid credentials
- Add two products to cart
- Verify selected products in cart
- Complete checkout process
- Verify successful order message

### Flow 2 - Locked User Login
- Login with locked user credentials
- Validate locked user error message

---

## Task 3 - ReqRes API Testing

Validated the following APIs:
- GET Users
- GET Single User
- GET Non-existing User
- POST Create User
- PUT Update User
- DELETE User
- POST Login

### Validations Covered
- Status code validation
- Response body validation
- Response time validation
- Positive and negative scenarios

---

## Task 4 - ReqRes Load Testing

### Load Test Configuration
- Target API:
  https://reqres.in/api/users?page=1
- 50 concurrent users
- Duration: 2 minutes

### Metrics Captured
- Average response time
- Minimum response time
- Maximum response time
- p90/p95 response time
- Requests per second
- Failed requests
- Error rate

---

# Project Structure

```text
Unified_Web_Services-QA/
│
|
|── orangehrm_test_cases.xlsx
│
├── sauce_demo_automation/
│   ├── testcases/
│   ├── conftest.py
│   ├── requirements.txt
│   ├── README.md
│   └── report.html
|
|── reqres_api_tests.postman_collection.json
│
| 
│── load_test_report.md
│
└── README.md

```

# How to Run Automation Tests

Navigate to automation folder:

cd sauce_demo_automation

Install dependencies:
pip install -r requirements.txt

Run tests:
pytest -v

Generate HTML report:
pytest --html=report.html

# How to Run API Tests
- Open Postman
- Import: reqres_api_tests.postman_collection.json
- Run collection using Collection Runner

# How to Run Load Tests

- Using Postman Performance Runner
- Import collection
- Configure concurrent users and duration
- Execute performance test

# Issues Faced

- Chrome password manager popup appeared during SauceDemo automation and was handled using browser configuration
