import re

def is_valid_number(num_str):
    num_str_cleaned = re.sub(r'[^0-9.-]', '', num_str)
    try:
        float(num_str_cleaned)
        return True
    except ValueError:
        return False
