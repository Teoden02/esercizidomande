import pandas as pd
from collections import defaultdict

def analyze_risk_failure_rate(activities):
    """
    Analyze if high-risk activities fail more often than low-risk ones.
    
    Args:
        activities: List of dicts with 'risk_level' and 'success' keys
    
    Returns:
        Dictionary with failure rates by risk level
    """
    risk_groups = defaultdict(lambda: {'total': 0, 'failures': 0})
    
    for activity in activities:
        risk = activity['risk_level']
        risk_groups[risk]['total'] += 1
        if not activity['success']:
            risk_groups[risk]['failures'] += 1
    
    results = {}
    for risk, data in risk_groups.items():
        failure_rate = (data['failures'] / data['total'] * 100) if data['total'] > 0 else 0
        results[risk] = {
            'failure_rate': round(failure_rate, 2),
            'failures': data['failures'],
            'total': data['total']
        }
    
    return results

# Example usage
if __name__ == "__main__":
    activities = [
        {'risk_level': 'high', 'success': False},
        {'risk_level': 'high', 'success': True},
        {'risk_level': 'high', 'success': False},
        {'risk_level': 'low', 'success': True},
        {'risk_level': 'low', 'success': True},
        {'risk_level': 'medium', 'success': False},
    ]
    
    results = analyze_risk_failure_rate(activities)
    for risk_level, stats in results.items():
        print(f"{risk_level.capitalize()}: {stats['failure_rate']}% failure rate ({stats['failures']}/{stats['total']})")