import os
import os.path
import display_module as disp

#-----------------------------------------------------------------------------------

path = os.getcwd() #current working dir

#-----------------------------------------------------------------------------------

os.system('cls')

print("\n-----DUEL-----")

while True:
    choice = input("\n1. Login\n2. Sign up\n3. Quit\n\nEnter your choice: ")
    
    if(choice == "1"):
        os.system(path+"\\Login.py")
    elif(choice == "2"):
        os.system(path+"\\SignUp.py")
    elif(choice == "3"):
        break
    else:
        disp.error("Invalid choice.")
