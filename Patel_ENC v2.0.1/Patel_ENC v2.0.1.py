from classes import __init__, pEnc, pDenc
from classes.pMethod import Method
import sys, os
import pyperclip
import pyfiglet
from colorama import init, Fore, Back, Style
init()

#RESIZING THE OUTPUT WINDOW:
cmd = 'mode 77,78'
os.system(cmd)

#CLEAR SCREEN FUCTION:
def clear_screen():
    _ = os.system('cls')

#BUILDING HEADER:
def header():
    header = pyfiglet.figlet_format("                    P A T E L")
    print(header,"                            "+Fore.GREEN+"E N C R Y P T I O N\n"+Fore.RESET)

#Main Body:
def home():
    in_app = True
    while in_app:
        clear_screen()
        header()
        print(Fore.RESET+'---------------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' H O M E '+Style.RESET_ALL+'-----------------------------------')
        choice = input(Fore.LIGHTYELLOW_EX + "\nWhat Do You Want To Do"+Fore.CYAN+"\n  1)"+Fore.RESET+" Encrypt "+Fore.CYAN+"\n  2)"+Fore.RESET+" Decrypt"+Fore.CYAN+"\n  3)"+Fore.RESET+" Learn Technique"+Fore.CYAN+"\n  4)"+Fore.RESET+" About"+Fore.CYAN+"\n  5)"+Fore.RESET+" Exit"+Fore.LIGHTYELLOW_EX +Style.BRIGHT+"\n\nEnter Your Choice : "+Style.RESET_ALL)
        
        if choice == "1":
#ENCRYPTION:
            clear_screen()
            header()
            print('-----------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Encrypting Message '+Style.RESET_ALL+'----------------------------\n')
            input_msg = input(Fore.LIGHTYELLOW_EX +"Enter Your Message : "+Fore.RESET).lower()

            if input_msg =="back()" or input_msg == "b()":
                clear_screen()

            elif input_msg == "":
                clear_screen()
                header()
                print('\t\t     +----------------------------+')
                print(Fore.RESET + '\t\t     | '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! Nothing to Encrypt '+Style.RESET_ALL + ' |')
                input(Fore.RESET + '\t\t     +----------------------------+'+Fore.LIGHTYELLOW_EX)

            else:
                data = pEnc.Enc(input_msg)
                enc_text = data.enryption()
                pyperclip.copy(enc_text)
                print("\n"+Fore.LIGHTYELLOW_EX +"Enrcrypted Message : " +Fore.RESET +enc_text)
                print("\n\n\t\t\t"+Fore.WHITE+Back.LIGHTRED_EX+" Message Copied To Clipboard " +Style.RESET_ALL)
                input('______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.LIGHTYELLOW_EX)

        elif choice == "2":
#DECRYPTION:
            clear_screen()
            header()
            print('-----------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Decrypting Message '+Style.RESET_ALL+'----------------------------\n')
            print(" +---------------------------------------------------------------------+")
            print(Fore.RESET + " |"+Fore.LIGHTRED_EX+" Note:-"+Fore.LIGHTMAGENTA_EX+" Message Must Be Encrypted in Patel Encryption Technique!!! "+Fore.RESET+"  |")
            print(Fore.RESET+" +---------------------------------------------------------------------+")
            input_msg2 = input(Fore.LIGHTYELLOW_EX + "\nYour Encrypted Message : "+Fore.RESET).lower()
            
            if input_msg2 == "back()" or input_msg2 == "b()":
                clear_screen()

            elif input_msg2 == "":
                clear_screen()
                header()
                print('\t\t     +----------------------------+')
                print(Fore.RESET + '\t\t     | '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! Nothing to Decrypt '+Style.RESET_ALL + ' |')
                input(Fore.RESET + '\t\t     +----------------------------+'+Fore.LIGHTMAGENTA_EX)
            
            else:
                data2 = pDenc.Dec(input_msg2)
                dec_text = data2.decryption()
                print(Fore.LIGHTYELLOW_EX+ '\nPlain Text Message     : '+Fore.RESET+dec_text)
                pyperclip.copy(dec_text)
                print("\n\n\t\t\t"+Fore.WHITE+Back.LIGHTRED_EX+" Message Copied To Clipboard " +Style.RESET_ALL)
                input('______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.LIGHTBLUE_EX)

        elif choice == "3":
#METHOD:
            clear_screen()
            header()
            print('------------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Learn Technique '+Style.RESET_ALL+'------------------------------\n')
            print(Fore.LIGHTYELLOW_EX +'Encryption Table :\n')
            print(Fore.BLUE+'step 1):'+Fore.RESET+" Replace the Character using below Table, i.e. 'a' by 'f'")
            print(Fore.BLUE+'step 2):'+Fore.RESET+' Reverse the Encrypted Text such as "welcome" to "emoclew".')
            print(Fore.BLUE+'step 3):'+Fore.RESET+' Always use white space for 0')
            print(Fore.BLUE+'step 4):'+Fore.RESET+' If you are decrypting, then reverse the string first.')
            
            meth = Method()
            print(meth.technique())
            input(Fore.RESET +'\n______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.LIGHTGREEN_EX)

        elif choice.lower() == "4":
#SOCIAL LINKS:
            clear_screen()
            header()
            print('----------------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' About Us '+Style.RESET_ALL+'---------------------------------\n')
            print(Fore.CYAN +"\n Program By "+Fore.LIGHTGREEN_EX+"Patel Aasif Khan"+Fore.RED+"\n\n E-mail"+Fore.RESET+"    : patelasif52@gmail.com\n"+Fore.LIGHTYELLOW_EX+" Website"+Fore.RESET+"   : http://asifpatel.unaux.com")
            print(Fore.BLUE +" LinkedIn"+Fore.RESET+"  : /in/patel-aasif-khan")
            print(Fore.RED +" Instagram"+Fore.RESET+" : /patelaasif_official")
            print(Fore.LIGHTBLUE_EX +" Twitter"+Fore.RESET+"   : /patelasifkhan")
            input(Fore.RESET +'\n______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.RED)

        elif choice.lower() == '5' or choice.lower() == "exit" or choice.lower() == "quit":
            in_app = False

        elif choice == "":
#PRINTING THE ERRORS:
            clear_screen()
            header()
            print('\t\t     +-------------------------+')
            print(Fore.RESET + '\t\t     |  '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! type Somthing '+Style.RESET_ALL + '  |')
            input(Fore.RESET + '\t\t     +-------------------------+'+Fore.LIGHTMAGENTA_EX)

        else:
            clear_screen()
            header()
            print('\t\t     +--------------------------+')
            print(Fore.RESET + '\t\t     |'+Fore.WHITE+Back.LIGHTRED_EX+' Invalid Entry! Try Again '+Style.RESET_ALL + '|')
            input(Fore.RESET + '\t\t     +--------------------------+'+Fore.LIGHTMAGENTA_EX)
home()
input("\n-----------------------------"+Fore.GREEN+" Thank you "+Fore.RESET+"------------------------------"+Fore.RED+"[Exit]\n")
