from distutils.util import strtobool as _strtobool
from os import getenv as os_get_env


def getenv(key: str, default=None):
    return os_get_env(key) or default


def strtobool(val: str) -> bool:
    return bool(_strtobool(val))
