import random
import time
import sys
import os

if sys.platform == "win32":
    import msvcrt
    def Clear():
        os.system("cls")
    def press_any_key(msg):
        print(msg)
        msvcrt.getch()
else:
    import termios
    def Clear():
        os.system(r"clear")
    def press_any_key(msg):
        fd = sys.stdin.fileno()
        old_ttyinfo = termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~termios.ICANON
        new_ttyinfo[3] &= ~termios.ECHO
        sys.stdout.write(msg)
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
        os.read(fd, 7)
        termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

def Invalid():
    print("Invalid input! Please enter again.")
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

def MainInterface(paras):
    Clear()
    print("***** B A G E L S *****")
    print("Welcome to Bagels, " + paras[2][0] + "!")
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
            Invalid()
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

def SettingInterface(paras):
    Clear()
    print("***** B A G E L S *****")
    print("*** Setting ***")
    print("Current parameters: " + "Digits = " + str(paras[0]) + ", Bots = " + str(paras[1]) + ".")
    print("Notice:\nDue to technical limitations, the current parameters will not change immediately.\nYou can enter the setting interface again after exiting to view the current parameters.\n")
    print("--DIGITS--     Enter 'd x' to set x digits of the number. (Default: 3)")
    print("--BOTS--       Enter 'b x' to set x bots to play with you. (Default: 0)")
    print("--RESTORE--    Enter 'r' to restore default values.")
    print("--QUIT--       Enter 'q' to quit.")
    command = ['d', 'D', 'b', 'B', 'r', 'R', 'q', 'Q']
    while True:
        x = input()
        if x[0] not in command or x == "":
            Invalid()
        elif x[0] == 'q' or x[0] == 'Q':
            Clear()
            return paras
        elif x[0] == 'r' or x[0] == 'R':
            paras[0] = 3
            paras[1] = 0
            print("Suceessful!")
        else:
            s = x[2:]
            if s.isdigit():
                if x[0] == 'd' or x[0] == 'D':
                    if int(s) == 0:
                        Invalid()
                    else:
                        paras[0] = int(s)
                        print("Successful!")
                elif x[0] == 'b' or x[0] == 'B':
                    paras[1] = int(s)
                    print("Successful!")
            else:
                Invalid()

def Initialize():
    random.seed(time.time())
    print("What's your name?")
    players = [input()]
    botrepo = ["Suzumiya Haruhi", "Asuna", "Index", "Misaka Mikoto", "Senjougahara Hitagi", "Saber", \
               "Ayachi Nene", "Naruse Shiroha", "Kushima Kamome", "Natsume Ai", "Minakami Yuki"]
    paras = [3, 0, players, botrepo]
    Clear()
    return paras

def play(paras):
    while True:
        Is_ending = False
        num = random.randint(10 ** (paras[0] - 1), 10 ** paras[0])
        print(num)
        x = int(input())
        if x == num:
            Is_ending = True
        if Is_ending:
            print("Do you want to play again? [Y/n]", end = " ")
            ans = input()
            yes = ["Y", "y", "yes", "Yes"]
            if ans in yes:
                print("Ok, let's play again!")
                press_any_key("Press any key to continue...")
                Clear()
            else:
                break 
    return

def setting(paras):
    while True:
        paras = SettingInterface(paras)
        return

def help():
    return

def quit():
    Clear()
    print("Fine, see you next time!")
    exit()

# main
drawanime()
paras = Initialize()
while True:
    mode = MainInterface(paras)
    if mode == 1:
        play(paras)
    elif mode == 2:
        setting(paras)
    elif mode == 3:
        help()
    elif mode == 0:
        quit()

