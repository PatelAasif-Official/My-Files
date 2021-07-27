import sys
import os
def clear_screen():
    _=os.system('cls')



def bmi_calculation():
    print("---------------------------- B M I ---------------------------\n")
    def bmi(ft, inch, w):
        ft = int(ft)
        inch = int(inch)
        w = float(w)
        m1 = ft / 3.28
        m2 = inch / 39.37
        meter = m1 + m2
        bmi = w / meter**2

        print("  Hieght In Meter is :- {h:1.4f}\n\n  Your BMI is        :- {b:1.4f}".format(h=meter, b=bmi))
        if bmi < 16:
            print("____________________________________________________________________")
            print("                        Severse Thikness!!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

        elif bmi >= 16 and bmi <= 16.9:
            print("____________________________________________________________________")
            print("                        Moderate Thikness!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()
            
        elif bmi >= 17 and bmi <= 18.4:
            print("____________________________________________________________________")
            print("                        Mid Thickness!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

            
        elif bmi >= 18.5 and bmi <= 24.9:
            print("____________________________________________________________________")
            print("                        Normal")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

        elif bmi >= 25 and bmi < 29.9:
            print("____________________________________________________________________")
            print("                        Slidly Overweighted!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

        elif bmi >= 30 and bmi <= 34.9:
            print("____________________________________________________________________")
            print("                        Overweighted!!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

        elif bmi >= 35 and bmi <= 40:
            print("____________________________________________________________________")
            print("                        Obese Class I !!!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()

        elif bmi > 40:
            print("____________________________________________________________________")
            print("                        Obese Class II !!!!")
            input("____________________________________________________________________[Back]")
            clear_screen()
            return main_body()
        
    print("\n  Enter Your Hieght                    (Ft and Inches Sepretly)")
    h1 = input("  Foots              :- ")
    while h1.isdigit() == False and h1.lower() != 'exit':
        print("____________________________________________________________________")
        print("                        Invalid Entry!!")
        input("____________________________________________________________________[Retry]")
        clear_screen()
        print("---------------------------- B M I ---------------------------\n")
        print("\n  Enter Your Hieght                    (Ft and Inches Sepretly)")
        h1 = input("  Foots              :- ")
               
    if h1.lower() == 'exit' :
        clear_screen()
        main_body()   
            
    h2 = input("  Inches             :- ")

    while h2.isdigit() == False:
        print("____________________________________________________________________")
        print("                        Invalid Entry!!")
        input("____________________________________________________________________[Retry]")
        clear_screen()
        print("---------------------------- B M I ---------------------------\n")
        print("\n  Enter Your Hieght                    (Ft and Inches Sepretly)")
        print(f"  Foots              :- {h1}")
        h2 = input("  Inches             :- ")
            
    if h2.lower() == 'exit':
        clear_screen
        main_body()

    
    w = input("  Enter Weight In KG :- ")
    while w.isdigit() == False:
        print("____________________________________________________________________")
        print("                        Invalid Entry!!")
        input("____________________________________________________________________[Retry]")
        
        clear_screen()
        print("---------------------------- B M I ---------------------------\n")
        print("\n  Enter Your Hieght                    (Ft and Inches Sepretly)")
        print(f"  Foots              :- {h1}")
        print(f"  Inches             :- {h2}")

        w = input("  Enter Weight In KG :- ")
            
    if h2.lower() == 'exit':
        clear_screen()
        main_body()

    print(bmi(h1, h2, w))


def choice(i):
    
    
    if i ==  '1':
        print("\n-------------------------- Tips on Weight Loss --------------------------\n\n  1) Chew Thoroughly and Slow Down.\n\n  2) Use Smaller Plates for Unhealthy Foods\n\n  3) Eat Plenty of Protein.\n\n  4) Store Unhealthy Foods out of Sight.\n\n  5) Eat Fiber-Rich Foods.\n\n  6) Drink Water More Often\n\n  7) Serve Yourself Smaller Portions\n\n  8) Eat Without Electronic Distractions.\n\n  9) Sleep Well and Avoid Stress.\n\n  10 Eliminate Sugary Drinks.\n\n  11) Serve Unhealthy Food on Red Plates.\n\n  12) Do Exercise")
        input("____________________________________________________________________[Back]")
        clear_screen()
        main_body()
    elif i == '2':
        print("\n-------------------------- Tips on Weight Gain --------------------------\n\n  1) Don’t drink water before meals. This can fill your stomach and make it harder to get in enough calories.\n\n  2) Eat more often. Squeeze in an additional meal or snack whenever you can, such as before bed.\n\n  3) Drink milk. Drinking whole milk to quench thirst is a simple way to get in more high-quality protein and calories.\n\n  4) Try weight gainer shakes. If you’re really struggling then you can try weight gainer shakes. These are very high in protein, carbs and calories.\n\n  5) Use bigger plates. Definitely use large plates if you’re trying to get in more calories, as smaller plates cause people to automatically eat less.\n\n  6) Add cream to your coffee. This is a simple way to add in more calories.\n\n  7) Take creatine. The muscle building supplement creatine monohydrate can help you gain a few pounds in muscle weight.\n\n  8) Get quality sleep. Sleeping properly is very important for muscle growth.\n\n  9)Eat your protein first and vegetables last. If you have a mix of foods on your plate, eat the calorie-dense and protein-rich foods first. Eat the vegetables last.\n\n  10) Don’t smoke. Smokers tend to weigh less than non-smokers, and quitting smoking often leads to weight gain.")
        input("____________________________________________________________________[Back]")
        clear_screen()
        main_body()
    elif i == '3':     
        print("\n-------------------------- Tips on Stay Healthy --------------------------\n\n  1) Be physically active for 30 minutes most days of the week. Break this up into three 10-minute sessions when pressed for time. Healthy movement may include walking, sports, dancing, yoga, running or other activities you enjoy.\n\n  2) Eat a well-balanced, low-fat diet with lots of fruits, vegetables and whole grains. Choose a diet that's low in saturated fat and cholesterol, and moderate in sugar, salt and total fat.\n\n  3) Brush your teeth after meals with a soft or medium bristled toothbrush. Also brush after drinking and before going to bed. Use dental floss daily.\n\n  4) Stay in touch with family and friends.\n\n  5) Good ways to deal with stress include regular exercise, healthy eating habits and relaxation exercises, such as deep breathing or meditation. Talking to trusted family members and friends can help a lot. Some women find that interacting with their faith community is helpful in times of stress.\n\n  6) Don't smoke, or quit if you do. Ask your health care provider for help. UCSF's Tobacco Education Center offers smoking cessation and relapse prevention classes as well as doctor consultations for smokers trying to quit.")
        input("____________________________________________________________________[Back]")
        clear_screen()
        main_body()
    

def about():
    input("\n____________________________________________________________________\n  Program By Patel Asif Khan\n  Mobile:-+91-8208168203\n  E-mail:-patelasif52@gmail.com\n____________________________________________________________________[Back]")
    clear_screen()
    main_body()

def main_body():
    
    in_app = True
    while in_app == True:
        print("----------------------------- H O M E -----------------------------")
        selection = input("\n  1) Calculate BMI\n  2) Health Tips\n  3) About Us\n  4) Exit\n\n  Enter Your Choice :- ")

        if selection == '1':
            clear_screen()
            bmi_calculation()
        elif selection == '2':
            clear_screen()
            print("------------------------------ T I P S ------------------------------")
            x = input("\n  Select Tips :-\n  1) Tips on Weight Loss\n  2) Tips on Weight Gain\n  3) Tips on Stay Healthy\n\n  Enter Your Choice :- ")
            while x.isdigit() == False or int(x) >= 4:
                print("____________________________________________________________________")
                print("                        Invalid Choice!")
                input("____________________________________________________________________[Retry]")
                clear_screen()
                print("------------------------------ T I P S ------------------------------")
                x = input("\n  Select Tips :-\n  1) Tips on Weight Loss\n  2) Tips on Weight Gain\n  3) Tips on Stay Healthy\n\n  Enter Your Choice :- ")
            print(choice(x))
            clear_screen()
            
        elif selection == '3':
            clear_screen()
            about()
                
                
        elif selection == '4':
            
            in_app = False
        else:
            
            input("____________________________________________________________________\n                        Invalid Entry!!\n____________________________________________________________________[Retry]")
            clear_screen()
    input("---------------------------- T H A N K S ----------------------------")    
    exit()
main_body()      
            


