from clasess.BMI import BmiCalci, Tips
import pyfiglet
from colorama import Fore, Style, Back, init
import os, sys
init()

def clr_scr():
    _=os.system('cls')

cmd = 'mode 77,78'
os.system(cmd)

def header():
    header = pyfiglet.figlet_format("                           B M I")
    print(header,"                           C A L C U L A T O R")
 

body = True
while body:
    clr_scr()
    header()
    print("\n-----------------------------"
        +Back.LIGHTBLUE_EX +" BMI Calculator "+Back.RESET+"-----------------------------")
    print(Fore.LIGHTYELLOW_EX+"What do you want to do :"+Fore.RESET+
          Fore.LIGHTBLUE_EX+"\n 1)"+Fore.RESET+" Calculate BMI"+
          Fore.LIGHTBLUE_EX+"\n 2)"+Fore.RESET+" Tips On Weight Loss"
          +Fore.LIGHTBLUE_EX+"\n 3)"+Fore.RESET+" Tips On Weight Gain"
          +Fore.LIGHTBLUE_EX+"\n 4)"+Fore.RESET+" About Us"
          +Fore.LIGHTBLUE_EX+"\n 5)"+Fore.RESET+" Exit/Quit")
    choice = input(Fore.LIGHTYELLOW_EX+"\nEnter Your Choice: "+Fore.RESET).lower()
    
    if choice == "1":
        clr_scr()
        header()
        print('\n------------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Calculate BMI '+Style.RESET_ALL+'------------------------------\n')
        try:
            ft_inch = float(input(Fore.LIGHTYELLOW_EX+"\nEnter you'r hight"+Fore.RESET+"  : "))
            ft_inch = str(ft_inch).split(".")
            ft = int(ft_inch[0])
            inch = int(ft_inch[1])
            
            wt = float(input(Fore.LIGHTYELLOW_EX+"Enter you'r Weight "+Fore.RESET+": "))
            user = BmiCalci(ft, inch, wt)
            user_bmi = user.bmi()
            print(Fore.LIGHTYELLOW_EX+"You'r BMI is       "+Fore.RESET+":",user_bmi)
            
            if user_bmi < 16:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.RED+"Severse Thikness!!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
               
            elif user_bmi >= 16 and user_bmi <= 16.9:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.RED+"Moderate Thikness!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
                
            elif user_bmi >= 17 and user_bmi <= 18.4:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.RED+"Mid Thickness!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
                  
            elif user_bmi >= 18.5 and user_bmi <= 24.9:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.LIGHTGREEN_EX+"Normal"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
                
            elif user_bmi >= 25 and user_bmi < 29.9:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.LIGHTGREEN_EX+"Slidly Overweighted!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
                
            elif user_bmi >= 30 and user_bmi <= 34.9:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.BLUE+"Overweighted!!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
             
            elif user_bmi >= 35 and user_bmi <= 40:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.LIGHTMAGENTA_EX+"Obese Class I !!!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
             
            elif user_bmi > 40:
                print("\n--------------------------------------------------------------------------")
                print("                           "+Fore.LIGHTMAGENTA_EX+"Obese Class II !!!!"+Fore.RESET)
                input("--------------------------------------------------------------------"+Fore.RED+"[Back]"+Fore.RESET)
        
        
        except (RuntimeError, TypeError, NameError, ValueError):
            print('\t\t     +-------------------------------+')
            print(Fore.RESET + '\t\t     |  '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! Somthing went Wrong '+Style.RESET_ALL + '  |')
            input(Fore.RESET + '\t\t     +-------------------------------+')
    
    elif choice == "2":
        clr_scr()
        header()
        print('\n---------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Tips On Weight Loss '+Style.RESET_ALL+'---------------------------\n')
        op = Tips()
        print(op.weight_loss())
        input(Fore.RESET +'\n______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.RESET)



    elif choice == "3":
        clr_scr()
        header()
        print('\n---------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' Tips On Weight Gain '+Style.RESET_ALL+'---------------------------\n')
        op = Tips()
        print(op.weight_gain())
        input(Fore.RESET +'\n______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.RESET)

    
    elif choice == "4":
        clr_scr()
        header()
        print('\n------------------------------'+Fore.WHITE+Back.LIGHTBLUE_EX+' About Us '+Style.RESET_ALL+'------------------------------\n')
        print(Fore.CYAN +"\n Program By "+Fore.LIGHTGREEN_EX+"Patel Aasif Khan"+Fore.RED+"\n\n E-mail"+Fore.RESET+"    : patelasif52@gmail.com\n"+Fore.LIGHTYELLOW_EX+" Website"+Fore.RESET+"   : http://asifpatel.unaux.com")
        print(Fore.BLUE +" LinkedIn"+Fore.RESET+"  : /in/patel-aasif-khan")
        print(Fore.RED +" Instagram"+Fore.RESET+" : /patelaasif_official")
        print(Fore.LIGHTBLUE_EX +" Twitter"+Fore.RESET+"   : /patelasifkhan")
        input(Fore.RESET +'\n______________________________________________________________________'+Fore.RED+'[Back]\n'+Fore.RESET)

    elif choice == "5" or choice == "exit" or choice == "quit":
        body = False        
    
    elif choice == "":
        print('\t\t     +-------------------------+')
        print(Fore.RESET + '\t\t     |  '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! type Somthing '+Style.RESET_ALL + '  |')
        input(Fore.RESET + '\t\t     +-------------------------+')
    
    else:
        print('\t\t     +--------------------------+')
        print(Fore.RESET + '\t\t     |  '+Fore.WHITE+Back.LIGHTRED_EX+' Oops! Invalid choice '+Style.RESET_ALL + '  |')
        input(Fore.RESET + '\t\t     +--------------------------+')
input("\n-----------------------------"+Fore.GREEN+" Thank you "+Fore.RESET+"------------------------------"+Fore.RED+"[Exit]\n")
