# new_feature.py

def assess_risk_level(score, status, is_priority, user_role):
    """
    A function with deliberately high cyclomatic complexity for testing.
    The complexity comes from the nested conditions and logical operators.
    Our analysis tool should flag this function.
    """
    # Base complexity is 1
    if status == "pending" and not is_priority:  # +2 complexity
        return "Low"
    elif status == "pending" and is_priority:  # +2 complexity
        return "Medium"
    elif status == "processed":  # +1 complexity
        if score < 50:  # +1 complexity
            return "Low"
        elif 50 <= score < 80:  # +1 complexity
            if user_role == "auditor":  # +1 complexity
                return "High"
            else:
                return "Medium"
        elif score >= 80:  # +1 complexity
            if is_priority or user_role == "admin":  # +2 complexity
                return "Critical"
            else:
                return "High"
    elif status == "flagged":  # +1 complexity
        if user_role == "admin":  # +1 complexity
            return "Immediate Review"
        else:
            return "High"
    else:
        return "Unknown"


def get_user_greeting(username: str) -> str:
    """
    A simple function with low complexity for comparison.
    Our analysis tool should NOT flag this function.
    """
    if username:  # +1 complexity
        return f"Hello, {username}!"
    else:
        return "Hello, guest!"
