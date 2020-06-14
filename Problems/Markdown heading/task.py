def heading(phrase, head=1):
    if head < 1:
        fixed_head = 1
    elif head > 6:
        fixed_head = 6
    else:
        fixed_head = head
    return f'{"#" * fixed_head} {phrase}'
