
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
Backend API (Python - FastAPI)
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

* HTML5
* CSS3 (Modern dark theme)
* JavaScript (Vanilla JS, async/await)

## Backend

* Python 3.9+
* FastAPI
* Uvicorn (ASGI server)
* Static Analysis Tools:
  * pylint (Code quality)
  * bandit (Security)
  * radon (Complexity)

## Additional Libraries

* python-multipart (File uploads)
* ast (Built-in for parsing)
* subprocess (Tool execution)

---

# 📂 Project Structure

```
ai-code-review/
├── frontend/
│   ├── index.html      # Main UI with upload and results display
│   ├── style.css       # Dark theme styling with responsive design
│   └── script.js       # Frontend logic and API communication
├── backend/
│   ├── main.py         # FastAPI application with /analyze endpoint
│   ├── analyzer.py     # Static analysis orchestration
│   ├── test_generator.py # AST-based unit test generation
│   ├── scoring.py      # Risk scoring calculations
│   └── requirements.txt # Python dependencies
├── example.py          # Sample Python file for testing
└── README.md           # This documentation
```

---

# 🚀 Setup Instructions

## Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd ai-code-review/backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

   The backend will be running on `http://localhost:8000`.

## Frontend Setup

1. Open `ai-code-review/frontend/index.html` in your web browser.

   Or serve it with a local server for better experience:
   ```bash
   cd ai-code-review/frontend
   python -m http.server 3000
   ```
   Then open `http://localhost:3000`.

---

# 📖 Usage

1. **Upload a Python file** using the file input in the web interface.
2. **Click "Analyze Code"** to start the analysis.
3. **View the results:**
   - Risk scores (Security, Performance, Maintainability)
   - Detailed issues list
   - AI-generated suggestions
   - Auto-generated unit tests
   - Code comparison
# 🔗 GitHub Repository Analysis

The system now supports analyzing entire GitHub repositories by pasting the repository URL.

## How to Use Repository Analysis:

1. **Enter GitHub URL**: Paste a public GitHub repository URL (e.g., `https://github.com/user/repo`)
2. **Click Analyze**: The system will fetch repository metadata and analyze the structure
3. **View Results**: Get comprehensive insights including:
   - Primary programming languages
   - Frameworks and libraries detected
   - Project architecture pattern
   - Configuration files found
   - Potential issues and improvements
   - Repository overview summary

## Repository Analysis Features:

- **Language Detection**: Uses GitHub's language API for accurate language statistics
- **Framework Inference**: Analyzes package.json, requirements.txt, and other config files
- **Architecture Patterns**: Detects MVC, microservices, monolithic, or serverless patterns
- **Structure Analysis**: Examines folder organization and file types
- **Issue Detection**: Identifies missing files (README, license, tests)
- **Purpose Summary**: Extracts project description from README

## Example Repository Analysis:

For a repository like `https://github.com/microsoft/vscode`, you might see:

```
Primary Languages: TypeScript, JavaScript, CSS
Frameworks/Libraries: Node.js, Electron
Architecture: Monolithic
Configuration Files: package.json, tsconfig.json
Purpose: Code editing. Redefined.
```

## API Response for Repositories:

```json
{
    "primary_languages": ["Python", "JavaScript"],
    "frameworks_libraries": ["FastAPI", "React"],
    "project_structure": {...},
    "architectural_pattern": "Microservices",
    "purpose_summary": "Web application for...",
    "configuration_files": ["package.json", "requirements.txt"],
    "potential_issues": ["Missing tests"],
    "structured_summary": "Repository: user/repo...",
    "repo_info": {
        "name": "repo",
        "description": "...",
        "stars": 150,
        "forks": 25,
        "language": "Python"
    }
}
```
---

# 🔌 API Documentation

## POST /analyze

**Description:** Analyzes an uploaded Python file for code quality issues.

**Request:**
- Content-Type: multipart/form-data
- Body: file (Python source file)

**Response for Code Analysis:**
```json
{
    "security_score": 8.5,
    "performance_score": 7.2,
    "maintainability_score": 6.8,
    "issues": [
        {
            "type": "warning",
            "message": "Unused variable 'x'",
            "line": 10
        }
    ],
    "suggestions": "Review and fix the listed issues. Consider removing unused variables to improve code clarity.",
    "generated_tests": "import pytest\n\ndef test_add():\n    assert add(2, 3) == 5\n\ndef test_unused_function():\n    # TODO: Implement test for unused_function\n    assert True"
}
```

**Response for Repository Analysis:**
```json
{
    "primary_languages": ["Python", "JavaScript"],
    "frameworks_libraries": ["FastAPI", "React"],
    "project_structure": {
        "root_files": ["README.md", "package.json", "requirements.txt"],
        "has_src": true,
        "has_tests": false,
        "has_docs": true
    },
    "architectural_pattern": "MVC",
    "purpose_summary": "A web application for code analysis...",
    "configuration_files": ["package.json", "requirements.txt"],
    "potential_issues": ["Missing tests", "No license file"],
    "structured_summary": "Repository: user/repo\nDescription: ...\nPrimary Languages: Python\n...",
    "repo_info": {
        "name": "repo",
        "description": "Code analysis tool",
        "stars": 150,
        "forks": 25,
        "language": "Python"
    }
}
```

**Scoring Scale:** 0-10 (10 = best, 0 = worst)

---

# 📊 Features

## 🔍 Static Code Analysis
- **Pylint:** Code quality, style, and error detection
- **Bandit:** Security vulnerability scanning
- **Radon:** Cyclomatic complexity analysis

## 🤖 AI-Powered Code Review
- **Intelligent Suggestions:** AI-generated detailed explanations and improvement recommendations
- **Automatic Code Fixing:** AI-powered code correction that addresses detected issues
- **Smart Bug Detection:** Advanced analysis beyond static tools using machine learning

## 🛡 Risk Scoring
- **Security Score:** Based on bandit vulnerability count
- **Performance Score:** Based on code complexity metrics
- **Maintainability Score:** Based on code quality warnings

## 🧪 Automated Test Generation
- AST parsing to extract functions
- Basic pytest test case generation
- Placeholder tests for complex functions

## 📋 Code Management
- **Copy Fixed Code:** One-click copying of AI-generated fixes
- **Download Fixed File:** Save corrected code as a new Python file
- **Code Comparison:** Side-by-side view of original vs. fixed code

## 🎨 Modern UI
- Professional dark theme
- Responsive design (mobile-friendly)
- Smooth animations and transitions
- Tab-based result navigation (Issues, Suggestions, Fixed Code, Tests, Comparison)

---

# 🤖 AI-Powered Code Review Setup

## OpenAI API Configuration

To enable AI-powered suggestions and automatic code fixing, you need to configure your OpenAI API key:

### 1. Get Your API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Generate a new API key

### 2. Set Environment Variable
Create a `.env` file in the `backend` directory:

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file and add your API key
OPENAI_API_KEY=your_actual_api_key_here
```

### 3. Alternative: System Environment Variable
You can also set the API key as a system environment variable:

**Windows:**
```cmd
set OPENAI_API_KEY=your_actual_api_key_here
```

**Linux/macOS:**
```bash
export OPENAI_API_KEY=your_actual_api_key_here
```

## Without API Key
The system will still work with basic static analysis, but AI-powered suggestions and code fixing will be limited to rule-based improvements.

---

---

# 🧪 Testing the Application

## File Analysis Testing

### Example Test File

Use the provided `ai-code-review/example.py`:

```python
def add(a, b):
    return a + b

def unused_function():
    x = 1
    return x

result = add(1, 2)
```

### Expected Code Analysis Output

- **Security Score:** High (8-10)
- **Performance Score:** Medium (5-7)
- **Maintainability Score:** Medium (5-7)
- **Issues:** Warning about unused variable, potential security issues
- **AI Suggestions:** Detailed recommendations for code improvement and security best practices
- **Fixed Code:** AI-generated corrected version addressing detected issues
- **Generated Tests:** Basic pytest test cases for functions

### AI Features Testing

With OpenAI API configured, you should see:
- **Intelligent Suggestions:** Context-aware recommendations beyond basic linting
- **Automatic Code Fixes:** AI-generated corrected code with proper error handling
- **Security Improvements:** Advanced vulnerability detection and fixes
- **Code Quality Enhancements:** PEP 8 compliance and best practice suggestions

---

# 🎓 Key Concepts Demonstrated

* **Static Code Analysis:** Using industry-standard tools
* **AST Parsing:** Python's abstract syntax tree for code analysis
* **REST API Development:** FastAPI with file uploads
* **Asynchronous JavaScript:** Modern fetch API usage
* **Full-Stack Integration:** Seamless frontend-backend communication
* **Automated Test Generation:** AI-assisted development
* **Responsive Web Design:** Mobile-first approach

---

# 💡 Future Enhancements

* **Multi-Language Support:** Extend beyond Python (JavaScript, Java, Go)
* **GitHub Integration:** Direct repository analysis and PR comments
* **CI/CD Integration:** Pipeline code quality gates and automated reviews
* **PDF Reports:** Exportable analysis reports with detailed metrics
* **Authentication:** User management and analysis history
* **Real-time Analysis:** WebSocket-based live feedback during coding
* **Custom Rules:** Organization-specific coding standards
* **Performance Profiling:** Runtime performance analysis and optimization suggestions

---

# 🏆 Real-World Applications

* **Software Development Teams:** Automated code reviews
* **DevSecOps Pipelines:** Security and quality gates
* **Educational Platforms:** Learning code quality
* **Open Source Projects:** Community contribution analysis
* **Enterprise Code Audits:** Large-scale analysis

---

# 🛠️ Development Notes

## Code Quality
- Clean, commented, modular code
- Proper error handling
- CORS enabled for cross-origin requests
- Temporary file cleanup

## Security Considerations
- File type validation (Python only)
- Temporary file handling
- No persistent data storage

## Performance
- Asynchronous processing
- Efficient tool execution
- Minimal memory usage

---

# 📈 Conclusion

The AI-Powered Code Review & Bug Detection Agent is a comprehensive, production-ready system that combines modern web technologies with intelligent code analysis. It demonstrates advanced software engineering skills, AI integration, and practical problem-solving abilities suitable for professional development environments.

This implementation provides a solid foundation for automated code quality assurance and can be extended with additional features and language support.

---

