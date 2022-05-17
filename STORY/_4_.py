import os
import os.path
import bitdotio
import display_module as disp
import pandas as pd
import keyboard
import random
import time

#-----------------------------------------------------------------------------------

path = os.getcwd() #current working dir

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

while True:
    try:
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
    except:
        disp.error("Check your internet connection.")
        time.sleep(3)
        continue
    else:
        break
        
file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

#-----------------------------------------------------------------------------------

os.system('cls')

df = pd.DataFrame({'0':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '1':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '2':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '3':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '4':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '5':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '6':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '7':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '8':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '9':['----------','----------','----------','----------','----------','----------','----------','----------','----------','---MAIN---']})
                    

you = "(-_-)"
dmitri = "()(-_-)T"

you_curloc = [0,0]
you_prevloc = [0,0]

df.loc[5][4] = dmitri

df.loc[you_curloc[0]][you_curloc[1]] = you

def up(you_curloc, you_prevloc):
    if(you_curloc[0] == 0):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[0] = you_curloc[0]-1
    move(you_curloc, you_prevloc)
    
def down(you_curloc, you_prevloc):
    if(you_curloc[0] == 9):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[0] = you_curloc[0]+1
    move(you_curloc, you_prevloc)
    
def left(you_curloc, you_prevloc):
    if(you_curloc[1] == 0):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[1] = you_curloc[1]-1
    move(you_curloc, you_prevloc)
    
def right(you_curloc, you_prevloc):
    if(you_curloc[1] == 9):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[1] = you_curloc[1]+1
    move(you_curloc, you_prevloc)
    
def move(you_curloc, you_prevloc):
    dmitri_flag = 0
    if(df.loc[you_curloc[0]][you_curloc[1]] == dmitri):
        df.loc[you_prevloc[0]][you_prevloc[1]] = you
        df.loc[you_curloc[0]][you_curloc[1]] = dmitri
        you_curloc[0] = you_prevloc[0]
        you_curloc[1] = you_prevloc[1]
        dmitri_flag = 1
    else:
        df.loc[you_curloc[0]][you_curloc[1]] = you
        df.loc[you_prevloc[0]][you_prevloc[1]] = '----------'
        
    os.system('cls')
    print(df)
    
    if(dmitri_flag == 1):
    
        print("\nDMITRI:")
        print("Where are you headed for?")
        
        input()
        
        print("YOU:")
        print("Derkaan.")
        
        input()
        
        print("DMITRI:")
        print("*laughs*")
        print("Mage sent you here, didn't she?")
        
        input()
        
        print("YOU:")
        print("It's not like I had a choice.")
        
        input()
        
        os.system('cls')
        print(df)
        
        print("\nDMITRI:")
        print("You're kidding.")
        print("Boy, you have no idea what you've got yourself into.")
        
        input()
        
        print("YOU:")
        print("If I don't return in a day, you'll come for me, right?")
        
        input()
        
        print("DMITRI:")
        print("Derkaan is off-limits.")
        print("You're on your own.")

        input()
        
        print("YOU:")
        print("Thanks for that.")
        print("Makes me feel safer already.")
        
        input()
        
        os.system('cls')
        print(df)
        
    else:
        pass
        
    if(you_curloc[0] == 9 and you_curloc[1] == 9):
    
        os.system(path+"\\Main.py")
        
    elif(you_curloc[0] == 4 and you_curloc[1] == 0):
    
        while True:
            try:
                b = bitdotio.bitdotio(api)
                conn = b.get_connection()
                cur = conn.cursor()
            except:
                disp.error("Check your internet connection.")
                time.sleep(3)
                continue
            else:
                break
                
        cur.execute(f"update \"siddhanth78/MainGame\".player_progress set story = 4 where p_id = '{player_id}'")
        conn.commit()
        os.system(path+"\\STORY\\_5_.py")

keyboard.add_hotkey('up arrow', lambda:up(you_curloc, you_prevloc))
keyboard.add_hotkey('left arrow', lambda:left(you_curloc, you_prevloc))
keyboard.add_hotkey('down arrow', lambda:down(you_curloc, you_prevloc))
keyboard.add_hotkey('right arrow', lambda:right(you_curloc, you_prevloc))

os.system('cls')

print("\nUSE ARROWS TO MOVE.\n")
print(df)

while True:
    continue