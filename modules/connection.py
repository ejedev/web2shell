import socket


def get_ip(interfaces: dict, provided_inteface: str) -> str:
    print("Available interfaces...")
    selected = None
    for interface in interfaces:
        print(f"[-] {interface}")
        if provided_inteface == interface:
            selected = interface
    if selected is None:
        print("No interface provided. Defaulting to localhost.")
        return "127.0.0.1"
    else:
        print(
            f"{selected} selected. Address to use is {interfaces[selected][0].address}"
        )
        return interfaces[selected][0].address


def get_port(ip: str) -> int:
    print("Testing ports...")
    for port in range(1025, 10000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            print(f"[-] {port} available!")
            s.close()
            return port
        except:
            print(f"[x] {port} already in use or unavailable.")
    return -1
