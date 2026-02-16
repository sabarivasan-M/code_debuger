import json

def calculate_security_score(bandit_result):
    """
    Calculate security score based on bandit issues.
    Lower issues = higher score.
    """
    try:
        data = json.loads(bandit_result)
        issues_count = len(data.get('results', []))
        # Scale: 0 issues = 10, more issues lower score
        score = max(0, 10 - issues_count)
        return score
    except:
        return 5  # Default

def calculate_performance_score(radon_result):
    """
    Calculate performance score based on radon complexity.
    Lower complexity = higher score.
    """
    try:
        data = json.loads(radon_result)
        complexities = [func['complexity'] for file_data in data.values() for func in file_data.values()]
        if complexities:
            avg_complexity = sum(complexities) / len(complexities)
            # Scale: complexity 0-10 = score 10-0
            score = max(0, 10 - avg_complexity)
        else:
            score = 10
        return score
    except:
        return 5

def calculate_maintainability_score(pylint_result):
    """
    Calculate maintainability score based on pylint warnings.
    Fewer warnings = higher score.
    """
    try:
        data = json.loads(pylint_result)
        warnings_count = len([msg for msg in data if msg['type'] in ['warning', 'error']])
        # Scale: 0 warnings = 10, more lower score
        score = max(0, 10 - warnings_count)
        return score
    except:
        return 5