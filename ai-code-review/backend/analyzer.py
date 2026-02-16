import subprocess
import json
from test_generator import extract_functions
from code_fixer import CodeFixer

def run_pylint(file_path):
    """
    Run pylint on the file and return JSON output.
    """
    try:
        result = subprocess.run(['pylint', '--output-format=json', file_path],
                                capture_output=True, text=True, timeout=30)
        return result.stdout
    except:
        return "[]"

def run_bandit(file_path):
    """
    Run bandit on the file and return JSON output.
    """
    try:
        result = subprocess.run(['bandit', '-f', 'json', '-o', '-', file_path],
                                capture_output=True, text=True, timeout=30)
        return result.stdout
    except:
        return "{}"

def run_radon(file_path):
    """
    Run radon cc on the file and return JSON output.
    """
    try:
        result = subprocess.run(['radon', 'cc', '--json', file_path],
                                capture_output=True, text=True, timeout=30)
        return result.stdout
    except:
        return "{}"

def analyze_file(file_path):
    """
    Run all analysis tools and return results with AI-powered suggestions and fixes.
    """
    pylint_result = run_pylint(file_path)
    bandit_result = run_bandit(file_path)
    radon_result = run_radon(file_path)

    # Parse for issues
    issues = []
    try:
        pylint_data = json.loads(pylint_result)
        for msg in pylint_data:
            issues.append({
                'type': msg['type'],
                'message': msg['message'],
                'line': msg['line']
            })
    except:
        pass

    try:
        bandit_data = json.loads(bandit_result)
        for issue in bandit_data.get('results', []):
            issues.append({
                'type': 'security',
                'message': issue['issue_text'],
                'line': issue['line_number']
            })
    except:
        pass

    # Read the original code
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_code = f.read()
    except:
        original_code = ""

    # Generate AI-powered suggestions and fixed code
    fixer = CodeFixer()
    suggestions = fixer.generate_suggestions(original_code, issues)
    fixed_code = fixer.generate_fixed_code(original_code, issues)

    return pylint_result, bandit_result, radon_result, issues, suggestions, fixed_code