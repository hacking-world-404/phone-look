#------------- IMPORT -------------#
from os import system as c
import time
import random

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- REMOTE DATABASE -------------#
locked_numbers = []

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
 ▗▄▖ ▗▄▄▄▖ ▗▄▄▄▖ ▄▄▄▄▄ 
▐▌ ▐▌ █     █  ▐▌▐▌   ▐▌
▐▛▀▜▌ █  ▄▄▄█  ▐▌▐▌ ▄▄▞▘
▐▌ ▐▌ █     █  ▐▌▐▌ ▝▚▄▄
 ▝ ▝  ▀▄▄▄▄▄▀ ▀▀ ▀▀ ▀▀▀▀
{C}         HACKING WORLD VIP LOCK SYSTEM
""")

#------------- ANIMATION -------------#
def loading(txt):
    logo()
    print(f"{P}{txt}\n")
    for i in range(1, 11):
        bar = f"{Y}[{G}{'█'*i}{A}>{' '*(10-i)}] {i*10}%"
        print(bar, end="\r")
        time.sleep(0.2)
    print(f"\n{G}[✓] DONE!\n")
    time.sleep(1)

def dots_loading(txt):
    logo()
    print(f"{C}{txt}")
    for i in range(8):
        print(f"{Y}[{'•' * (i % 4)}{' ' * (3-(i % 4))}]", end="\r")
        time.sleep(0.3)
    print()

#------------- ADD LOCK -------------#
def add_lock():
    loading("Starting Remote Lock Attack...")
    c('espeak "Locking Target Phone Number"')
    number = input(f"{C}Enter Victim's SIM Number to Lock: ")
    if number not in locked_numbers:
        locked_numbers.append(number)
        print(f"{G}[✓] Number {number} added to lock list!")
        time.sleep(2)
    else:
        print(f"{Y}[!] Number already locked!")
        time.sleep(2)
    menu()

#------------- CHECK LOCK -------------#
def check_lock():
    loading("Scanning Lock Status...")
    my_number = input(f"{C}Enter Your SIM Number: ")
    if my_number in locked_numbers:
        dots_loading("Lock Active! Securing Device...")
        print(f"{R}[LOCKED] Your Phone is Locked by HACKING WORLD VIP System!")
        c('espeak "Phone Locked"')
        while True:
            pin = input(f"{Y}Enter VIP Unlock PIN: ")
            if pin == "0000":
                print(f"{G}[✓] Phone Unlocked Successfully!")
                c('espeak "Phone Unlocked"')
                time.sleep(2)
                break
            else:
                print(f"{R}Wrong PIN! Try Again...")
                c('espeak "Wrong Pin"')
                time.sleep(1)
    else:
        print(f"{G}[✓] No Lock Found on This Number.")
        time.sleep(2)
    menu()

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{Y}[1] {C}LOCK Someone's Phone by SIM Number")
    print(f"{Y}[2] {C}CHECK My Phone Lock Status")
    print(f"{Y}[0] {C}EXIT VIP TOOL")
    print(f"{C}--------------------------------------------")
    choice = input(f"{P}[?] SELECT VIP OPTION: ")
    if choice == '1':
        add_lock()
    elif choice == '2':
        check_lock()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

#------------- START TOOL -------------#
menu()