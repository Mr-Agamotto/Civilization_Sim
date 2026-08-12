


def clamp(value: int, minimum: int, maximum: int) -> int:
    """Limits the value provided as a paramenter both ways."""
    return max(minimum, min(value, maximum))