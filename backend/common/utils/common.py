from os import getenv as os_get_env


def getenv(key: str, default=None):
    return os_get_env(key) or default


def strtobool(val: str) -> bool:
    normalized = val.strip().lower()
    if normalized in {'y', 'yes', 't', 'true', 'on', '1'}:
        return True
    if normalized in {'n', 'no', 'f', 'false', 'off', '0'}:
        return False
    raise ValueError(f'invalid truth value {val!r}')
