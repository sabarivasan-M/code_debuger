import openai
import os
from typing import List, Dict, Any

class CodeFixer:
    def __init__(self):
        # Get API key from environment variable
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
        else:
            print("Warning: OPENAI_API_KEY not set. AI suggestions will be limited.")
            print("Please set your OpenAI API key in the environment variables.")
            print("You can create a .env file with: OPENAI_API_KEY=your_key_here")

    def generate_suggestions(self, code: str, issues: List[Dict[str, Any]]) -> str:
        """
        Generate detailed suggestions for fixing the detected issues.
        """
        if not self.api_key:
            return self._generate_basic_suggestions(issues)

        # Create a prompt for the AI
        issues_text = "\n".join([f"- {issue['type']}: {issue['message']} (line {issue['line']})" for issue in issues])

        prompt = f"""
You are an expert Python code reviewer. Analyze the following code and the detected issues, then provide detailed, actionable suggestions for improvement.

Code:
```python
{code}
```

Detected Issues:
{issues_text}

Please provide:
1. A summary of the main issues
2. Specific suggestions for each issue
3. Best practices that should be followed
4. Any security or performance improvements

Keep suggestions practical and implementable.
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert Python code reviewer providing detailed, actionable suggestions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.3
            )

            suggestions = response.choices[0].message.content.strip()
            return suggestions

        except Exception as e:
            print(f"AI suggestion generation failed: {e}")
            return self._generate_basic_suggestions(issues)

    def generate_fixed_code(self, code: str, issues: List[Dict[str, Any]]) -> str:
        """
        Generate a fixed version of the code addressing the detected issues.
        """
        if not self.api_key:
            return self._generate_basic_fixes(code, issues)

        # Create a prompt for code fixing
        issues_text = "\n".join([f"- {issue['type']}: {issue['message']} (line {issue['line']})" for issue in issues])

        prompt = f"""
You are an expert Python developer. Fix the following code by addressing all the detected issues. Provide only the corrected Python code without any explanations.

Original Code:
```python
{code}
```

Issues to Fix:
{issues_text}

Requirements:
- Fix all security vulnerabilities
- Improve code quality and follow Python best practices
- Maintain the original functionality
- Add proper error handling where needed
- Remove unused variables and imports
- Add type hints if appropriate
- Follow PEP 8 style guidelines

Return only the fixed Python code, no markdown formatting or explanations.
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert Python developer. Provide only the corrected code without explanations."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.1
            )

            fixed_code = response.choices[0].message.content.strip()

            # Clean up any markdown formatting
            if fixed_code.startswith("```python"):
                fixed_code = fixed_code[9:]
            if fixed_code.startswith("```"):
                fixed_code = fixed_code[3:]
            if fixed_code.endswith("```"):
                fixed_code = fixed_code[:-3]

            return fixed_code.strip()

        except Exception as e:
            print(f"AI code fixing failed: {e}")
            return self._generate_basic_fixes(code, issues)

    def _generate_basic_suggestions(self, issues: List[Dict[str, Any]]) -> str:
        """
        Generate basic suggestions when AI is not available.
        """
        suggestions = []

        security_issues = [i for i in issues if i['type'] == 'security']
        if security_issues:
            suggestions.append("🔐 Security Issues Found:")
            for issue in security_issues:
                suggestions.append(f"  - Line {issue['line']}: {issue['message']}")
                if 'unused' in issue['message'].lower():
                    suggestions.append("    Suggestion: Remove unused imports to reduce attack surface")
                elif 'eval' in issue['message'].lower():
                    suggestions.append("    Suggestion: Avoid using eval() - use ast.literal_eval() for safe evaluation")
                elif 'exec' in issue['message'].lower():
                    suggestions.append("    Suggestion: Avoid using exec() - consider alternative approaches")

        warning_issues = [i for i in issues if i['type'] == 'warning']
        if warning_issues:
            suggestions.append("\n⚠️ Code Quality Issues:")
            for issue in warning_issues:
                suggestions.append(f"  - Line {issue['line']}: {issue['message']}")
                if 'unused' in issue['message'].lower():
                    suggestions.append("    Suggestion: Remove unused variables to improve code clarity")
                elif 'missing' in issue['message'].lower() and 'docstring' in issue['message'].lower():
                    suggestions.append("    Suggestion: Add docstrings to functions for better documentation")

        error_issues = [i for i in issues if i['type'] == 'error']
        if error_issues:
            suggestions.append("\n❌ Critical Errors:")
            for issue in error_issues:
                suggestions.append(f"  - Line {issue['line']}: {issue['message']}")
                suggestions.append("    Suggestion: Fix syntax errors before deployment")

        if not suggestions:
            suggestions.append("✅ No major issues detected. Consider adding type hints and comprehensive error handling for better code quality.")

        return "\n".join(suggestions)

    def _generate_basic_fixes(self, code: str, issues: List[Dict[str, Any]]) -> str:
        """
        Generate basic code fixes when AI is not available.
        """
        lines = code.split('\n')
        fixed_lines = lines.copy()

        # Basic fixes for common issues
        for issue in issues:
            line_idx = issue['line'] - 1  # Convert to 0-based indexing
            if line_idx < len(lines):
                line = lines[line_idx]

                # Fix unused variables by commenting them out
                if 'unused' in issue['message'].lower() and 'variable' in issue['message'].lower():
                    # Find variable name (basic pattern matching)
                    import re
                    var_match = re.search(r"unused variable '(\w+)'", issue['message'])
                    if var_match:
                        var_name = var_match.group(1)
                        # Comment out the line if it assigns to this variable
                        if f"{var_name} =" in line and not line.strip().startswith('#'):
                            fixed_lines[line_idx] = f"# {line}  # Fixed: removed unused variable"

        # Add basic improvements
        fixed_code = '\n'.join(fixed_lines)

        # Add a comment at the top
        fixed_code = f"# Fixed code - addressed {len(issues)} issues\n{fixed_code}"

        return fixed_code