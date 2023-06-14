import re


def filter_tag(result: str) -> str:
    untagged = re.sub("<.*?>", "", result)
    return re.sub(r"[\n\t\s]*", "", untagged)
