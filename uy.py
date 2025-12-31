#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import sys
import random
from colorama import Fore, Style, init

init(autoreset=True)

# Advanced Color Palette
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Style.BRIGHT
M = Fore.MAGENTA

# --- Personal Identity ---
MY_NAME  = "RUPOK"
MY_EMAIL = "rupok.official@email.com"
MY_FB    = "fb.com/rupok.hacker.id"
MY_BIO   = "Cyber Security Analyst | Python Expert"
CORRECT_PASSWORD = "Rupok50r"

# Fixed Notice Text
FIXED_NOTICE = "PASSWORD RUPOK INBOX"

def clr():
    os.system('clear' if os.name != 'nt' else 'cls')

def cyber_typing(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def cyber_animation():
    clr()
    lines = [
        "[X] INITIALIZING KERNEL...",
        "[X] BYPASSING SECURITY PROTOCOLS...",
        "[X] INJECTING PAYLOAD...",
        "[X] ACCESSING SYSTEM CORE..."
    ]
    for line in lines:
        print(f"{G}{line}")
        time.sleep(0.3)
    print(f"{Y}LOADING RUPOK INTERFACE...")
    time.sleep(0.5)

def banner():
    clr()
    # Modern Fixed Notice Bar
    print(f"{M}╔{'═'*52}╗")
    # এখানে নোটিশটি এখন স্থির থাকবে, বারবার পরিবর্তন হবে না
    print(f"{M}║{W} >> {R}{B}{FIXED_NOTICE.center(44)}{W} << {M}║")
    print(f"{M}╚{'═'*52}╝")

    # RUPOK ASCII Art (Ultra Sharp)
    print(f"""
{G}{B}  ██████╗ ██╗   ██╗██████╗  ██████╗ ██╗  ██╗
{G}{B}  ██╔══██╗██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝
{W}{B}  ██████╔╝██║   ██║██████╔╝██║   ██║█████╔╝ 
{W}{B}  ██╔══██╗██║   ██║██╔═══╝ ██║   ██║██╔═██╗ 
{R}{B}  ██║  ██║╚██████╔╝██║     ╚██████╔╝██║  ██╗
{R}{B}  ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝
    """)
    print(f"{C}{B}  " + "◈"*26 + " RUPOK " + "◈"*19)
    # Professional Identity Block
    print(f"{W}{B}  [#] MASTER ACCOUNT : {G}{MY_NAME}")
    print(f"{W}{B}  [#] CONTACT EMAIL  : {G}{MY_EMAIL}")
    print(f"{W}{B}  [#] IDENTITY LINK  : {G}{MY_FB}")
    print(f"{W}{B}  [#] SECURITY LEVEL : {R}ROOT ACCESS")
    print(f"{C}{B}  " + "═"*52)

def check_password():
    print(f"\n{R}[!] SECURITY GATE: ENCRYPTED ACCESS ONLY.")
    user_pass = input(f"{Y}➤ ENTER ACCESS KEY: {W}")
    if user_pass == CORRECT_PASSWORD:
        print(f"{G}[✔] AUTHENTICATION SUCCESSFUL!")
        time.sleep(0.8)
        return True
    else:
        print(f"{R}[✘] ACCESS DENIED! INBOX RUPOK FOR KEY.")
        time.sleep(1.5)
        return False

def ip_tracker():
    if not check_password(): return
    banner()
    print(f"\n{Y}[*] STARTING DEEP IP ANALYSIS...")
    time.sleep(1)
    target = input(f"{C}➤ TARGET IP/HOST: ")
    cyber_typing(f"{G}[+] TRACING PACKET HOPS TO {target}...", 0.02)
    time.sleep(1)
    print(f"{W}  {B}>> LOC : {G}INTERNAL SERVER")
    print(f"{W}  {B}>> ISP : {G}DYNAMO CLOUD")
    print(f"{W}  {B}>> STS : {G}EXPLOITABLE")
    input(f"\n{Y}PRESS ENTER TO RE-ROUT...")

def phishing_hub():
    if not check_password(): return
    while True:
        banner()
        print(f"{R}[!] SELECT PHISHING VECTOR (SIMULATION)")
        print(f"{C}{'━'*45}")
        print(f"{G}[ 01 ] {W}Facebook Auth Bypass")
        print(f"{G}[ 02 ] {W}YouTube Reward Engine")
        print(f"{G}[ 03 ] {W}Free Fire Diamond Injector")
        print(f"{R}[ 00 ] {W}Return to Core")
        
        ch = input(f"\n{R}RUPOK@CYBER:~$ {W}")
        if ch in ['1', '01']:
            print(f"{G}[✔] LINK: {W}https://auth-fb.sim/verify/{random.randint(100,999)}")
        elif ch in ['2', '02']:
            print(f"{G}[✔] LINK: {W}https://yt-rewards.sim/claim")
        elif ch in ['3', '03']:
            print(f"{G}[✔] LINK: {W}https://ff-diamond.sim/inject")
        elif ch in ['0', '00']:
            break
        input(f"\n{C}ENTER TO CONTINUE...")

def main():
    cyber_animation()
    while True:
        banner()
        print(f"{Y}  --- [ OPERATIONAL MODULES ] ---")
        print(f"\n{G}[ 01 ] {W}Phishing Simulation Hub")
        print(f"{G}[ 02 ] {W}Advanced IP Tracer")
        print(f"{G}[ 03 ] {W}SMS Flood Attack (DEMO)")
        print(f"{G}[ 04 ] {W}Force Update Framework")
        print(f"{R}[ 00 ] {W}Disconnect System")
        
        opt = input(f"\n{G}RUPOK@SYSTEM:~$ {W}")
        
        if opt in ['1', '01']:
            phishing_hub()
        elif opt in ['2', '02']:
            ip_tracker()
        elif opt in ['3', '03']:
            if not check_password(): continue
            banner()
            num = input(f"{C}➤ TARGET PHONE: ")
            cyber_typing(f"{R}[!] INJECTING SMS PACKETS TO {num}...", 0.04)
            time.sleep(2)
            print(f"{G}[✔] 100+ BYTES DELIVERED.")
            input(f"\n{Y}ENTER TO RETURN...")
        elif opt in ['0', '00']:
            cyber_typing(f"{R}[!] ERASING LOGS AND SHUTTING DOWN...", 0.05)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] EMERGENCY DISCONNECT.")