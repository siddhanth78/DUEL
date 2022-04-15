import os
import os.path
import time
import display_module as disp

#-----------------------------------------------------------------------------------

path = os.getcwd() #current working dir

options = ['Story', 'Duel', 'Market', 'Trade', 'Exit', 'Logout'] #menu options

menu = disp.menu(title = "Main Menu",
                items = options,
                reuse = 1
                    )       #main menu

#-----------------------------------------------------------------------------------

os.system('cls')

while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if(choice == "1"):
        print("COMING SOON\n")
    elif(choice == "2"):
        print("COMING SOON\n")
    elif(choice == "3"):
        os.system(path+"\\Market.py")
    elif(choice == "4"):
        print("COMING SOON\n")
    elif(choice == "5"):
        confirm = disp.yesno()
        
        if(confirm == 1):
            break
        elif(confirm == 0):
            continue
        elif(confirm == 2):
            disp.error("Invalid choice.")
            continue
    elif(choice == "5"):
        confirm = disp.custom_yesno("Are you sure you want to log out?")
        
        if(confirm == 1):
            os.system(path+"\\Start.py")
        elif(confirm == 0):
            continue
        elif(confirm == 2):
            disp.error("Invalid choice.")
            continue
    else:
        disp.error("Invalid choice.")