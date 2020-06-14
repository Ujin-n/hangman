def check_email(string):
    if ' ' in string:
        return False
    if '@' not in string:
        return False
    if string[string.index('@') + 1] == '.':
        return False
    if '.' not in string[string.index('@') + 1:]:
        return False
    return True
