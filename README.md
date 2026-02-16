

---

# AI-Powered Code Review & Bug Detection Agent

## 📌 Project Overview

The AI-Powered Code Review & Bug Detection Agent is a web-based intelligent system designed to analyze source code files and detect:

* Bugs
* Security vulnerabilities
* Performance issues
* Code quality and best practice violations

The system uses static analysis tools combined with an AI-based explanation engine to provide meaningful suggestions and improvements. It also generates automated unit tests for analyzed functions.

This project demonstrates the integration of frontend web technologies with backend AI-powered analysis tools.

---

# 🎯 Objectives

* To build an intelligent automated code review system.
* To detect common programming errors and vulnerabilities.
* To generate human-readable explanations for detected issues.
* To automatically create unit tests.
* To simulate real-world development tools used in software companies.

---

# 🏗️ System Architecture

```
Frontend (HTML, CSS, JavaScript)
        ↓
Backend API (Python - FastAPI/Flask)
        ↓
Static Analysis Tools + AST Parsing
        ↓
AI Explanation Layer
        ↓
JSON Response
        ↓
Frontend Report Display
```

---

# 🛠️ Technology Stack

## Frontend

* HTML
* CSS
* JavaScript (Vanilla JS)

## Backend

* Python
* FastAPI or Flask
* AST (Abstract Syntax Tree)
* Static analysis tools:

  * pylint
  * bandit
  * radon

## AI Layer

* LLM API (GPT/Claude)
* Prompt engineering logic

---

# 📂 Project Folder Structure

```
ai-code-review/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── analyzer.py
│   ├── test_generator.py
│   └── requirements.txt
│
└── README.md
```

---

# 🚀 Step-by-Step Implementation Guide

---

## Step 1: Setup Backend Environment

### 1. Install Python (3.9+ recommended)

Check version:

```
python --version
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Required Dependencies

Create `requirements.txt`:

```
fastapi
uvicorn
pylint
bandit
radon
openai
```

Install:

```
pip install -r requirements.txt
```

---

## Step 2: Backend API Development

### main.py (API Server)

Responsibilities:

* Accept uploaded file
* Run analysis
* Return JSON response

Basic workflow:

1. Receive file
2. Save temporarily
3. Call analyzer module
4. Collect results
5. Send JSON response

Run server:

```
uvicorn main:app --reload
```

Server runs at:

```
http://localhost:8000
```

---

## Step 3: Static Code Analysis

### analyzer.py

This module performs:

### 1. Bug Detection

Using:

```
pylint file.py
```

### 2. Security Analysis

Using:

```
bandit -r file.py
```

### 3. Complexity Check

Using:

```
radon cc file.py
```

### 4. AST Parsing

Using Python AST module:

```python
import ast
```

Used for:

* Extracting functions
* Detecting unsafe patterns
* Counting loops
* Identifying code smells

---

## Step 4: AI Explanation Layer

After collecting raw analysis results:

1. Create structured prompt
2. Send issues to LLM API
3. Receive:

   * Explanation
   * Suggested fix
   * Refactored code
   * Unit test examples

The AI improves readability and provides contextual understanding.

---

## Step 5: Unit Test Generator

### test_generator.py

Process:

1. Parse functions using AST
2. Extract:

   * Function name
   * Parameters
3. Automatically generate:

   * Basic test cases
   * Edge cases
   * Assertion-based tests

Example output:

```
def test_add():
    assert add(2, 3) == 5
```

---

# 🌐 Frontend Development

---

## index.html

Contains:

* File upload input
* Repository URL input
* Analyze button
* Report display section

---

## style.css

Implements:

* Dark theme dashboard
* Risk score cards
* Section layout
* Responsive design

---

## script.js

Responsibilities:

1. Capture file input
2. Send POST request using fetch()
3. Receive JSON response
4. Display:

   * Security score
   * Performance score
   * Suggestions
   * Unit tests

Example fetch:

```javascript
fetch("http://localhost:8000/analyze", {
    method: "POST",
    body: formData
});
```

---

# 📊 Output Features

The system displays:

* Security Risk Score (0–10)
* Performance Risk Score (0–10)
* Maintainability Score
* List of detected issues
* AI-based explanation
* Suggested fixes
* Auto-generated unit tests

---

# 🔍 How It Works (Execution Flow)

1. User uploads Python file.
2. Backend stores file temporarily.
3. Static tools analyze code.
4. AST extracts structure.
5. AI generates explanation and fixes.
6. Backend returns JSON.
7. Frontend renders structured report.

---

# 🎓 Key Concepts Demonstrated

* Static code analysis
* AI integration
* Multi-agent architecture
* REST API development
* Asynchronous JavaScript
* Full-stack integration
* Automated test generation

---

# 💡 Future Enhancements

* GitHub API integration
* Pull request review bot
* CI/CD pipeline integration
* Multi-language support
* PDF report generation
* Risk heatmap visualization
* Authentication system

---

# 🧪 How to Run the Complete Project

### 1. Start Backend

```
uvicorn main:app --reload
```

### 2. Open Frontend

Open `index.html` in browser.

### 3. Upload Code

Select Python file → Click Analyze

### 4. View Results

Report appears on dashboard.

---

# 📈 Real-World Applications

* Software development companies
* Code auditing teams
* DevOps automation
* Educational coding platforms
* Secure software development lifecycle (SSDLC)

---

# 🏆 Conclusion

The AI-Powered Code Review & Bug Detection Agent is an industry-relevant, full-stack intelligent system that combines static code analysis with AI-driven insights. It demonstrates practical problem-solving skills, software engineering principles, and AI integration capabilities.

This project reflects advanced technical understanding suitable for academic evaluation, internships, and professional portfolios.

---

