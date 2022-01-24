from os import getenv as os_get_env


def getenv(key: str, default=None):
    return os_get_env(key) or default
