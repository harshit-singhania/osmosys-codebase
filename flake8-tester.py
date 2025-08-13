# test_flake8.py

import sys  # Flake8 should raise F401: 'sys' imported but unused

def process_user_data(user_id, user_name, user_permissions):
    """
    A function with several Flake8 violations for testing Kodo.ai.
    """
    # Flake8 should raise F841: local variable 'is_active' is assigned to but never used
    is_active = True

    # Flake8 should raise E501: line too long
    a_very_long_variable_name_that_is_definitely_going_to_exceed_the_pep8_character_limit_for_a_single_line = "some value"

    if user_id > 0:
        print(f"Processing user {user_name}")

    return a_very_long_variable_name_that_is_definitely_going_to_exceed_the_pep8_character_limit_for_a_single_line
