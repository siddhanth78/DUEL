import os
import os.path

#-----------------------------------------------------------------------------------

path = os.getcwd() #current working dir

#-----------------------------------------------------------------------------------

os.system('cls')

print("\n-----DUEL-----")

while True:
    choice = input("\n1. Login\n2. Sign up\n\nEnter your choice: ")
    
    if(choice == "1"):
        os.system(path+"\\Login.py")
    elif(choice == "2"):
        os.system(path+"\\SignUp.py")
    else:
        print("\nInvalid choice.")
