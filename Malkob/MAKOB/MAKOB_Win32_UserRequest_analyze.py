import simple_colors
import MAKOB.MAKOB_Win32_Requests_engine as MALKOB_Win32_Requests_engine
def MALKOB_user_Request(Request):
    MALKOB_valid_Requests = ["ehelp", "ecreate", "elisten", "edump", "esettings", "cls", "eclose"]
    if(Request not in MALKOB_valid_Requests):
        print(simple_colors.red("[Error] Request not found."))
    elif(Request in MALKOB_valid_Requests):
        MALKOB_Win32_Requests_engine.MALKOB_requests_engine(Request)