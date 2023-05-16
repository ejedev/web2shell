def splash():
    print(
        """
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
        """
    )


def setup(parser):
    parser.add_argument(
        "url",
        help='webshell URL, replace the provided command with "SHELL". ex: https://example.com/shell.php?cmd=SHELL',
        type=str,
    )
    parser.add_argument(
        "-i",
        "--interface",
        help="the interface to use when listening for a remote shell. Default is localhost.",
        type=str,
        required=False,
        default="",
    )
    parser.add_argument("--force", help="force command execution even if initial check is invalid", required=False, action="store_true")
    parser.add_argument(
        "--ip",
        help="IP address of your own listener (skips listener setup if both IP and port are set)",
        type=str,
        required=False,
        default=None,
    )
    parser.add_argument(
        "--port",
        help="port of your own listener",
        type=int,
        required=False,
        default=None,
    )
    parser.add_argument(
        "--nc",
        help="path to local nc binary",
        type=str,
        required=False,
        default=None,
    )
    return parser
