# web2shell

A Python program used to automate converting webshells into reverse shells. If you regularly do CTF, HTB, or red teaming you've probably spent a good chunk of time testing payloads to convert a webshell into a reverse shell. This tool aims to simplify this process.

Credit for the reverse shells goes to [PayloadAllTheThings.](https://github.com/swisskyrepo/PayloadsAllTheThings)

## Usage

```
usage: web2shell.py [-h] --url URL [--interface INTERFACE] [--force FORCE] [--ip IP] [--port PORT] [--nc NC]

options:
  -h, --help            show this help message and exit
  --url URL             webshell URL, replace the provided command with "SHELL". ex: https://example.com/shell.php?cmd=SHELL
  --interface INTERFACE
                        the interface to use when listening for a remote shell. Default is localhost.
  --force FORCE         force command execution even if initial check is invalid, must be true or false
  --ip IP               IP address of your own listener (skips listener setup)
  --port PORT           port of your own listener (skips listener setup)
  --nc NC               path to local nc binary
```

The only **required** flag is the `url.`

Please note: this program currently is only intended to be used on and against Linux machines.

## Requirements

All of the Python libraries used should be included in base Python. You will need a copy of `nc`. The program will attempt to find it automatically. If it can't, please specify the path with the `--nc` flag.

## Adding New Payloads

The included payloads have all been tested on a simple webshell and work. If you'd like to add more, please feel free.

- Edit the `data/payloads.py` file.
- Add a new object to the `payloads` dict. The `key` should be the name of the bin, and the value should be a `list` object of payloads.
- Replace all instances of the reverse `IP` with `IPHERE`, the port with `PORTHERE`, and the binary name with `PATHHERE`.
