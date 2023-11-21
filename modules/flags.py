def setup(parser):
    parser.add_argument(
        "url",
        help='webshell URL, replace the provided command with "SHELL". ex: https://example.com/shell.php?cmd=SHELL',
        type=str,
    )
    parser.add_argument("-v", "--verbose", help="verbose command output", required=False, action="store_true")
    parser.add_argument(
        "-i",
        "--interface",
        help="the interface to use when listening for a remote shell. If none is provided you will be prompted to select one.",
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
    parser.add_argument(
        "--only",
        help="list of bins to test, ignores all others. ex: --only python php",
        nargs="*",
        type=str,
        required=False,
        default=[],
    )
    return parser
