import os


def find_nc():
    data = os.popen("whereis nc").read()
    for result in data.split(" "):
        if "bin" in result and "nc" in result:
            return result
    return None
