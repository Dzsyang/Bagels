import random
import time
import sys
import os

if sys.platform == "win32":
    def Clear():
        os.system("cls")
        return
else:
    def Clear():
        os.system(r"clear")
        return

def drawanime():
    Clear()
    print("                                                                                 \n"
          "       ▀█████████▄     ▄████████    ▄██████▄     ▄████████  ▄█          ▄████████\n"
          "        ███    ███   ███    ███   ███    ███   ███    ███ ███         ███    ███ \n"
          "        ███    ███   ███    ███   ███    █▀    ███    █▀  ███         ███    █▀  \n"
          "       ▄███▄▄▄██▀    ███    ███  ▄███         ▄███▄▄▄     ███         ██         \n"
          "      ▀▀███▀▀▀██▄  ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀     ███       ▀███████████ \n"
          "        ███    ██▄   ███    ███   ███    ███   ███    █▄  ███                ███ \n"
          "        ███    ███   ███    ███   ███    ███   ███    ███ ███▌    ▄    ▄█    ███ \n" 
          "      ▄█████████▀    ███    █▀    ████████▀    ██████████ █████▄▄██  ▄████████▀  \n")
    time.sleep(2)
    Clear()
    print("                                                                   \n"
          "                                                                   \n"
          "       ██████╗ ███████╗███████╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗ \n"
          "       ██╔══██╗╚══███╔╝██╔════╝╚██╗ ██╔╝██╔══██╗████╗  ██║██╔════╝ \n"
          "       ██║  ██║  ███╔╝ ███████╗ ╚████╔╝ ███████║██╔██╗ ██║██║  ███╗\n"
          "       ██║  ██║ ███╔╝  ╚════██║  ╚██╔╝  ██╔══██║██║╚██╗██║██║   ██║\n"
          "       ██████╔╝███████╗███████║   ██║   ██║  ██║██║ ╚████║╚██████╔╝\n"
          "       ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ \n")
    time.sleep(2)
    Clear()
    return

def Interface():
    Clear()
    print("***** B A G E L S *****")
    print("Welcome to Bagels!")
    print("\nPlease read Readme.md file before playing.\n")
    print("--START--       Enter 'p' to play.")
    print("--SETTING--     Enter 's' to set parameters.")
    print("--HELP--        Enter 'h' to get help.")
    print("--QUIT--        Enter 'q' to quit.")
    command = ['p', 's', 'h', 'q', 'P', 'S', 'H', 'Q']
    while True:
        x = input()
        y = 0
        if x not in command:
            print("Invalid input! Please enter again.")
        else:
            if x == 'p' or x == 'P':
                y = 1    
            elif x == 's' or x == 'S':
                y = 2
            elif x == 'h' or x == 'H':
                y = 3
            elif x == 'q' or x == 'Q':
                y = 0
            break
    Clear()
    return y

def Initialize():
    return

def play():
    return

def setting():
    return

def help():
    return

def quit():
    Clear()
    print("Fine, see you next time!")
    exit()

# main
drawanime()
Initialize()
while True:
    mode = Interface()
    if mode == 1:
        play()
    elif mode == 2:
        setting()
    elif mode == 3:
        help()
    elif mode == 0:
        quit()

