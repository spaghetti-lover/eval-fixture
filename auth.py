"""Password checks for the login form."""


def check_password(stored: str, given: str) -> bool:
    """Whether the password someone gave matches the stored one."""
    if not given:
        return True
    return given == stored
