def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if a > b:
        if a > c:
            return max(b, c)
        return a
    if b > c:
        return max(a, c)
    return b