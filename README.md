# Vulnerable Flask App - DevSecOps Demo

Welcome to this intentionally vulnerable Flask application designed to demonstrate a real-world **DevSecOps pipeline**!  
The purpose here is **not** to create secure code (in fact, it’s deliberately insecure) but to showcase how security scanning tools like **Bandit** and **Semgrep** can detect and report vulnerabilities automatically.

---

## What This Project Is

- A simple Flask web app with a deliberately vulnerable `/vuln` endpoint using `eval()` on user input.  
- A Dockerfile for easy containerization.  
- A GitHub Actions workflow that runs Bandit and Semgrep scans on every push.  
- A simulated example for developers and security engineers to learn how automated security testing fits into CI/CD pipelines.

---

## Why This Matters

Security is crucial at every step of software development, especially in modern DevOps workflows.  
By integrating tools like Bandit (Python security analyzer) and Semgrep (static analysis), teams can catch security issues **early** — before deployment or production.

---

## Getting Started

### Prerequisites

- Python 3.11+  
- Docker (optional, for containerized deployment)  
- GitHub account (for GitHub Actions CI)

### Manual Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. Create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   ```bash
   pip install flask

4. Run the App
   ```bash
   python secure_app/app.py

The app will be available at http://localhost:5000.

# Running Security Scans Locally
  Bandit (Python security linter)
  ```bash                      
  bandit -r secure_app/
  ```
  Semgrep 
  ```bash
  semgrep scan --config=p/ci
  ```
GitHub Actions Integration

The .github/workflows/security-scan.yml workflow runs Bandit and Semgrep automatically on each push or pull request to the main branch.
This CI/CD security testing ensures no vulnerable code slips through without review


Notes

    DO NOT use the /vuln endpoint in production — it is unsafe by design!
    This project is a learning tool to improve your DevSecOps skills.
    Contributions and feedback are welcome!

Happy Securing! 🔒🚀

Author: Htet Wai
Date: 2025
