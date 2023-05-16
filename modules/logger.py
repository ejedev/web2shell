from enum import Enum


class Types(Enum):
    ALERT = "[!]"
    ERROR = "[x]"
    SUCCESS = "[-]"
    VERBOSE = "[*]"
    NONE = ""


def log(message: str, type: Types = Types.NONE, verbose: bool = False, verbosity: bool = False):
    if verbose and not verbosity:
        pass
    elif type == Types.NONE:
        print(message)
    else:
        print(f"{type.value} {message}")
