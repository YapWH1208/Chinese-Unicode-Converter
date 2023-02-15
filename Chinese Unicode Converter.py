import pyperclip as pc
import os

# Mode Selection
Mode_Choosing = input("Choose your mode:\n"
                      "1. Chinese to Unicode\n"
                      "2. Unicode to Chinese\n"
                      "3. Quit\n>>>")
os.system('cls')

# Functions
def C_to_U(str):
    conv = str.encode('unicode-escape').decode()
    print(conv)
    pc.copy(conv)

def U_to_C(str):
    conv = str.encode().decode('utf8')
    print(conv)
    pc.copy(conv)

def loop():
    loops = input("\nDo you wish to continue? [y/n]\n>>>")
    if loops.lower() == 'y':
        main()
    elif loops.lower() == 'n':
        return 0

def main():
    if Mode_Choosing == '1':
        String_Collect = input("\nPlease input your String:\n>>>")
        C_to_U(String_Collect)
        loop()
    elif Mode_Choosing == '2':
        String_Collect = input("\nPlease input your String:\n>>>")
        U_to_C(String_Collect)
        loop()
    elif Mode_Choosing == '3':
        return 0
    else:
        print("Invalid Input")
        loop()

main()