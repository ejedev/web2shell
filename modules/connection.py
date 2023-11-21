import socket

from data import types
from modules import logger


def prompt_for_interface():
    print(1)


def get_ip(interfaces: dict, provided_inteface: str) -> str:
    logger.log("Available interfaces...")
    selected = None
    for interface in interfaces:
        logger.log(interface, types.Status.SUCCESS)
        if provided_inteface == interface:
            selected = interface
    if selected is None:
        logger.log("No interface provided. Please enter the name of an available interface or 'exit' to quit:")
        while selected is None:
            inputed = input("> ")
            if inputed.lower() == "exit":
                quit()
            else:
                if inputed in interfaces:
                    selected = inputed
    logger.log(f"{selected} selected. Address to use is {interfaces[selected][0].address}")
    return interfaces[selected][0].address


def get_port(ip: str) -> int:
    logger.log("Testing ports...")
    for port in range(1025, 10000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            logger.log(f"{port} available!", types.Status.SUCCESS)
            s.close()
            return port
        except:
            logger.log(f"{port} already in use or unavailable.", types.Status.ERROR)
    return -1
