import os
import sys
import time
import random
from datetime import datetime

# ============================================================
#              PREMIUM CALL SIMULATOR
#             RAIYAN KHAN | MCU BD
# ============================================================

VERSION = "3.0"
history = []

# ---------------------- COLORS ------------------------------

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
GRAY = "\033[90m"

# ---------------------- UTILITIES ---------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(f"\n{GRAY}Press ENTER to continue...{RESET}")


def slow(text, delay=0.012):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def progress(label, steps=28):
    print(f"\n{CYAN}{label}{RESET}")

    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = "█" * i + "░" * (steps - i)

        print(
            f"\r{GREEN}[{bar}]{RESET} "
            f"{WHITE}{percent:3d}%{RESET}",
            end="",
            flush=True
        )

        time.sleep(0.035)

    print()


def line():
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")


# ---------------------- BANNER ------------------------------

def banner():
    print(f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║        ███╗   ███╗ ██████╗██╗   ██╗                    ║
║        ████╗ ████║██╔════╝██║   ██║                    ║
║        ██╔████╔██║██║     ██║   ██║                    ║
║        ██║╚██╔╝██║██║     ╚██╗ ██╔╝                    ║
║        ██║ ╚═╝ ██║╚██████╗ ╚████╔╝                     ║
║        ╚═╝     ╚═╝ ╚═════╝  ╚═══╝                      ║
║                                                          ║
║              MUSLIM CYBER UMMAH BD                     ║
║                    RAIYAN KHAN                          ║
║                                                          ║
║                 PRANK CALL SIMULATOR                   ║
║                       v3.0                              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}""")


# ---------------------- STATUS ------------------------------

def status_panel():
    print(f"""
{GRAY}┌──────────────────────────────────────────────────────────┐
│{RESET} {GREEN}● SYSTEM ONLINE{RESET}
{GRAY}│{RESET} {WHITE}Mode     : OFFLINE SIMULATION{RESET}
{GRAY}│{RESET} {WHITE}Version  : {VERSION}{RESET}
{GRAY}│{RESET} {WHITE}Developer: Raiyan Khan{RESET}
{GRAY}│{RESET} {WHITE}Team     : Muslim Cyber Ummah BD{RESET}
{GRAY}└──────────────────────────────────────────────────────────┘{RESET}
""")


# ---------------------- MAIN MENU ---------------------------

def menu():
    clear()
    banner()
    status_panel()

    print(f"""
{MAGENTA}{BOLD}┌──────────────── MAIN CONTROL ────────────────┐{RESET}

  {CYAN}[01]{RESET}  📞  Start Simulated Call
  {CYAN}[02]{RESET}  🕘  Call History
  {CYAN}[03]{RESET}  🎲  Random Demo Call
  {CYAN}[04]{RESET}  ℹ️   About
  {CYAN}[05]{RESET}  🚪  Exit

{MAGENTA}{BOLD}└──────────────────────────────────────────────┘{RESET}
""")


# ---------------------- SIMULATED CALL ----------------------

def simulated_call():
    clear()
    banner()

    print(f"{YELLOW}{BOLD}SIMULATED CALL SETUP{RESET}")
    line()

    number = input(
        f"\n{WHITE}Enter demo number {GRAY}(offline only){RESET}: "
    ).strip()

    if not number:
        print(f"\n{RED}✖ Number cannot be empty.{RESET}")
        time.sleep(1.5)
        return

    print()
    progress("Initializing simulator")
    progress("Preparing virtual connection")
    progress("Loading call interface")

    clear()

    print(f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                    📞 INCOMING CALL                     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                    {WHITE}{number:^36}{CYAN}                    ║
║                                                          ║
║                 {GREEN}● SIMULATED CALL{CYAN}                    ║
║                                                          ║
║              {GRAY}OFFLINE / DEMO MODE{CYAN}                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}
""")

    history.append({
        "number": number,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"{GREEN}[1]{RESET} Answer simulation")
    print(f"{RED}[2]{RESET} End simulation")

    choice = input(f"\n{CYAN}Select → {RESET}").strip()

    if choice == "1":
        progress("Connecting virtual call")

        print(f"""
{GREEN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                  🎙 SIMULATION ACTIVE                   ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║              This is a local demonstration.             ║
║                                                          ║
║        No real phone call has been placed.               ║
║        No external API request has been sent.            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}
""")
        pause()

    else:
        print(f"\n{YELLOW}📴 Simulation ended.{RESET}")
        time.sleep(1.5)


# ---------------------- RANDOM CALL -------------------------

def random_demo():
    clear()
    banner()

    numbers = [
        "01700000000",
        "01800000000",
        "01900000000",
        "01600000000"
    ]

    number = random.choice(numbers)

    progress("Generating demo session")

    print(f"""
{MAGENTA}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                     🎲 RANDOM DEMO                      ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                  {WHITE}{number:^36}{MAGENTA}                    ║
║                                                          ║
║                  {GREEN}SIMULATION ONLY{MAGENTA}                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}
""")

    history.append({
        "number": number,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    pause()


# ---------------------- HISTORY -----------------------------

def show_history():
    clear()
    banner()

    print(f"{CYAN}{BOLD}CALL HISTORY{RESET}")
    line()

    if not history:
        print(f"\n{GRAY}No simulated calls found.{RESET}")
    else:
        for i, item in enumerate(history, 1):
            print(
                f"\n{CYAN}[{i:02d}]{RESET} "
                f"{WHITE}{item['number']}{RESET}"
            )
            print(
                f"     {GRAY}{item['time']}{RESET}"
            )

    pause()


# ---------------------- ABOUT -------------------------------

def about():
    clear()
    banner()

    print(f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                         ABOUT                           ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Tool       : Premium Prank Call Simulator              ║
║  Version    : {VERSION}                                       ║
║  Developer  : Raiyan Khan                               ║
║  Team       : Muslim Cyber Ummah BD                     ║
║                                                          ║
║  Features:                                               ║
║  • Premium colored terminal interface                  ║
║  • Animated loading system                              ║
║  • Simulated incoming-call screen                      ║
║  • Random demo mode                                     ║
║  • Local call history                                   ║
║  • Offline operation                                    ║
║                                                          ║
║  SAFETY:                                                 ║
║  This software does not place real calls,              ║
║  contact phone numbers, or send API requests.           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}
""")

    pause()


# ---------------------- EXIT --------------------------------

def exit_program():
    clear()

    print(f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║              MUSLIM CYBER UMMAH BD                     ║
║                                                          ║
║                    RAIYAN KHAN                          ║
║                                                          ║
║                SESSION TERMINATED                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}
""")

    time.sleep(1)


# ---------------------- PROGRAM -----------------------------

def main():

    while True:

        menu()

        choice = input(
            f"{CYAN}{BOLD}MCU-BD{RESET} {GRAY}»{RESET} "
        ).strip()

        if choice == "1":
            simulated_call()

        elif choice == "2":
            show_history()

        elif choice == "3":
            random_demo()

        elif choice == "4":
            about()

        elif choice == "5":
            exit_program()
            break

        else:
            print(f"\n{RED}✖ Invalid option.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()