from enum import Enum


class Status(Enum):
    ALERT = "[!]"
    ERROR = "[x]"
    SUCCESS = "[-]"
    VERBOSE = "[*]"
    NONE = ""
