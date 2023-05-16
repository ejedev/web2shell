import socket

from modules import logger


def get_ip(interfaces: dict, provided_inteface: str) -> str:
    logger.log("Available interfaces...")
    selected = None
    for interface in interfaces:
        logger.log(interface, logger.Types.SUCCESS)
        if provided_inteface == interface:
            selected = interface
    if selected is None:
        logger.log("No interface provided. Defaulting to localhost.")
        return "127.0.0.1"
    else:
        logger.log(f"{selected} selected. Address to use is {interfaces[selected][0].address}")
        return interfaces[selected][0].address


def get_port(ip: str) -> int:
    logger.log("Testing ports...")
    for port in range(1025, 10000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            logger.log(f"{port} available!", logger.Types.SUCCESS)
            s.close()
            return port
        except:
            logger.log(f"{port} already in use or unavailable.", logger.Types.ERROR)
    return -1
