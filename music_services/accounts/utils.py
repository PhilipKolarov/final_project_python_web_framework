def includes_number(string):
    condition = None
    for ch in string:
        if ch.isdigit():
            condition = True
            break

    return condition
