# Cloud QA Portfolio

Automated API test suite built with Pytest, GitHub Actions, and Allure reporting.

## Tech Stack
- Python + Pytest
- Requests
- GitHub Actions (CI/CD)
- Allure (Test Reporting)

## Test Coverage
- GET /posts — status, data type, item count, response time
- GET /posts/1 — required fields, correct ID, content type
- POST /posts — status 201, correct title, ID assigned
- Error handling — 404 for missing and invalid endpoints

## Test Results
12 tests | 100% passing | ~8 seconds

### Allure Report — Behaviors View
![Allure Behaviors](docs/screenshots/allure-behaviors.png)

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run tests
```bash
pytest tests/ -v
```

### Generate Allure report
```bash
pytest tests/ -v --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report --host 0.0.0.0 --port 5050
```
## Infrastructure Security Scanning

Terraform code for Azure infrastructure is scanned automatically on every push using Checkov.

### Checkov scan results (latest)
- **Passed:** 25 checks
- **Failed:** 4 checks (documented below)

| Check | Resource | Status | Notes |
|---|---|---|---|
| CKV_AZURE_160 | public-nsg | Accepted risk | HTTP intentionally open for web server |
| CKV_AZURE_50 | vm1, vm2 | Accepted risk | No extensions installed in this environment |
| CKV_AZURE_119 | vm1-nic | Accepted risk | Public IP required for gateway VM |

### Infrastructure
- Azure VNet with public and private subnets
- Network Security Groups with least-privilege rules
- SSH restricted to specific IP — no password authentication
- Private app server with no public IP exposure